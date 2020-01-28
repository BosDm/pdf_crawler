from django.db import models
from django.utils.translation import ugettext_lazy as _


class PDFDocument(models.Model):
    name = models.CharField(_('pdf document name'), max_length=1024)
    date_uploaded = models.DateTimeField(_('date created'), auto_now_add=True)

    def __str__(self):
        return self.name


class PDFUrls(models.Model):
    url = models.CharField(_('project title'), unique=True, max_length=2048)
    documents = models.ManyToManyField(
        PDFDocument,
        related_name='urls',
        related_query_name='urls',
    )
    is_live = models.BooleanField()

    class Meta:
        indexes = [
            models.Index(fields=['url']),
        ]

    def __str__(self):
        return self.url
