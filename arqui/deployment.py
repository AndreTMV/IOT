import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]
DEBUG = False
SECRET_KEY = os.environ['MY_SECRET_KEY']

PUBLIC_BASE_URL = os.environ.get(
    "PUBLIC_BASE_URL", f"https://{os.environ['WEBSITE_HOSTNAME']}")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'releaseVersions.middleware.version_guard',
    'backend.core.middleware.AllowPopupsCOOPMiddleware',
]


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",

    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

connection_string = os.environ.get(
    "CUSTOMCONNSTR_AZURE_POSTGRESQL_CONNECTIONSTRING", "")

connection_params = {
    param.split("=")[0].strip(): param.split("=")[1].strip()
    for param in connection_string.split(";") if "=" in param
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': connection_params.get('Database', 'default_db_name'),
        'USER': connection_params.get('User Id', 'default_user'),
        'PASSWORD': connection_params.get('Password', 'default_password'),
        'HOST': connection_params.get('Server', 'localhost'),
    }
}


STATIC_ROOT = BASE_DIR/'staticfiles'
