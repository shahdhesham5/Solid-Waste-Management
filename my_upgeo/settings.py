# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
import ast

try:
    from urllib.parse import urlparse, urlunparse
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
    from urlparse import urlparse, urlunparse
# Load more settings from a file called local_settings.py if it exists
try:
    from my_upgeo.local_settings import *
#    from geonode.local_settings import *
except ImportError:
    from geonode.settings import *

#
# General Django development settings

PROJECT_NAME = 'my_upgeo'


SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# add trailing slash to site url. geoserver url will be relative to this
if not SITEURL.endswith('/'):
    SITEURL = '{}/'.format(SITEURL)

SITENAME = os.getenv("SITENAME", 'my_upgeo')

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "{}.wsgi.application".format(PROJECT_NAME)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', "en")

my_apps=(PROJECT_NAME ,'jazzmin','mapCustomisation', 'sw','mainpage',
'apii','Learning', 'geoleaflet', )
geonode_apps=INSTALLED_APPS
if PROJECT_NAME not in INSTALLED_APPS:
    INSTALLED_APPS = my_apps+geonode_apps
     # 'rest_framework',
     # 'rest_framework.authtoken'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Location of url mappings
ROOT_URLCONF = os.getenv('ROOT_URLCONF', '{}.urls'.format(PROJECT_NAME))

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

TEMPLATES[0]['DIRS'].insert(0, os.path.join(LOCAL_ROOT, "templates"))
loaders = TEMPLATES[0]['OPTIONS'].get('loaders') or ['django.template.loaders.filesystem.Loader','django.template.loaders.app_directories.Loader']
# loaders.insert(0, 'apptemplates.Loader')
TEMPLATES[0]['OPTIONS']['loaders'] = loaders
TEMPLATES[0].pop('APP_DIRS', None)




MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'dj_pagination.middleware.PaginationMiddleware',

    # The setting below makes it possible to serve different languages per
    # user depending on things like headers in HTTP requests.
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'geonode.base.middleware.MaintenanceMiddleware',
    'geonode.base.middleware.ReadOnlyMiddleware',   # a Middleware enabling Read Only mode of Geonode
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d '
                      '%(thread)d %(message)s'
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"], "level": "ERROR", },
        "geonode": {
            "handlers": ["console"], "level": "INFO", },
        "geoserver-restconfig.catalog": {
            "handlers": ["console"], "level": "ERROR", },
        "owslib": {
            "handlers": ["console"], "level": "ERROR", },
        "pycsw": {
            "handlers": ["console"], "level": "ERROR", },
        "celery": {
            "handlers": ["console"], "level": "DEBUG", },
        "mapstore2_adapter.plugins.serializers": {
            "handlers": ["console"], "level": "DEBUG", },
        "geonode_logstash.logstash": {
            "handlers": ["console"], "level": "DEBUG", },
    },
}


CENTRALIZED_DASHBOARD_ENABLED = ast.literal_eval(os.getenv('CENTRALIZED_DASHBOARD_ENABLED', 'False'))
if CENTRALIZED_DASHBOARD_ENABLED and USER_ANALYTICS_ENABLED and 'geonode_logstash' not in INSTALLED_APPS:
    INSTALLED_APPS += ('geonode_logstash',)

    CELERY_BEAT_SCHEDULE['dispatch_metrics'] = {
        'task': 'geonode_logstash.tasks.dispatch_metrics',
        'schedule': 3600.0,
    }

LDAP_ENABLED = ast.literal_eval(os.getenv('LDAP_ENABLED', 'False'))
if LDAP_ENABLED and 'geonode_ldap' not in INSTALLED_APPS:
    INSTALLED_APPS += ('geonode_ldap',)


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissions',
    )
}
ALLOWED_HOSTS=['*']





# max_request_size_to_be_15Mb
DATA_UPLOAD_MAX_MEMORY_SIZE = 15242880


# DATABASES ['new']={
#         #'ENGINE': 'django.db.backends.sqlite3',
#         #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         'ENGINE' :  'django.contrib.gis.db.backends.postgis',
#         'NAME' : 'mygis',
#         'USER' :  'postgres',
#         'HOST': 'localhost',
#         'PASSWORD' : 'postgres',
#         'PORT' : '5432',
#
#     }


# DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
# Add your specific LDAP configuration after this comment:
# https://docs.geonode.org/en/master/advanced/contrib/#configuration

# DATABASES = {
#  'default': {
#      'ENGINE': 'django.contrib.gis.db.backends.postgis',#'django.db.backends.sqlite3',
#      'NAME': 'development',
#      'USER' : 'postgres',
#      'PASSWORD' : 'postgres',
#      'HOST' : 'localhost',
#      'PORT' : '5432',
#
#  },
#  'geonode_imports' : {
#      'ENGINE': 'django.contrib.gis.db.backends.postgis',
#      'NAME': 'geonode_imports',
#      'USER' : 'geonode_user',
#      'PASSWORD' : 'a_password',
#      'HOST' : 'localhost',
#      'PORT' : '5432',
#   }
# }



# To enable the MapStore2 based Client enable those
# print('Mohamed11')
# if 'geonode_mapstore_client' not in INSTALLED_APPS:
#     print('Mohamed22')
#     INSTALLED_APPS += (
#         'mapstore2_adapter',
#         'geonode_mapstore_client',)
#
# GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY = 'mapstore'  # DEPRECATED use HOOKSET instead
# GEONODE_CLIENT_HOOKSET = "geonode_mapstore_client.hooksets.MapStoreHookSet"
# MAPSTORE_DEBUG = True
#
# def get_geonode_catalogue_service():
#     if PYCSW:
#         pycsw_config = PYCSW["CONFIGURATION"]
#         if pycsw_config:
#                 pycsw_catalogue = {
#                     ("%s" % pycsw_config['metadata:main']['identification_title']): {
#                         "url": CATALOGUE['default']['URL'],
#                         "type": "csw",
#                         "title": pycsw_config['metadata:main']['identification_title'],
#                         "autoload": True
#                      }
#                 }
#                 return pycsw_catalogue
#     return None
#
# GEONODE_CATALOGUE_SERVICE = get_geonode_catalogue_service()
#
# MAPSTORE_CATALOGUE_SERVICES = {
#     "Demo WMS Service": {
#         "url": "https://demo.geo-solutions.it/geoserver/wms",
#         "type": "wms",
#         "title": "Demo WMS Service",
#         "autoload": False
#      },
#     "Demo WMTS Service": {
#         "url": "https://demo.geo-solutions.it/geoserver/gwc/service/wmts",
#         "type": "wmts",
#         "title": "Demo WMTS Service",
#         "autoload": False
#     }
# }
#
# MAPSTORE_CATALOGUE_SELECTED_SERVICE = "Demo WMS Service"
#
# if GEONODE_CATALOGUE_SERVICE:
#     MAPSTORE_CATALOGUE_SERVICES[list(GEONODE_CATALOGUE_SERVICE.keys())[0]] = GEONODE_CATALOGUE_SERVICE[list(GEONODE_CATALOGUE_SERVICE.keys())[0]]
#     MAPSTORE_CATALOGUE_SELECTED_SERVICE = list(GEONODE_CATALOGUE_SERVICE.keys())[0]
#
# DEFAULT_MS2_BACKGROUNDS = [{
#         "type": "osm",
#         "title": "Open Street Map",
#         "name": "mapnik",
#         "source": "osm",
#         "group": "background",
#         "visibility": True
#     },
#     {
#         "group": "background",
#         "name": "osm",
#         "source": "mapquest",
#         "title": "MapQuest OSM",
#         "type": "mapquest",
#         "visibility": False
#     }
# ]
#
# # MAPSTORE_BASELAYERS = DEFAULT_MS2_BACKGROUNDS
#
# if 'geonode.geoserver' in INSTALLED_APPS:
#     LOCAL_GEOSERVER = {
#         "type": "wms",
#         "url": OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms",
#         "visibility": True,
#         "title": "Local GeoServer",
#         "group": "background",
#         "format": "image/png8",
#         "restUrl": "/gs/rest"
#     }
#customising admin page
from . import django_jazzmin_settings
JAZZMIN_SETTINGS=django_jazzmin_settings.JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS=django_jazzmin_settings.JAZZMIN_UI_TWEAKS
