"""
Django settings for hinga-weze-procurement project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

from django.contrib.messages import constants as message_constants
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'usv1c&3$zu#6y0$s@*3c(c-+hc3afa2c#cn!o9qvzf(+0#!jcx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    '127.0.0.1',
]

# SECURE_HSTS_SECONDS = 86400
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# X_FRAME_OPTIONS = 'DENY'
# SECURE_HSTS_PRELOAD = True

# Application definition

INSTALLED_APPS = [
    # apps
    'app',
    'backend',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # static css and js compressor
    'compressor',
    # google recaptcha
    'captcha',
    # user agent details
    'django_user_agents',
    # datatable
    'django_tables2',
    # debug toolbar
    # 'debug_toolbar',
    # django_archive
    'django_archive',
    # django_tinymce
    'tinymce',
    # cors
    'corsheaders',
    # Bootstrap Modals
    'bootstrap_modal_forms',
]

TEMPLATE_PATH_BACKEND = 'backend/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # other middleware
    'django_user_agents.middleware.UserAgentMiddleware',
    # debug toolbar
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # cors
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'app.urls'

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
                # app global constants
                'app.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

IS_LOCAL = True
BACKEND_DOMAIN_LOCAL = 'http://127.0.0.1:8000/backend'
BACKEND_DOMAIN_PROD = 'https://192.168.1.121:8000/backend'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hinga_weze_procurement_test_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '/Applications/AMPPS/var/mysql.sock',
        'PORT': '3306',
        # 'HOST': '/var/run/mysqld/mysqld.sock',
        # 'PORT': '3306',
        'OPTIONS': {
            # Ignore MySQL Strict Mode is not set for database connection 'default'
            'sql_mode': 'traditional',
        }
    }
}

ARCHIVE_DIRECTORY = 'backups'
ARCHIVE_FILENAME = '%Y-%m-%d-%H-%M-%S'
ARCHIVE_FORMAT = 'bz2'  # gz, bz2
ARCHIVE_EXCLUDE = (
    'contenttypes.ContentType',
    'sessions.Session',
    'auth.Permission',
    'app.Backups',
)

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Datetime
USE_TZ = True
TIME_ZONE = 'UTC'
APP_CONSTANT_DISPLAY_TIME_ZONE = 'Africa/Kigali'
APP_CONSTANT_DISPLAY_TIME_ZONE_INFO = '(CAT)'
APP_CONSTANT_DISPLAY_DATE_FORMAT = '%a, %d %b %Y'
APP_CONSTANT_DISPLAY_TIME_FORMAT = '%H:%M:%S'
APP_CONSTANT_DISPLAY_DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S'
APP_CONSTANT_INPUT_DATE_FORMAT = '%Y-%m-%d'
APP_CONSTANT_INPUT_TIME_FORMAT = '%H:%M:%S'
APP_CONSTANT_INPUT_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
APP_CONSTANT_DEFAULT_DATETIME = '0001-01-01 00:00:00'
APP_CONSTANT_DEFAULT_DATE = '0001-01-01'
APP_CONSTANT_DEFAULT_TIME = '00:00:00'
APP_CONSTANT_DEFAULT_DATETIME_VALUE = '0001-01-01 00:00:00'
APP_CONSTANT_DEFAULT_DATE_VALUE = '0001-01-01'

USE_I18N = True

USE_L10N = True

MESSAGE_LEVEL = message_constants.DEBUG
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'
COMPRESS_OUTPUT_DIR = 'cache'
# COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
# COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]
COMPRESS_CSS_FILTERS = ["compressor.filters.yuglify.YUglifyCSSFilter"]
COMPRESS_JS_FILTERS = ["compressor.filters.yuglify.YUglifyJSFilter"]

# MEDIA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')

# Redirect
LOGIN_URL = '/hinga-weze-procurement/operators/signin'
CONTACT_URL = '/hinga-weze-procurement/site/contact'

# App Constants
# Project related
APP_CONSTANT_APP_NAME = "CNFA"
APP_CONSTANT_APP_SHORT_NAME = "CNFA"
APP_CONSTANT_APP_NAME_NO_SPACE = "CNFA"
APP_CONSTANT_APP_PACKAGE_NAME = "hinga-weze-procurement"
APP_CONSTANT_APP_VERSION_CODE = "v1.0.0"
APP_CONSTANT_APP_VERSION_NAME = "v1.0.0"
APP_CONSTANT_COMPANY_NAME = "CNFA"
APP_CONSTANT_COMPANY_WEBSITE = "https://www.cnfa.org"
APP_CONSTANT_TECH_SUPPORT_EMAIL_ID = "support@techcible.com"
APP_CONSTANT_ADMIN_SUPPORT_EMAIL_ID = APP_CONSTANT_TECH_SUPPORT_EMAIL_ID

# Email Settings
EMAIL_HOST = 'smtp.zoho.com'
# 587,465
EMAIL_PORT = 465
EMAIL_HOST_USER = 'support@techcible.com'
EMAIL_HOST_PASSWORD = 'Navin@321'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# Email Verification
EMAIL_VERIFICATION_SUBJECT = APP_CONSTANT_APP_NAME_NO_SPACE + " : Email Verification"
EMAIL_VERIFICATION_MESSAGE = "Thank you for registration. An email has been sent for verification."
EMAIL_VERIFICATION_MESSAGE_SUCCESS = "Your email id has been verified successfully. Please login to continue."
EMAIL_VERIFICATION_MESSAGE_WARNING = "Failed to verify your email id!"
EMAIL_VERIFICATION_MESSAGE_ERROR = "Verification Link is not valid!!!"
# Email Reset Password
EMAIL_PASSWORD_RESET_SUBJECT = APP_CONSTANT_APP_NAME_NO_SPACE + " : Reset Password"
EMAIL_PASSWORD_RESET_MESSAGE = "A link has been sent to your registered Email ID to reset your password."
# Email Message
EMAIL_NOTIFICATION_SUBJECT = APP_CONSTANT_APP_NAME_NO_SPACE + " : Notification"
EMAIL_NOTIFICATION_MESSAGE = "Message"

# Google Recptcha
RECAPTCHA_PUBLIC_KEY = '6LcMslYUAAAAAMdx1MtvWa29gOyXAWeTBkxg_zML'
GOOGLE_RECAPTCHA_SECRET_KEY = RECAPTCHA_PRIVATE_KEY = '6LcMslYUAAAAABtumFioJwSzq1wntmrmAUTS9J90'
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True

# General
ERROR_MESSAGE = "Oops! Something went wrong. Please contact admin for support."
MAX_LOGIN_ATTEMPTS_CAPTCHA = 3

# cors
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    '127.0.0.1:8000'
)

# External Library Constants
# User Agent
# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'

# Backend Sections
BACKEND_SECTION_DASHBOARD = 10
BACKEND_SECTION_ORDERS = 20
BACKEND_SECTION_OPERATORS = 30
BACKEND_SECTION_PROFILE = 101
BACKEND_SECTION_CHANGE_PASSWORD = 102
BACKEND_SECTION_SETTINGS = 103
BACKEND_SECTION_HELP = 104

# Operator Permissions
ACCESS_PERMISSION_DASHBOARD_VIEW = 'dashboard-view'
ACCESS_PERMISSION_SETTINGS_VIEW = 'settings-view'
ACCESS_PERMISSION_OPERATOR_CREATE = 'operator-create'
ACCESS_PERMISSION_OPERATOR_UPDATE = 'operator-update'
ACCESS_PERMISSION_OPERATOR_DELETE = 'operator-delete'
ACCESS_PERMISSION_OPERATOR_VIEW = 'operator-view'
ACCESS_PERMISSION_LOG_CREATE = 'log-create'
ACCESS_PERMISSION_LOG_UPDATE = 'log-update'
ACCESS_PERMISSION_LOG_DELETE = 'log-delete'
ACCESS_PERMISSION_LOG_VIEW = 'log-view'
ACCESS_PERMISSION_ORDER_CREATE = 'order-create'
ACCESS_PERMISSION_ORDER_UPDATE = 'order-update'
ACCESS_PERMISSION_ORDER_VIEW = 'order-delete'
ACCESS_PERMISSION_ORDER_DELETE = 'order-view'

# Operator Permissions
STATUS_ACTIVE_COLOR = '#2ECC71'
STATUS_INACTIVE_COLOR = '#7F8C8D'
STATUS_BLOCKED_COLOR = '#E74C3C'
STATUS_UNVERIFIED_COLOR = '#2980B9'
STATUS_UNAPPROVED_COLOR = '#FFC300'

# Model Titles
MODEL_OPERATORS_PLURAL_TITLE = 'Operators'
MODEL_OPERATORS_SINGULAR_TITLE = 'Operator'
MODEL_ORDERS_PLURAL_TITLE = 'Procurement Requests'
MODEL_ORDERS_SINGULAR_TITLE = 'Procurement Request'
MODEL_ORDER_PAYMENTS_PLURAL_TITLE = 'Payment History'
MODEL_ORDER_PAYMENTS_SINGULAR_TITLE = 'Payment History'
MODEL_ORDER_APPROVALS_PLURAL_TITLE = 'Order Approvals'
MODEL_ORDER_APPROVALS_SINGULAR_TITLE = 'Order Approval'
MODEL_ORDER_ATTACHMENTS_PLURAL_TITLE = 'Order Attachments'
MODEL_ORDER_ATTACHMENTS_SINGULAR_TITLE = 'Order Attachment'
MODEL_ORDER_PROPOSALS_PLURAL_TITLE = 'Proposals'
MODEL_ORDER_PROPOSALS_SINGULAR_TITLE = 'Proposal'
MODEL_ORDER_ITEMS_PLURAL_TITLE = 'Order Items'
MODEL_ORDER_ITEM_SINGULAR_TITLE = 'Order Item'
MODEL_NOTIFICATIONS_PLURAL_TITLE = 'Notifications'
MODEL_NOTIFICATIONS_SINGULAR_TITLE = 'Notification'
MODEL_BACKUPS_PLURAL_TITLE = 'Backups'
MODEL_BACKUPS_SINGULAR_TITLE = 'Backup'

# Image Extensions
MAX_IMAGE_UPLOAD_SIZE = 4 * 1024 * 1024  # 4MB
VALID_IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg']
VALID_IMAGE_MIMES = ("image/png", "image/jpeg")

TINYMCE_DEFAULT_CONFIG = {
    'height': 300,
    'width': '100%',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

# Colors
COLOR_PRIMARY = '#3498DB'
COLOR_PRIMARY_DARK = '#2E86C1'
COLOR_PRIMARY_LIGHT = '#5DADE2'
