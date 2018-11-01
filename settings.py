PORT_NUMBER = 8080
APP_NAME='simple_file_uploader'

BUCKET_NAME = 'ts-engineering-test'
AWS_ACCESS_KEY_ID = 'AKIAIFPODV5Z66HLO2VA'
AWS_SECRET_ACCESS_KEY = '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'
REGION_NAME = 'us-east-1'

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s (%(process)d:%(thread)d) [%(levelname)s] (%(name)s:%(funcName)s:%(lineno)s): %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}