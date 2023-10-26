class TelegramChat:
    def __init__(self, chat_id: str = None, chat_name: str = None, chat_type: str = None):
        self.chat_id: str = chat_id
        self.chat_name: str = chat_name
        self.chat_type: str = chat_type

    def __repr__(self):
        return f"<TelegramChat {self.__dict__}>"

    def __str__(self):
        return self.__repr__()


class SlackChannel:
    def __init__(self, channel_id: str = None, channel_name: str = None, channel_type: str = None):
        self.channel_id: str = channel_id
        self.channel_name: str = channel_name
        self.channel_type: str = channel_type

    def __repr__(self):
        return f"<SlackChannel {self.__dict__}>"

    def __str__(self):
        return self.__repr__()
