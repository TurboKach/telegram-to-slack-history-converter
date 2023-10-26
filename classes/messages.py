from classes.chats import TelegramChat


class TelegramMessage:
    def __init__(self, chat: TelegramChat = None, message_id: int = None, message_type: str = None, date: str = None,
                 date_unixtime: str = None, from_name: str = None, from_id: str = None, forwarded_from: str = None,
                 text: str = None, photo: str = None, file: str = None, text_entities: list[dict] = None,
                 media=None, **kwargs):
        self.chat: TelegramChat = chat
        self.message_id: int = message_id
        self.message_type: str = message_type
        self.date: str = date
        self.date_unixtime: str = date_unixtime
        self.from_name: str = from_name
        self.from_id: str = from_id
        self.from_user_id: str = self.from_id.split("user")[1] if self.from_id and self.from_id.startswith("user") else None  # FIXME check another types of users
        self.from_username: str = None  # FIXME call func to get it by user_id
        self.forwarded_from_name: str = forwarded_from  # full name of user who's message was forwarded
        self.text: str = text
        self.text_entities: list[dict] = text_entities  # type (formatting), text (content)
        self.photo: str = photo  # path to photo file in Telegram history dir
        self.file: str = file  # path to photo file in Telegram history dir
        self.media = media
        self.message_link_prefix: str = "https://t.me/c"
        self.message_link: str = f"{self.message_link_prefix}/{self.chat.chat_id}/{self.message_id}"
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f"<TelegramMessage {self.__dict__}"

    def __str__(self):
        return self.__repr__()


class SlackMessage:
    """timestamp, channel, username, text"""

    def __init__(self, timestamp_unixtime: int = None, channel_name: str = None, username: str = None, text: str = None,
                 media=None):
        self.timestamp_unixtime: int = timestamp_unixtime
        self.channel_name: str = channel_name
        self.username: str = username
        self.text: str = text
        self.media = media

    def __repr__(self):
        return f"<SlackMessage {self.__dict__}>"

    def __str__(self):
        return self.__repr__()

    def prepare_message_to_write_to_file(self):
        """
        Prepares message to write to file.
        Slack rules:
        1. Separate messages by row
        2. Multi-line messages should be represented by raw newlines, but the text must be enclosed in "
        3. Separate message data by column. Columns must follow this order: timestamp, channel, username, text
        4. Sort messages by timestamp (earlier messages first)
        5. All data must be in a single, uncompressed file
        6. HTML will be escaped or skipped, with the exception of links shared in messages
        """
        if self.username is None or self.text == "":
            return None

        return f'"{self.timestamp_unixtime}","{self.channel_name}","{self.username}","{self.text}"'
