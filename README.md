
# PhishCraft

A simple python tool for sending mass phishing emails :envelope:


## Features

- Quickly send mass emails
- Spoof sender name and email :unlock:
- Configure reply-to header
- Few message types accepted, including HTML


## Requirements

- Python 3 (tested with 3.11.7)
- SMTP server - it can be gmail or any other


## Installation & Configuration

#### To install this tool:

```bash
  git clone https://github.com/Mar0dev/PhishCraft.git
  cd ./PhishCraft
```
#### Configuration:

Configuration is in `config.ini` file that should be located in the same folder as main script.

```ini
[smtp]
server = smtp-server.example            # SMTP server address
port = 587                              # SMTP server port
username = username@for.smtp            # SMTP username
password = yoursmtppassword             # SMTP password

[sender]
name = IT Support                       # Spoofed name of sender
email = support@yourcompany.com         # Spoofed sender email
reply_to = support0@protonmail.com      # Reply-to header
```

`[smtp]` section is standard SMTP relay configuration.

In `[sender]` section the `name` is the name of the sender that will be dispalyed in an email. 

`email` parameter is the email that will be spoofed. Phishing messages will look like they are coming from this email.

`reply_to` value will be used when someone will try to reply to phishing email. It can have the same value as `email` if you don't want recipient reply to different email address.
## Usage/Examples

```bash
python3 ./phishcraft.py -h
```
Will display help for a tool:

```bash
usage: phishcraft.py [-h] -l EMAIL_LIST -s SUBJECT (-c CONTENT | -ht HTML_CONTENT | -m MESSAGE)

options:
  -h, --help            show this help message and exit
  -l EMAIL_LIST, --email_list EMAIL_LIST
                        File containing list of emails.
  -s SUBJECT, --subject SUBJECT
                        Subject of the email.
  -c CONTENT, --content CONTENT
                        .txt file containing email content as plain text.
  -ht HTML_CONTENT, --html_content HTML_CONTENT
                        .html file containing email content as HTML.
  -m MESSAGE, --message MESSAGE
                        Directly provide the email message as text.

```
#### Examples:

Send emails to recipients from the list with basic message:

`python3 ./phishcraft.py -l '/path/to/list.txt' -s "Subject of email" -m "basic message" `

Send emails to recipients from the list with message from .txt file:

`python3 ./phishcraft.py -l '/path/to/list.txt' -s "Subject" -m '/path/to/message.txt' `

Send emails to recipients from the list with HTML message:

`python3 ./phishcraft.py -l '/path/to/list.txt' -s "Subject" -m '/path/to/content.html' `
### Files description

`content.html` is an example of HTML message

`list.txt` shows the format of email addresses list

`config.ini` is a configuration file

### Usage limitation

This tool is designed exclusively for authorized internal phishing assessments and security awareness training within an organization. Its use is strictly limited to educational purposes to help improve the organization's defense against cyber threats by increasing awareness and resilience against phishing attacks among employees.

Users assume full liability for any consequences resulting from the use of the tool.
## License

[MIT](https://choosealicense.com/licenses/mit/)


