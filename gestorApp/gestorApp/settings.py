"""
Django settings for gestorApp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Incluir Configuracion BASE DE DATOS

# import databases

# DATABASES = databases.db()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9+()f6f*s^81ocqrclp5b4alay%&^b^!)bvb=rftm^)x6ntx@c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# Fecha actualizado: 10/09/2014
# Cambio realizado: Matricular aplicacion django_evolution en el framework, Ln 47
# Fecha actualizado: 15/09/2014
# Cambio realizado: Desactivar modulo django-evolution
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',	
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gestorApp.urls'

WSGI_APPLICATION = 'gestorApp.wsgi.application'

# Fecha creado: 12/09/2014
# Proposito: Especificar el dierctorio static en el sistema

STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# CAMBIO: 26/08/2014 => Clave de la BD, Ln 66 
# CAMBIO: 01/09/2014 => Usuario y clave de la BD, Ln 67.
# OBSERVACIONES: No publicar
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gestorapp',
        'HOST': 'localhost',
        'PORT': 5432,
        'USER': 'sena',
        'PASSWORD': 'admin'
		#'PASSWORD': 'granados'
}
}



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
# Fecha actualizado: 03/09/2014
# Cambio realizado: Cambiar lenguaje de la interfaz
# Fecha actualizado: 12/09/2014
# Cambio realizado: Interpretacion idioma y zona horaria, Ln 91,94. Desactivacion USE_TZ en False, Ln 101

# LANGUAGE_CODE = 'es-es'
LANGUAGE_CODE = 'es-co'

# TIME_ZONE = 'UTC'
TIME_ZONE =	'America/Panama'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# fecha creado: 12/09/2014
# Proposito: Especificar el directorio root de archivos estaticos, Ln 115

STATIC_ROOT = 'staticfiles'

# Fecha actualizado: 03/09/2014
# Cambio realizado: Enrutar templates del modulo administrador al directorio templates
TEMPLATE_DIRS = (
    'templates',
)
