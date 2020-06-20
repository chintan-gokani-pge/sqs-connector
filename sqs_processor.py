import json

from util.constant import logger, aws_access_key_id, aws_secret_access_key
from util.env import SQS_URL
from util.SQSUtil import SQSUtil
from ast import literal_eval

from batch_builder.sqs_batch_builder import SQSmessageBuilderClient

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


def send_message_batch():
    batch_id = '1'
    message_entries = SQSmessageBuilderClient(batch_id)
    message_id: int = 1
    sqs_client = SQSUtil(SQS_URL, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    for message in sample_messages:
        str_message = str(message)
        str_message_id = str(message_id)
        message_entries.construct(str_message_id, str_message)
        message_id = message_id + 1
    sqs_client.send_message_batch(message_entries)


# Sample function to sqs Producer
def send_message():
    sqs_client = SQSUtil(SQS_URL, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    for message in sample_messages:
        str_message = str(message)
        sqs_client.send_message(str_message)


# Sample Lambda sqs consumer
def sqs_consumer(event, context):
    logger.info('sqs_consumer')
    records = event.get('Records')
    for record in records:
        msg_body = literal_eval(record.get('body'))
        logger.info('msg_body = {}'.format(msg_body))

    logger.info('sqs_consumer records processed successfully !')


if __name__ == '__main__':
    send_message_batch()



