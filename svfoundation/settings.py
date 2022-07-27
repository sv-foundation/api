"""
Django settings for svfoundation project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from os.path import dirname, abspath, join
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from cloudipsp import Api

import environ

# Initialise environment variables
env = environ.Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', cast=bool, default=True)

ALLOWED_HOSTS = env('ALLOWED_HOSTS', cast=list, default=['*'])
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

API_URL = env('API_URL', default='http://127.0.0.1:8000')
# Application definition

INSTALLED_APPS = [
    'django.contrib.sessions',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_filters',
    'phonenumber_field',
    'rest_framework',
    'django_summernote',
    'corsheaders',
    'news',
    'help',
    'payments'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

CSRF_TRUSTED_ORIGINS = ['https://*.beta.svfoundation.org.ua', 'https://*.127.0.0.1']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'
}

X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'svfoundation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'svfoundation.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE', default='django.db.backends.postgresql_psycopg2'),
        'NAME': env('DB_NAME', default='svfoundation_db'),
        'USER': env('DB_USR', default='postgres'),
        'PASSWORD': env('DB_PWD', default='postgres'),
        'HOST': env('DB_HOST', default='127.0.0.1'),
        'PORT': env('DB_PORT', default='5432')
    }

}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

gettext = lambda s: s

LANGUAGES = (
    ('uk', gettext('Ukrainian')),
    ('en', gettext('English')),
    ('pl', gettext('Polish')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uk'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL: str = '/static/'
STATIC_ROOT: str = join(BASE_DIR, 'static/')
STATICFILES_DIRS = (
    BASE_DIR / "summernote_static",
)
MEDIA_URL: str = '/media/'
MEDIA_ROOT: str = join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

APPEND_SLASH = True

# fondy settings
FONDY_MERCHANT_ID = env('FONDY_MERCHANT_ID', cast=int, default='1396424')
FONDY_KEY = env('FONDY_KEY', default='test')

fondy_api = Api(merchant_id=FONDY_MERCHANT_ID,
                secret_key=FONDY_KEY)

# email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USR')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PWD')
EMAIL_TIMEOUT = 180

SUMMERNOTE_CONFIG = {
    'summernote': {
        'styleTags': [
            'p', 'blockquote', 'pre', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            {'title': "Gallery", 'tag': "div", 'value': "div", 'className': "gallery"},
            {'title': "Gallery Item", 'tag': "div", 'value': "div", 'className': "galleryItem"},
        ],
    },
    'css': (
        '/static/css/summernote_gallery.css',
    )
}
