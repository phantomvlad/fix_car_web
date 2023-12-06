import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(".env")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CSRF_COOKIE_SECURE = False
ALLOWED_HOSTS = []

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_ON_GET = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'simple_menu',
    'django_bootstrap5',
    'crispy_forms',
    'crispy_bootstrap5',
    'storages',

    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'cars.apps.CarsConfig',
    'repair.apps.RepairConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.CustomUser'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_FORMS = {'signup': 'users.forms.CustomUserSignupForm'}
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# STORAGE AWS
#DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
#AWS_ACCESS_KEY_ID='b5FeyZU6xui1JTge9LLbQG'
#AWS_SECRET_ACCESS_KEY='amDxoDaGyrmZDB8YeaoXMYPkFobKLjyAxn54ZTytKoHc'
#AWS_STORAGE_BUCKET_NAME='fix-car'
#AWS_S3_ENDPOINT='hb.ru-msk.vkcs.cloud'
#AWS_DEFAULT_REGION='ru-msk'
#AWS_S3_CUSTOM_DOMAIN=f'{AWS_STORAGE_BUCKET_NAME}.hb.ru-msk.vkcs.cloud'
#AWS_S3_OBJECT_PARAMETERS = {
    #'CacheControl': 'max-age=86400',
#}
#AWS_LOCATION='static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
#STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
STATIC_URL = '/static/'
#AWS_DEFAULT_ACL='private'

#STATICFILES_STORAGE= 'storages.backends.s3boto3.S3Boto3Storage'