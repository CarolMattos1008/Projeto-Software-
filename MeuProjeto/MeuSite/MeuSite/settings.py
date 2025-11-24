"""
Django settings for MeuSite project.
(O resto dos comentários do topo...)
"""

from pathlib import Path
import os # (Import necessário para o MEDIA_ROOT)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings...
SECRET_KEY = "django-insecure-ukgnxo3!wlufbhxnk!f4s%p$x*!@&_!^$uo$*u*pf*81=w+*zi"
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'MeuSite',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "MeuSite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "MeuSite.wsgi.application"


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # ... (Validadores de senha) ...
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


STATIC_URL = "/static/"

STATICFILES_DIRS = [ BASE_DIR / "MeuSite" / "static" ]


STATIC_ROOT = BASE_DIR / 'staticfiles'
# --- Fim da Resolução ---



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CSRF_TRUSTED_ORIGINS = [
    'https://localhost:8000',      # <-- Essa é a que o erro pediu especificamente
    'http://localhost:8000',       # Por garantia
    'http://127.0.0.1:8000',       # Por garantia
    'https://spidery-crypt-69779pgx7ppq25vvr-8000.app.github.dev'# Se quiser, adicione o seu link https://...github.dev aqui também
]