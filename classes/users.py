class TelegramUser:
    """
    Represents a Telegram user with attributes for user ID, username, user type, and full name.
    """

    def __init__(self, user_id: str = None, username: str = None, user_type: str = None, full_name: str = None) -> None:
        """
        Initializes a new instance of the TelegramUser class.

        :param user_id: The ID of the user.
        :param username: The username of the user.
        :param user_type: The type of the user.
        :param full_name: The full name of the user.
        """
        self.user_id = user_id
        self.username = username
        self.user_type = user_type
        self.full_name = full_name

    def get_username_by_user_id(self, user_id: int) -> str:
        """
        Fetches the username of a Telegram user by their user ID. This method is a placeholder and needs to be implemented.
        https://core.telegram.org/method/users.getFullUser

        :param user_id: The ID of the user.
        :return: The username of the user.
        """
        # Placeholder for the actual implementation
        raise NotImplementedError

    def __repr__(self) -> str:
        """
        Returns a string representation of the TelegramUser object.

        :return: A string representation of the TelegramUser object.
        """
        return f"<TelegramUser {self.__dict__}>"

    def __str__(self) -> str:
        """
        Returns a string representation of the TelegramUser object.

        :return: A string representation of the TelegramUser object.
        """
        return self.__repr__()


class SlackUser:
    """
    Represents a Slack user with attributes for user ID, username, full name, display name, and profile link.
    """

    def __init__(self, user_id: str, username: str, full_name: str = None, display_name: str = None,
                 profile_link: str = None) -> None:
        """
        Initializes a new instance of the SlackUser class.

        :param user_id: The ID of the user.
        :param username: The username of the user.
        :param full_name: The full name of the user.
        :param display_name: The display name of the user.
        :param profile_link: The profile link of the user.
        """
        self.user_id = user_id
        self.username = username
        self.full_name = full_name
        self.display_name = display_name
        self.profile_link = profile_link

    def __repr__(self) -> str:
        """
        Returns a string representation of the SlackUser object.

        :return: A string representation of the SlackUser object.
        """
        return f"<SlackUser {self.__dict__}>"

    def __str__(self) -> str:
        """
        Returns a string representation of the SlackUser object.

        :return: A string representation of the SlackUser object.
        """
        return self.__repr__()
