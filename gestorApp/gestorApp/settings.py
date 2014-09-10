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
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
	'django_evolution',
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
        #'PASSWORD': 'admin'
		#'PASSWORD': 'granados'
}
}



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
# Fecha actualizado: 03/09/2014
# Cambio realizado: Cambiar lenguaje de la interfaz

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Fecha actualizado: 03/09/2014
# Cambio realizado: Enrutar templates del modulo administrador al directorio templates
TEMPLATE_DIRS = (
    'templates',
)
