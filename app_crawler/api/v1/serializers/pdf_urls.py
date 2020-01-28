from rest_framework import serializers

from app_crawler.models import PDFUrls


class PDFUrlSerializer(serializers.ModelSerializer):
    documents_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = PDFUrls
        fields = ('id', 'url', 'is_live', 'documents_count')
