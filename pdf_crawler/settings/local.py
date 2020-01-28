from pdf_crawler.settings.common import *
from pdf_crawler.settings.rest_framework import *


ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pdf_crawler',
        'USER': 'root_comeet',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
