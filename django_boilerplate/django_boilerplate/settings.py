from django.core.urlresolvers import reverse_lazy
import os


PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

# Use debug on local machine. If not using debug and static files are
# being used, you must serve them (i.e. using nginx)
# Note: set env variable WITH VIRTUALENV ACTIVE: export DEBUG=True
# if os.environ['DEBUG'] == 'True':
#     DEBUG = TEMPLATE_DEBUG = True
# else:
#     DEBUG = TEMPLATE_DEBUG = False
DEBUG = TEMPLATE_DEBUG = True

ADMINS = (
    #('<name>', '<email>'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join('db.sqlite3'),     # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

AUTH_USER_MODULE = 'users.UserProfile'
AUTH_PROFILE_MODULE = 'users.UserProfile'

# Required tastypie api settings
ACCOUNT_ACTIVATION_DAYS = 7 
TASTYPIE_DEFAULT_FORMATS = ['json']
API_LIMIT_PER_PAGE = 0
TASTYPIE_ALLOW_MISSING_SLASH = True

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
DATETIME_INPUT_FORMATS = (
    '%m/%d/%Y %I:%M %p',     # '01/01/2001 01:01 AM'

    # '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    # '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    # '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    # '%Y-%m-%d',              # '2006-10-25'
    # '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    # '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    # '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    # '%m/%d/%Y',              # '10/25/2006'
    # '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    # '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    # '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    # '%m/%d/%y',              # '10/25/06'
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_x689jsb088!7sj+h(t%=_nei@))zk%9!*z21t*!vl#mlt71l%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # 'allauth.account.context_processors.account',
    # 'allauth.socialaccount.context_processors.socialaccount',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# AUTHENTICATION_BACKENDS = (
#     "django.contrib.auth.backends.ModelBackend",
#     "allauth.account.auth_backends.AuthenticationBackend",
# )

SOCIALACCOUNT_QUERY_EMAIL = True

CRISPY_FAIL_SILENTLY = not DEBUG

ROOT_URLCONF = 'django_boilerplate.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'django_boilerplate.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), '../templates'),
)

INSTALLED_APPS = (
    # Generic apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # 'django.contrib.comments',

    # additional apps
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',

    'registration',
    'bootstrapform',
    'bootstrap3_datetime',
    'django.contrib.humanize',
    'localflavor',
    'xadmin',
    'crispy_forms',
    'south',
    # 'tastypie,',
    
    # Application specific
    'django_boilerplate',
    'users',
)


# Email settings; must be set in virtualenv
# Use: export EMAIL_HOST_USER='' && export EMAIL_HOST_PASSWORD=''
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']


LOGIN_URL=reverse_lazy("login")
LOGIN_REDIRECT_URL=reverse_lazy("home")
LOGOUT_URL=reverse_lazy("logout")


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Enable debug toolbar and django_extensions
if DEBUG:
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INTERNAL_IPS = ('127.0.0.1',)
    INSTALLED_APPS += ('debug_toolbar', 'django_extensions' )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
