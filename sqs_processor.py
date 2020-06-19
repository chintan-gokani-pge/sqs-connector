import logging
from util.constant import aws_access_key_id, aws_secret_access_key
from util.env import SQS_URL
from util.SQSUtil import SQSUtil

logger = logging.getLogger()
logger.setLevel(logging.INFO)


if __name__ == '__main__':
    sample_messages = [
        {
            'name': 'Nirav',
            'country': 'india'
        },
        {
                'name': 'Sanjay',
                'country': 'india'
        },
        {
                'name': 'Nadim',
                'country': 'india'
        }
    ]

    for message in sample_messages:
        sqs_client = SQSUtil(SQS_URL,aws_access_key_id= aws_access_key_id, aws_secret_access_key= aws_secret_access_key)
        sqs_client.send_message(msg_body=message)
