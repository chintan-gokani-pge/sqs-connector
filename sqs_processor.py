import json

from util.constant import logger, aws_access_key_id, aws_secret_access_key
from util.env import SQS_URL
from util.SQSUtil import SQSUtil
from ast import literal_eval


def send_message():
    sample_messages = [
        {
            'name': 'User1',
            'team': 'team1'
        },
        {
            'name': 'User2',
            'team': 'team2'
        },
        {
            'name': 'User3',
            'team': 'team3'
        }
    ]

    for message in sample_messages:
        str_message = str(message)
        sqs_client = SQSUtil(SQS_URL, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        sqs_client.send_message(str_message)


def sqs_consumer(event, context):
    logger.info('sqs_consumer')
    records = event.get('Records')
    for record in records:
        msg_body = literal_eval(record.get('body'))
        logger.info('msg_body = {}'.format(msg_body))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == '__main__':
    send_message()
