# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# END DEBUG CONFIGURATION


# CELERY BROKER CONFIGURATION
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
# END CELERY BROKER CONFIGURATION


# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'test.jtglabs@gmail.com'
EMAIL_HOST_PASSWORD = 'test_pass'
DEFAULT_FROM_EMAIL = 'test.jtglabs@gmail.com'
# END EMAIL CONFIGURATION


# DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'exp_mgr',  # Or path to database file if using sqlite3.
        'USER': 'postgres',  # Not used with sqlite3.
        'PASSWORD': 'postgres',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}
# END DATABASE CONFIGURATION
#
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
#
# NOSE_ARGS = [
# '--with-coverage',
#     '--cover-package=apps.account, apps.inventory'
# ]

