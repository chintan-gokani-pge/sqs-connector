from .env import LOG_LEVEL
import logging

# AWS CONFIG const
aws_secret_access_key = 'aws_secret_key'
aws_access_key_id = 'aws_access_key_id'

logger = logging.getLogger()
if LOG_LEVEL == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)