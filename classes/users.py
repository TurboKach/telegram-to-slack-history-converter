class TelegramUser:
    def __init__(self, user_id: str = None, username: str = None, user_type: str = None, full_name: str = None, ):
        self.user_id = user_id
        self.username = username
        self.user_type = user_type
        self.full_name = full_name

    def get_username_by_user_id(self, user_id: int):
        """https://core.telegram.org/method/users.getFullUser"""
        raise NotImplementedError

    def __repr__(self):
        return f"<TelegramUser {self.__dict__}>"

    def __str__(self):
        return self.__repr__()


class SlackUser:
    def __init__(self, user_id: str, username: str, full_name: str = None, display_name: str = None,
                 profile_link: str = None):
        self.user_id = user_id
        self.username = username
        self.full_name = full_name
        self.display_name = display_name  # how you can be called after @
        self.profile_link = profile_link  # copy link to profile in slack

    def __repr__(self):
        return f"<SlackUser {self.__dict__}>"

    def __str__(self):
        return self.__repr__()
