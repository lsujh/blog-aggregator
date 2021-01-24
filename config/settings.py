import os
import dj_database_url
from pathlib import Path
from decouple import config
from django.contrib.messages import constants as messages


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY", default="very-secret-key")
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'blog-agregator.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.postgres',
    'django.contrib.sitemaps',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.openid',
    'crispy_forms',
    "bootstrap4",
    "mptt",
    "easy_thumbnails",
    "meta",
    "ckeditor",
    "ckeditor_uploader",

    'accounts',
    'blog',
    'comments',
    'likes',
    'bookmark',
    'badwordfilter',
    'contact',
]

AUTH_USER_MODEL = 'accounts.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates'),],
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

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": "ihor",
        "USER": "ihor",
        "PASSWORD": "ihor",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = config("EMAIL_HOST", default=None)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default=None)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default=None)
EMAIL_PORT = config("EMAIL_PORT", cast=int, default=0)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=False)
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#          'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         },
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     },
#     'facebook': {
#         'METHOD': 'oauth2',
#         'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
#         'SCOPE': ['email', 'public_profile'],
#         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#         'INIT_PARAMS': {'cookie': True},
#         'FIELDS': [
#             'id',
#             'first_name',
#             'last_name',
#             'middle_name',
#             'name',
#             'name_format',
#             'picture',
#             'short_name'
#         ],
#         'EXCHANGE_TOKEN': True,
#         'LOCALE_FUNC': 'path.to.callable',
#         'VERIFIED_EMAIL': False,
#         'VERSION': 'v7.0',
#     },
#     'linkedin': {
#         'SCOPE': [
#             'r_basicprofile',
#             'r_emailaddress'
#         ],
#         'PROFILE_FIELDS': [
#             'id',
#             'first-name',
#             'last-name',
#             'email-address',
#             'picture-url',
#             'public-profile-url',
#         ]
#     },
#
# }

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True

LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

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

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
# STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = str(BASE_DIR.joinpath('static'))
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))

META_DEFAULT_KEYWORDS = [
]

META_INCLUDE_KEYWORDS = ['блог-агрегатор', 'про все',
  ]

THUMBNAIL_ALIASES = {
    "": {
        "mini": {"size": (100, 100), "crop": True},
        "avatar": {"size": (200, 200), "crop": True},
        "small": {"size": (300, 300), "crop": True},
        "large": {"size": (800, 800), "crop": True},
    },
}

from ckeditor.configs import DEFAULT_CONFIG

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False

# CKEDITOR_CONFIGS = {
#     'default': {
#      'toolbar': 'None'
#     },
# }
CUSTOM_TOOLBAR = [
    {
        "name": "document",
        "items": [
            "Styles",
            "Format",
            "Bold",
            "Italic",
            "Underline",
            "Strike",
            "-",
            "TextColor",
            "BGColor",
            "-",
            "JustifyLeft",
            "JustifyCenter",
            "JustifyRight",
            "JustifyBlock",
        ],
    },
    {
        "name": "widgets",
        "items": [
            "Undo",
            "Redo",
            "-",
            "NumberedList",
            "BulletedList",
            "-",
            "Outdent",
            "Indent",
            "-",
            "Link",
            "Unlink",
            "-",
            "Image",
            "CodeSnippet",
            "Table",
            "HorizontalRule",
            "Smiley",
            "SpecialChar",
            "-",
            "Blockquote",
            "-",
            "ShowBlocks",
            "Maximize",
        ],
    },
]

CKEDITOR_CONFIGS = {
    "default": DEFAULT_CONFIG,
    "my-custom-toolbar": {
        "skin": "moono-lisa",
        "toolbar": CUSTOM_TOOLBAR,
        "toolbarGroups": None,
        "extraPlugins": ",".join(["image2", "codesnippet"]),
        "removePlugins": ",".join(["image"]),
        "codeSnippet_theme": "xcode",
    },
}

# LOGGING_CONFIG = "logging.config.dictConfig"
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "default": {
#             "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             "datefmt": "%Y-%m-%d %H:%M:%S",
#         },
#     },
#     "handlers": {
#         "file": {
#             "level": "INFO",
#             "class": "logging.FileHandler",
#             "formatter": "default",
#             "filename": os.path.join(BASE_DIR, "logs/django/debug.log"),
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["file"],
#             "propagate": True,
#             "level": "INFO",
#         },
#     },
# }
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
