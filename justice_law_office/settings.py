"""
Django settings for justice_law_office project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from django.utils.translation import gettext_lazy as _
import os
from pathlib import Path
import types
import dotenv


dotenv.read_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', str)
ENCRYPT_KEY = os.environ.get('ENCRYPT_KEY').encode()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', bool)

ALLOWED_HOSTS = ['192.168.221.131', '127.0.0.1']



# Application definition

INSTALLED_APPS = [
   
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'whitenoise.runserver_nostatic',
    'django.contrib.humanize',
    'django.contrib.sites',
    'clear_cache',
    'crispy_forms',
    'accounts',
    'clients',
    'adversaires',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
   
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware', 
]

SESSION_EXPIRE_SECONDS = 3600  # 30 minutes = 1800 seconds; 1 hour = 3600 seconds
# SESSION_TIMEOUT_REDIRECT = '/accounts/login/'
SESSION_TIMEOUT_REDIRECT = '/'
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
# SESSION_COOKIE_AGE = 3600 * 24 * 30 # One month


ROOT_URLCONF = 'justice_law_office.urls'

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_PATH,
            os.path.join(BASE_DIR, 'views')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':[
                'clients.templatetags.tags',
            ]
        },
    },
]

WSGI_APPLICATION = 'justice_law_office.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT', int),
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, "assets")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 3

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'nga_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'nga_verbose',
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        
        'nga_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/justice.log',
            'when': 'D',
            'interval': 1,
            'utc': True,
            'backupCount': 5,
            'formatter': 'nga_verbose',
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        
        'nga_file_debug': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/justice_debug.log',
            'when': 'D',
            'interval': 1,
            'utc': True,
            'backupCount': 5,
            'formatter': 'nga_verbose',
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        
        'nga_file_warning': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/justice_warning.log',
            'when': 'D',
            'interval': 1,
            'utc': True,
            'backupCount': 5,
            'formatter': 'nga_verbose',
            'level': os.getenv('DJANGO_LOG_LEVEL', 'WARNING'),
        },
        
        'nga_file_error': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/justice_error.log',
            'when': 'D',
            'interval': 1,
            'utc': True,
            'backupCount': 5,
            'formatter': 'nga_verbose',
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
        
        'nga_file_critical': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/justice_critical.log',
            'when': 'D',
            'interval': 1,
            'utc': True,
            'backupCount': 5,
            'formatter': 'nga_verbose',
            'level': os.getenv('DJANGO_LOG_LEVEL', 'CRITICAL'),
        },
    },
    'root': {
        'handlers': ['nga_file', 'nga_console', 'nga_file_warning', 'nga_file_error', 'nga_file_critical'],
         'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
    },
    # 'loggers': {
    #     'django': {
    #         'handlers': ['console'],
    #         'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
    #         'propagate': False,
    #     },
    # },
    
    'formatters': {
        'nga_verbose': {
            'format': '{asctime}: {levelname} [{pathname}: {funcName}:{lineno:d}], {name}, {module}, {process:d}, {thread:d}, {message}',
            'style': '{',
        },
        'nga_simple': {
            'format': '{levelname}, {message}',
            'style': '{',
        },
    },
}
