from classes.chats import TelegramChat
from typing import Optional, List, Dict, Any, Union


class TelegramMessage:
    """
    Represents a Telegram message with various attributes like chat details, message ID, type, date, sender details, etc.
    """

    def __init__(self, chat: Optional[TelegramChat] = None, message_id: Optional[int] = None,
                 message_type: Optional[str] = None, date: Optional[str] = None, date_unixtime: Optional[str] = None,
                 from_name: Optional[str] = None, from_id: Optional[str] = None, forwarded_from: Optional[str] = None,
                 text: Optional[str] = None, photo: Optional[str] = None, file: Optional[str] = None,
                 text_entities: Optional[List[Dict[str, Any]]] = None, media: Optional[Any] = None, **kwargs) -> None:
        self.chat = chat
        self.message_id = message_id
        self.message_type = message_type
        self.date = date
        self.date_unixtime = date_unixtime
        self.from_name = from_name
        self.from_id = from_id
        self.from_user_id = self.from_id.split("user")[1] if self.from_id and self.from_id.startswith("user") else None
        self.from_username = None  # TODO: call func to get it by user_id
        self.forwarded_from_name = forwarded_from
        self.text = text
        self.text_entities = text_entities
        self.photo = photo
        self.file = file
        self.media = media
        self.message_link_prefix = "https://t.me/c"
        self.message_link = f"{self.message_link_prefix}/{self.chat.chat_id}/{self.message_id}"

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self) -> str:
        return f"<TelegramMessage {self.__dict__}>"

    def __str__(self) -> str:
        return self.__repr__()


class SlackMessage:
    """
    Represents a Slack message with attributes like timestamp, channel name, username, and text.
    """

    def __init__(self, timestamp_unixtime: Optional[int] = None, channel_name: Optional[str] = None,
                 username: Optional[str] = None, text: Optional[str] = None, media: Optional[Any] = None) -> None:
        self.timestamp_unixtime = timestamp_unixtime
        self.channel_name = channel_name
        self.username = username
        self.text = text
        self.media = media

    def __repr__(self) -> str:
        return f"<SlackMessage {self.__dict__}>"

    def __str__(self) -> str:
        return self.__repr__()

    def prepare_message_to_write_to_file(self) -> Union[str, None]:
        """
        Prepares the Slack message to be written to a file following specific Slack rules.

        :return: A formatted string representation of the Slack message or None if conditions aren't met.
        """
        if not self.username or not self.text:
            return None

        return f'"{self.timestamp_unixtime}","{self.channel_name}","{self.username}","{self.text}"'
