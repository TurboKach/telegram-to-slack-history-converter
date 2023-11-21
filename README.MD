# About
This script is made to convert exported Telegram group history into Slack import format, because Slack itself does not provide tools to do it.  
There might be minor bugs or errors so feel free to open [Pull Requests](https://github.com/TurboKach/telegram-to-slack-history-converter/compare) to improve this code.

# Getting started

## Installation
Requires Python 3.8 or higher.

```bash
pip3 install -r requirements.txt
```

## Usage
1. [Download Telegram chat history in **JSON** format](https://telegram.org/blog/export-and-more)
   - for Mac use [this](https://telegram.org/dl/desktop/mac) client to export chat history
2. Run `python main.py` and follow instructions:
   - Enter an **absolute path** to `result.json` file;
   - Get your converted TXT file in `converted_files` directory;
3. [Upload generated TXT file to Slack](https://slack.com/services/import/csv) and press **Start Import**
4. Wait for file processing to finish (you will also receive an email when it's done)
5. Configure the import settings - press the button **Information required** (same page)
   - **User mapping** - map Telegram users to Slack users;
   - **Channel mapping** - map Telegram chats to Slack channels;  
   *current version supports only one Telegram chat export, so make sure there is no other Slack channels offered to import to in case of some data convert bugs*
6. Click **Save Changes** and check your import settings
7. Click **Yes, proceed with this import** if all correct
8. Wait till data import is complete (you will receive an email)

## Notes
If there were any errors on converting, they will be saved in `converted_files` directory

## Current limitations
- Only supports text messages (No images, videos, etc.), but in case if message contains link to image or file, message link will be added to message text
- Only supports one chat at a time
- No tg_user_id <-> tg_username mapping
- No Telegram-Slack user mapping (you will be asked to map users manually)
- Message responses are not linked to original message
- No support for Slack threads
- Text formatting not supported by slack will be converted to bold or left as plain text
- No service messages (e.g. "User joined the group")
- `"` char replaced to `'` in messages due to import problems
