import os

import ijson
from typing import List, Dict, Optional

from classes.chats import TelegramChat, SlackChannel
from classes.messages import TelegramMessage, SlackMessage
from colorize import Colorize
from envs import ROOT_DIR


class MessageConverter:
    """Converts TelegramMessage to SlackMessage."""

    def __init__(self) -> None:
        self.slack_channel: SlackChannel = SlackChannel()
        self.input_file_path: Optional[str] = None
        self.tg_message_to_convert: Optional[TelegramMessage] = None
        self.slack_message_converted: Optional[SlackMessage] = None
        self.slack_message_for_send: Optional[str] = None
        self.output_dir: str = ROOT_DIR + "/converted_files/"
        self.output_filename: Optional[str] = None
        self.telegram_chat: TelegramChat = TelegramChat()

    def message__convert_tg_to_slack(self) -> None:
        """Converts TelegramMessage to SlackMessage."""
        if not self.tg_message_to_convert:
            raise ValueError("self.tg_message_to_convert must be specified")

        quote = False
        text = r''
        if self.tg_message_to_convert.forwarded_from_name:
            text = fr"*Forwarded from {self.tg_message_to_convert.forwarded_from_name}:*" + "\n"
            quote = True

        converted_text = self.convert_message_text_entities_to_slack_format(self.tg_message_to_convert.text_entities)
        text += converted_text

        if quote:
            text = "\n".join([fr"> {line}" for line in text.splitlines()])

        # Media handling
        if self.tg_message_to_convert.photo:
            text += f"\n\n<{self.tg_message_to_convert.message_link}|[link to photo `{self.tg_message_to_convert.photo}`]>"
        if self.tg_message_to_convert.file:
            text += f"\n\n<{self.tg_message_to_convert.message_link}|[link to file `{self.tg_message_to_convert.file}`]>"

        # Additional attributes handling
        if hasattr(self.tg_message_to_convert, "sticker_emoji"):
            text += f"{self.tg_message_to_convert.sticker_emoji}"
        if hasattr(self.tg_message_to_convert, "poll"):
            text += f"{self.tg_message_to_convert.poll.get('question')}\n\nPoll results:\n"
            for answer in self.tg_message_to_convert.poll.get('answers'):
                text += f"{answer.get('text')} ({answer.get('voters')})\n"

        if not text.strip():
            return

        self.slack_message_converted = SlackMessage(
            timestamp_unixtime=int(self.tg_message_to_convert.date_unixtime),
            channel_name=self.tg_message_to_convert.chat.chat_name,
            username=self.tg_message_to_convert.from_name,
            text=text
        )

    def message__append_slack_to_file(self) -> None:
        """Appends SlackMessage to file."""
        if not self.slack_message_converted:
            return

        with open(self.output_dir + self.output_filename, "a") as f:
            self.slack_message_for_send = self.slack_message_converted.prepare_message_to_write_to_file()
            if not self.slack_message_for_send:
                return
            f.write(self.slack_message_for_send + "\n")

    def convert_and_append_to_file(self, tg_message: TelegramMessage) -> None:
        """Converts a Telegram message to Slack format and appends it to a file."""
        self.slack_message_converted = None
        self.tg_message_to_convert = tg_message
        self.message__convert_tg_to_slack()
        self.message__append_slack_to_file()

    def convert(self):
        """
        Converts all messages in history file from Telegram to Slack format
        by calling message__convert_tg_to_slack() and message__append_slack_to_file()
        and outputs the result to a new file in output/ directory
        """
        # 1. Clean self.tg_message_to_convert and self.slack_message_converted
        # 2. Open telegram history file with ijson for stream reading
        # 3. Iterate over messages in history file
        # 3.1. Convert message to Slack format
        # 3.2. Append message to file
        # 4. Close history file
        # 5. Return absolute path to output file
        # Parse result.json file messages, convert them to Slack format and append to output file

        Colorize.print(
            text='Welcome to Telegram to Slack chat history converter\n',
            text_color=Colorize.FG.lightcyan,
        )
        Colorize.print(
            text=('1. You need to download Telegram chat history in JSON format first\n'
                  '   See https://telegram.org/blog/export-and-more for more details\n'),
            text_color=Colorize.FG.lightcyan,
        )
        colorized_input_text = Colorize.color_text(
            text='2. Enter an absolute path to result.json file:\n   ',
            text_color=Colorize.FG.lightcyan,
        )
        input_file_path = input(colorized_input_text)
        self.input_file_path = input_file_path.strip()

        converted_messages_cnt = 0
        with open(self.input_file_path, 'r') as file:
            parser = ijson.parse(file)
            for prefix, event, value in parser:
                if prefix == 'name':
                    self.telegram_chat.chat_name = value
                elif prefix == 'type':
                    self.telegram_chat.chat_type = value
                elif prefix == 'id':
                    self.telegram_chat.chat_id = value

        Colorize.print(
            text=("\n3. Converting messages to Slack format and saving to file\n"
                  f"    Chat name to be converted: {self.telegram_chat.chat_name}"),
            text_color=Colorize.FG.lightcyan,
        )
        self.output_filename = f"{self.telegram_chat.chat_name.replace(' ', '_')}__for_slack_import.txt"
        Colorize.print(
            text=f"    Output filename: {self.output_filename}\n",
            text_color=Colorize.FG.lightcyan,
        )
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        with open(self.output_dir + self.output_filename, "w") as f:
            f.write("")
        errors = []
        with open(self.input_file_path, 'r') as file:
            messages_iterator = ijson.items(file, 'messages.item')
            for message in messages_iterator:
                message["message_id"] = message.get("id")
                message["message_type"] = message.get("type")
                message["from_name"] = message.get("from")
                tg_msg_obj = TelegramMessage(**message, chat=self.telegram_chat)
                try:
                    self.convert_and_append_to_file(tg_msg_obj)
                except Exception as e:
                    errors.append({"error": e, "message": tg_msg_obj, })
                converted_messages_cnt += 1

        Colorize.print(
            text="Converting finished!\n",
            text_color=Colorize.FG.lightgreen,
        )
        if errors:
            error_filename = f"{self.output_dir}errors_{self.telegram_chat.chat_name.replace(' ', '_')}"
            with open(error_filename, "w") as f:
                f.writelines([f"{str(e)}\n" for e in errors])
            Colorize.print(
                text=(f"There were {len(errors)} errors during converting process. "
                      f"You can find error log in file '{error_filename}'"),
                text_color=Colorize.FG.lightred,
            )

        Colorize.print(
            text=(f"{converted_messages_cnt} messages from {self.telegram_chat.chat_name} "
                  f"chat were successfully converted to Slack format and saved to {self.output_filename} file\n\n"
                  f"Now you can import {self.output_dir}{self.output_filename} file to your Slack workspace.\n"
                  f"See https://slack.com/help/articles/201748703-Import-conversations-from-Slack-classic for more details"),
            text_color=Colorize.FG.lightgreen,
        )

    def convert_message_text_entities_to_slack_format(self, text_entities: List[Dict[str, str]]) -> str:
        """
        Converts Telegram message text entities to Slack format.

        :param text_entities: List of dictionaries with text entities.
        :return: String with Slack-formatted text.
        """
        text = r''

        if not isinstance(text_entities, list):
            raise ValueError("text_entities must be a list")

        for entity in text_entities:
            if not isinstance(entity, dict):
                raise ValueError("text_entities must be a list of dictionaries")

            entity_text = (
                entity.get("text")
                .replace(r'"', r"'")
                .replace(r" ", r" ")
                .replace(r"∙", r"")
            )  # Replace non-breaking space with space

            match entity.get("type"):
                case "plain":
                    formatted_text = fr'{entity_text}'
                case "bot_command":
                    formatted_text = fr'{entity_text}'
                case "bold":
                    formatted_text = fr"*{entity_text}*"
                case "underline":  # Underlined text is not supported in Slack, so we convert it to bold
                    formatted_text = fr"*{entity_text}*"
                case "italic":
                    formatted_text = fr"_{entity_text}_"
                case "strikethrough":
                    formatted_text = fr"~{entity_text}~"
                case "spoiler":  # spoiler text is not supported in Slack, so we convert it to bold
                    formatted_text = fr"*{entity_text}*"
                case "link":
                    formatted_text = fr"{entity_text}"
                case "text_link":
                    formatted_text = fr"<{entity.get('href')}|{entity_text}>"
                case "pre":
                    formatted_text = fr"```{entity_text}```"
                case "hashtag":
                    formatted_text = fr"{entity_text}"
                case "code":
                    formatted_text = fr"`{entity_text}`"
                case "phone":
                    formatted_text = fr"`{entity_text}`"
                case "custom_emoji":
                    formatted_text = ''
                case "sticker":
                    formatted_text = ''
                case "mention":
                    formatted_text = fr"<https://t.me/{entity_text[1:]}|{entity_text}>"
                case "email":
                    formatted_text = fr"{entity_text}"
                case _:
                    raise ValueError(f"Unknown text entity type: {entity.get('type')}, entity: {entity}")

            text += formatted_text

        return text
