"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3r%n10476l2+f0^=!p^z=4+n6ui91x9!1381uoj#&4qefv6q^&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if os.getenv('DJANGO_MODE') == 'production':
    DEBUG =  False 
elif os.getenv('DJANGO_MODE') == 'development':
    DEBUG =  True 

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

PASSWORDLESS_AUTH = {
    # Allowed auth types, can be EMAIL, MOBILE, or both.
    'PASSWORDLESS_AUTH_TYPES': ['MOBILE'],

    # URL Prefix for Authentication Endpoints
    'PASSWORDLESS_AUTH_PREFIX': 'v1/account/',
    
    #  URL Prefix for Verification Endpoints
    'PASSWORDLESS_VERIFY_PREFIX': 'v1/account/verify/',

    # Amount of time that tokens last, in seconds
    'PASSWORDLESS_TOKEN_EXPIRE_TIME': 3 * 60,

    # The user's email field name
    'PASSWORDLESS_USER_EMAIL_FIELD_NAME': 'email',

    # The user's mobile field name
    'PASSWORDLESS_USER_MOBILE_FIELD_NAME': 'mobile',

    # Marks itself as verified the first time a user completes auth via token.
    # Automatically unmarks itself if email is changed.
    'PASSWORDLESS_USER_MARK_EMAIL_VERIFIED': False,
    'PASSWORDLESS_USER_EMAIL_VERIFIED_FIELD_NAME': 'email_is_verified',

    # Marks itself as verified the first time a user completes auth via token.
    # Automatically unmarks itself if mobile number is changed.
    'PASSWORDLESS_USER_MARK_MOBILE_VERIFIED': False,
    'PASSWORDLESS_USER_MOBILE_VERIFIED_FIELD_NAME': 'mobile_is_verified',

    # The email the callback token is sent from
    'PASSWORDLESS_EMAIL_NOREPLY_ADDRESS': None,

    # The email subject
    'PASSWORDLESS_EMAIL_SUBJECT': "Your Login Token",

    # A plaintext email message overridden by the html message. Takes one string.
    'PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE': "Enter this token to sign in: %s",

    # The email template name.
    'PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME': "passwordless_default_token_email.html",

    # Your twilio number that sends the callback tokens.
    'PASSWORDLESS_MOBILE_NOREPLY_NUMBER': None,

    # The message sent to mobile users logging in. Takes one string.
    'PASSWORDLESS_MOBILE_MESSAGE': "Use this code to log in: %s",

    # Registers previously unseen aliases as new users.
    'PASSWORDLESS_REGISTER_NEW_USERS': True,

    # Suppresses actual SMS for testing
    'PASSWORDLESS_TEST_SUPPRESSION': False,

    # Context Processors for Email Template
    'PASSWORDLESS_CONTEXT_PROCESSORS': [],

    # The verification email subject
    'PASSWORDLESS_EMAIL_VERIFICATION_SUBJECT': "Your Verification Token",

    # A plaintext verification email message overridden by the html message. Takes one string.
    'PASSWORDLESS_EMAIL_VERIFICATION_PLAINTEXT_MESSAGE': "Enter this verification code: %s",

    # The verification email template name.
    'PASSWORDLESS_EMAIL_VERIFICATION_TOKEN_HTML_TEMPLATE_NAME': "passwordless_default_verification_token_email.html",

    # The message sent to mobile users logging in. Takes one string.
    'PASSWORDLESS_MOBILE_VERIFICATION_MESSAGE': "Enter this verification code: %s",

    # Automatically send verification email or sms when a user changes their alias.
    'PASSWORDLESS_AUTO_SEND_VERIFICATION_TOKEN': False,

    # What function is called to construct an authentication tokens when
    # exchanging a passwordless token for a real user auth token. This function
    # should take a user and return a tuple of two values. The first value is
    # the token itself, the second is a boolean value representating whether
    # the token was newly created.
    'PASSWORDLESS_AUTH_TOKEN_CREATOR': 'drfpasswordless.utils.create_authentication_token',
    
    # What function is called to construct a serializer for drf tokens when
    # exchanging a passwordless token for a real user auth token.
    'PASSWORDLESS_AUTH_TOKEN_SERIALIZER': 'drfpasswordless.serializers.TokenResponseSerializer',

    # A dictionary of demo user's primary key mapped to their static pin
    'PASSWORDLESS_DEMO_USERS': {},

    # configurable function for sending email
    'PASSWORDLESS_EMAIL_CALLBACK': 'drfpasswordless.utils.send_email_with_callback_token',
    
    # configurable function for sending sms
    'PASSWORDLESS_SMS_CALLBACK': 'utils.sms.verification_sms',

    # Token Generation Retry Count
    'PASSWORDLESS_TOKEN_GENERATION_ATTEMPTS': 3
}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'safedelete',
    "graphene_django",
    'rest_framework',
    'rest_framework.authtoken',
    'ckeditor',
    'drfpasswordless',
    'account',
    'ad',
    'billing',
    'cart',
    'category',
    'collection',
    'comment',
    'gift',
    'notice',
    'order',
    'seller',
    'store',
    'ticket',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

# payment
ZP_MERCHANT = os.getenv('ZP_MERCHANT' ,"ZP_MERCHANT")


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES =  {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASS'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
    }
}

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         },
#         "KEY_PREFIX": "ropomoda"
#     }
# }

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

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
# https://docs.django project.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

AUTHENTICATION_BACKENDS = (
    # default, but now optional
    # This should be removed if you use mailauth.contrib.user or any other
    # custom user model that does not have a username/password
    'django.contrib.auth.backends.ModelBackend',
)



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

API_VERSION = "v1"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication',),
}

GRAPHENE = {
    "SCHEMA": "core.schema.schema"
}

AUTH_USER_MODEL = 'account.User'
# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'

CKEDITOR_FILENAME_GENERATOR = 'account.utils.generate_uuid4_filename'
AWS_QUERYSTRING_AUTH = False

CACHE_TTL = 60 * 15

# GRAPPELLI_ADMIN_TITLE = 'Ropo Moda Admin'

# Celery settings
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')


# cache config
CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": os.getenv('CACHE_LOCATION'),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
            },
            "KEY_PREFIX": os.getenv('CACHE_KEY_PREFIX')
        }
}


if not DEBUG:

    # database config

    DATABASES =  {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASS'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
    }

    # rest framework config

    REST_FRAMEWORK |= {
        'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        )
    }
    
    # secret key config
    
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    

    # s3 storage config
    from .cdn.conf import * # s3
