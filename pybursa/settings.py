"""
Django settings for pybursa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1+k@yezokyfz7&c%kdxhx=hhrlq2_bezy#8ma7ut=95vp%&rh%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'quadratic',
    'courses',
    'students',
    'coaches',
    'feedbacks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pybursa.urls'

WSGI_APPLICATION = 'pybursa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
ADMINS = (
    ('Admin', 'admin@pybursa.com'), 
    ('Director', 'director@pybursa.com'), 
    ('Manager', 'manager@pybursa.com'),
)

LOGGING = {
    'version': 1,
    'formatters': {
        'student': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
        'course': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file_course': {
            'level': 'DEBUG', 
            'class': 'logging.FileHandler', 
            'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
            'formatter': 'course'
        },
        'file_student': {
            'level': 'WARNING', 
            'class': 'logging.FileHandler', 
            'filename': os.path.join(BASE_DIR, 'students_logger.log'),
            'formatter': 'student'
        },
    },
    'loggers': {
        'courses': {
            'handlers': ['file_course'],
            'level': 'DEBUG',
        },
        'students': {
            'handlers': ['file_student'],
            'level': 'WARNING',
        },
    },
}

try:
    from local_settings import * 
except ImportError:
    print “Warning! local_settings are not defined!”

try:
    from do_settings import * 
except ImportError:
    print “Warning! do_settings are not defined!”