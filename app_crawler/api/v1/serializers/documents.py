from rest_framework import serializers

from app_crawler.models import PDFDocument


class PDFDocumentSerializer(serializers.ModelSerializer):
    urls = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = PDFDocument
        fields = ('id', 'name', 'urls')


class PDFDocumentUrlsSerializer(PDFDocumentSerializer):
    class Meta(PDFDocumentSerializer.Meta):
        fields = ('urls',)


class PDFDocumentListSerializer(serializers.ModelSerializer):
    urls_count = serializers.IntegerField()

    class Meta:
        model = PDFDocument
        fields = ('id', 'name', 'urls_count')
