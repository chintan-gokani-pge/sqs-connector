import os

# SQS Config
SQS_URL= os.getenv('sqs_arn', 'https://sqs.us-west-2.amazonaws.com/{account-ID}/poc-connector')
SQS_REGION_NAME = os.getenv('sqs_region_name', "us-west-2")
SQS_VERIFY_SSL = os.getenv('sqs_ssl_enabled', False)
SQS_MAX_MESSAGES_TO_RECEIVE = os.getenv('sqs_max_message_to_receive', 1)

# Logger Config:
LOG_LEVEL = os.getenv('log_level', 'INFO')