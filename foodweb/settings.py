#-*- coding: UTF-8 -*-
"""
Django settings for foodweb project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0!gpwnt-(6_e^hxe66qx3^6*ajv%^8fkaqib2kxm3mi!gt^r!_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurants',
]
## 若有新增元件，要同步資料庫 $ python manage.py migrate  (django > 1.7 )
MIDDLEWARE_CLASSES = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',    # add by Kuanhua
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'foodweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'foodweb/templates'),
                 os.path.join(BASE_DIR, 'restaurants/templates')],
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

WSGI_APPLICATION = 'foodweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

##CSRF_COOKIE_SECURE = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-STATIC_URL
# STATIC_URL
# Default: None
# URL to use when referring to static files located in STATIC_ROOT.
# Example: "/static/" or "http://static.example.com/"
# If not None, this will be used as the base path for asset definitions (the Media class) and the staticfiles app.
# It must end in a slash if set to a non-empty value.
# You may need to configure these files to be served in development and will definitely need to do so in production.

STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-STATICFILES_DIRS
# STATICFILES_DIRS
# Default: []
# This setting defines the additional locations the staticfiles app will traverse if the FileSystemFinder finder is enabled, e.g. if you use the collectstatic or findstatic management command or use the static file serving view.
# This should be set to a list or tuple of strings that contain full paths to your additional files directory(ies) e.g.:
#
# STATICFILES_DIRS = (
#     "/home/special.polls.com/polls/static",
#     "/home/polls.com/polls/static",
#     "/opt/webfiles/common",
# )
# Note that these paths should use Unix-style forward slashes, even on Windows (e.g. "C:/Users/user/mysite/extra_static_content").
# Prefixes (optional)¶
# In case you want to refer to files in one of the locations with an additional namespace, you can optionally provide a prefix as (prefix, path) tuples, e.g.:
# STATICFILES_DIRS = (
#     # ...
#     ("downloads", "/opt/webfiles/stats"),
# )
# For example, assuming you have STATIC_URL set to '/static/', the collectstatic management command would collect the “stats” files in a 'downloads' subdirectory of STATIC_ROOT.
# This would allow you to refer to the local file '/opt/webfiles/stats/polls_20101022.tar.gz' with '/static/downloads/polls_20101022.tar.gz' in your templates, e.g.:
# <a href="{% static "downloads/polls_20101022.tar.gz" %}">

STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static'),
)

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-STATIC_ROOT
# STATIC_ROOT
# Default: None
# The absolute path to the directory where collectstatic will collect static files for deployment.
# Example: "/var/www/example.com/static/"
# If the staticfiles contrib app is enabled (default) the collectstatic management command will collect static files into this directory. See the howto on managing static files for more details about usage.
# !!Warning
# This should be an initially empty destination directory for collecting your static files from their permanent locations into one directory for ease of deployment; it is not a place to store your static files permanently. You should do that in directories that will be found by staticfiles’s finders, which by default, are 'static/' app sub-directories and any directories you include in STATICFILES_DIRS).

# STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'assets')

SESSION_SERIALIZER = 'django.contrib.sessions.serializers'+'.PickleSerializer'

LOGIN_REDIRECT_URL = "/index/"




