"""
Django settings for birthdaysite project.

Generated by 'django-admin startproject' using Django 2.0.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!kw&1m099)z=h%5ksgjo@slf&*9=pnob4k#yefpuxpe+s@bmm^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
]
MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    },
]
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
ROOT_URLCONF = 'birthdaysite.urls'
WSGI_APPLICATION = 'birthdaysite.wsgi.application'
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'