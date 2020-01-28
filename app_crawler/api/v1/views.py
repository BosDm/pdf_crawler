from django.db import transaction
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView

from app_crawler.api.v1.serializers.documents import (
    PDFDocumentSerializer, PDFDocumentListSerializer, PDFDocumentUrlsSerializer
)
from app_crawler.api.v1.serializers.pdf_urls import PDFUrlSerializer
from app_crawler.models import PDFDocument, PDFUrls
from app_crawler.api.v1.utils import extract_urls_from_pdf, is_url_live


class PDFDocumentListCreate(ListCreateAPIView):
    queryset = PDFDocument.objects.annotate(urls_count=Count('urls')).all()
    serializer_class = PDFDocumentListSerializer

    def _save_document(self, serializer_cls, name):
        pdf_document_data = {
            'name': name,
        }
        serializer = serializer_cls(data=pdf_document_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.instance

    def _save_urls(self, document_id, extract_urls):
        for url in extract_urls:
            is_live = is_url_live(url)
            try:
                obj = PDFUrls.objects.get(url=url)
            except ObjectDoesNotExist:
                url_data = {'url': url, 'is_live': is_live, 'documents': [document_id]}
                serializer = PDFUrlSerializer(data=url_data)
                serializer.is_valid(raise_exception=True)
                obj = serializer.save()
            else:
                if not is_live == obj.is_live:
                    obj.is_live = is_live
            obj.documents.add(document_id)
            obj.save()

    def create(self, request, *args, **kwargs):
        create_serializer = PDFDocumentSerializer

        file = request.data['package']
        extract_urls = extract_urls_from_pdf(file)

        with transaction.atomic():
            document = self._save_document(create_serializer, str(file.name))
            self._save_urls(document.id, extract_urls)
        document.refresh_from_db()

        return Response(create_serializer(document).data, status=status.HTTP_201_CREATED)


class PDFDocumentRetrieve(RetrieveAPIView):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer


class PDFDocumentRetrieveUrls(RetrieveAPIView):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentUrlsSerializer


class PDFUrlList(ListAPIView):
    queryset = PDFUrls.objects.annotate(documents_count=Count('documents')).all()
    serializer_class = PDFUrlSerializer
