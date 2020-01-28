from django.conf.urls import url

from app_crawler.api.v1.views import (
    PDFDocumentListCreate, PDFDocumentRetrieve, PDFDocumentRetrieveUrls, PDFUrlList
)


from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^documents/$', PDFDocumentListCreate.as_view()),
    url(r'^documents/(?P<pk>\d+)/$', PDFDocumentRetrieve.as_view()),
    url(r'^documents/(?P<pk>\d+)/urls/$', PDFDocumentRetrieveUrls.as_view()),

    url(r'^urls/$', PDFUrlList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
