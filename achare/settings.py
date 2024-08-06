from datetime import timedelta
from pathlib import Path
from decouple import config, Csv

# -------------------------------------------------- GENERAL -----------------------------------------------------------
SECRET_KEY = config('SECRET_KEY', cast=str)
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

BASE_DIR = Path(__file__).resolve().parent.parent

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'core_apps.accounts.apps.AccountsConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'achare.urls'

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

WSGI_APPLICATION = 'achare.wsgi.application'
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'

ADMIN_URL = config('ADMIN_URL', cast=str)

# ------------------------------------------------- MEDIA & STATIC -----------------------------------------------------
STATIC_URL = 'static/'
STATIC_ROOT = 'staticfiles/'

MEDIA_URL = 'media/'
MEDIA_ROOT = 'mediafiles/'

# --------------------------------------------------- DATABASE ---------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'HOST': config('DB_HOST'),
        'PASSWORD': config('DB_PASSWORD'),
        'PORT': config('DB_PORT'),
        'USER': config('DB_USER'),
    }
}

# ---------------------------------------------------- LOGGING ---------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s -> %(message)s'
        },
    },
    'handlers': {
        'django_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'simple'
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'django': {
            'handlers': ['django_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# --------------------------------------------------- AUTH -------------------------------------------------------------
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Token', 'token'),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'SIGNING_KEY': config('SECRET_KEY'),
    'UPDATE_LAST_LOGIN': True,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

OTP_TIMEOUT_SECONDS = config('OTP_TIMEOUT_SECONDS', cast=int)

MAXIMUM_ALLOWED_LOGIN_REQUESTS = config('MAXIMUM_ALLOWED_LOGIN_REQUESTS', cast=int)
MAXIMUM_ALLOWED_REGISTER_REQUESTS = config('MAXIMUM_ALLOWED_LOGIN_REQUESTS', cast=int)

LOGIN_REQUEST_BLOCK_TIMEOUT_MINUTES = config('LOGIN_REQUEST_BLOCK_TIMEOUT_MINUTES', cast=int)
LOGIN_REQUEST_BLOCK_TIMEOUT_SECONDS = LOGIN_REQUEST_BLOCK_TIMEOUT_MINUTES * 60
REGISTER_REQUEST_BLOCK_TIMEOUT_MINUTES = config('REGISTER_REQUEST_BLOCK_TIMEOUT_MINUTES', cast=int)
REGISTER_REQUEST_BLOCK_TIMEOUT_SECONDS = REGISTER_REQUEST_BLOCK_TIMEOUT_MINUTES * 60
