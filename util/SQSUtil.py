import boto3
from util.env import SQS_REGION_NAME, SQS_MAX_MESSAGES_TO_RECEIVE, SQS_VERIFY_SSL
from util.constant import logger
from batch_builder.sqs_batch_builder import SQSmessageBuilderClient


class SQSUtil:

    def __init__(self, queue_arn, region_name=SQS_REGION_NAME, ssl_enabled=SQS_VERIFY_SSL,
                 aws_access_key_id=None, aws_secret_access_key=None):
        self._queue_url = queue_arn
        self._client = boto3.client(
            service_name="sqs", region_name=region_name, verify=ssl_enabled,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    def send_message(self, msg_body: str, msg_delay: int = 0, msg_attributes: dict = {}):
        if not msg_body or (msg_delay < 0 or msg_delay > 900):
            return None
        response = self._client.send_message(
            QueueUrl=self._queue_url,
            DelaySeconds=msg_delay,
            MessageBody=msg_body,
            MessageAttributes=msg_attributes,
        )
        logger.info(response['MessageId'])
        return response

    def send_message_batch(self, msg_entries: SQSmessageBuilderClient):
        response = self._client.send_message_batch(
            QueueUrl=self._queue_url,
            Entries=msg_entries.get_message_entries()
        )
        print(response)
        logger.info(response)
        return response

    def receive_message(self, msg_attribute_name='All'):
        messages = self._client.receive_message(
            QueueUrl=self._queue_url,
            MessageAttributeNames=[msg_attribute_name],
            MaxNumberOfMessages=SQS_MAX_MESSAGES_TO_RECEIVE,
        ).get("Messages")

        return messages
