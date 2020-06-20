
class SQSmessageBuilderClient:

    def __init__(self, batch_id: str):
        self._id = batch_id
        self._entries = list()

    def construct(self, msg_id: str, msg_body: str, msg_delay: int = 0, msg_attributes: dict = {}):
        message = {
            'Id': msg_id,
            'MessageBody': msg_body,
            'DelaySeconds': msg_delay,
            'MessageAttributes': msg_attributes,
            # 'MessageGroupId': self._id
        }
        self._entries.append(message)

    def get_message_entries(self):
        print(self._entries)
        return self._entries
