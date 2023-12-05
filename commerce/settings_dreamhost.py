from .settings import *


ALLOWED_HOSTS = ['deals.uaa490.org', 'www.deals.uaa490.org']
DEBUG=False

STATIC_ROOT = '/home/deals490/deals.uaa490.org/public/static/'
MEDIA_ROOT = '/home/deals490/deals.uaa490.org/public/media/'


DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.mysql',
	'NAME': 'dbdeals490',
	'USER': 'dbuserdeals490',
	'PASSWORD': 'throggenbottom',
	'HOST': 'mysql.deals.uaa490.org',
	'PORT': '3306',
    }
}

