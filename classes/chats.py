class TelegramChat:
    """
    Represents a Telegram chat with attributes for ID, name, and type.
    """

    def __init__(self, chat_id: str = None, chat_name: str = None, chat_type: str = None) -> None:
        """
        Initializes a new instance of the TelegramChat class.

        :param chat_id: The ID of the chat.
        :param chat_name: The name of the chat.
        :param chat_type: The type of the chat.
        """
        self.chat_id: str = chat_id
        self.chat_name: str = chat_name
        self.chat_type: str = chat_type

    def __repr__(self) -> str:
        """
        Returns a string representation of the TelegramChat object.

        :return: A string representation of the TelegramChat object.
        """
        return f"<TelegramChat {self.__dict__}>"

    def __str__(self) -> str:
        """
        Returns a string representation of the TelegramChat object.

        :return: A string representation of the TelegramChat object.
        """
        return self.__repr__()


class SlackChannel:
    """
    Represents a Slack channel with attributes for ID, name, and type.
    """

    def __init__(self, channel_id: str = None, channel_name: str = None, channel_type: str = None) -> None:
        """
        Initializes a new instance of the SlackChannel class.

        :param channel_id: The ID of the channel.
        :param channel_name: The name of the channel.
        :param channel_type: The type of the channel.
        """
        self.channel_id: str = channel_id
        self.channel_name: str = channel_name
        self.channel_type: str = channel_type

    def __repr__(self) -> str:
        """
        Returns a string representation of the SlackChannel object.

        :return: A string representation of the SlackChannel object.
        """
        return f"<SlackChannel {self.__dict__}>"

    def __str__(self) -> str:
        """
        Returns a string representation of the SlackChannel object.

        :return: A string representation of the SlackChannel object.
        """
        return self.__repr__()
