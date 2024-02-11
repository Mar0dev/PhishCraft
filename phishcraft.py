import smtplib
import argparse
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# Function to read SMTP and sender settings from a file
def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return {
        "smtp": {
            "server": config['smtp']['server'],
            "port": config['smtp']['port'],
            "username": config['smtp']['username'],
            "password": config['smtp']['password']
        },
        "sender": {
            "name": config['sender']['name'],
            "email": config['sender']['email'],
            "reply_to": config['sender']['reply_to']
        }
    }

# Function to read message from a file
def read_message(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

# Function to send email
def send_email(sender_info, smtp_settings, recipient_email, subject, message, is_html):
    msg = MIMEMultipart()
    msg['From'] = Header(f"{sender_info['name']} <{sender_info['email']}>", 'utf-8')
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg['Reply-To'] = sender_info['reply_to']
    msg['X-Priority'] = '1'
    msg['Importance'] = 'high'
    
    if is_html:
        msg.attach(MIMEText(message, 'html'))
    else:
        msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_settings['server'], smtp_settings['port'])
        server.starttls()
        server.login(smtp_settings['username'], smtp_settings['password'])
        server.sendmail(sender_info['email'], recipient_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {recipient_email}.")
    except Exception as e:
        print(f"An error occurred while sending to {recipient_email}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Send emails from a list.")
    parser.add_argument("-l", "--email_list", required=True, help="File containing list of emails.")
    parser.add_argument("-s", "--subject", required=True, help="Subject of the email.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-c", "--content", help="File containing email content as plain text.")
    group.add_argument("-ht", "--html_content", help="File containing email content as HTML.")
    group.add_argument("-m", "--message", help="Directly provide the email message as text.")
    
    args = parser.parse_args()

    # Read configuration settings
    config = read_config('config.ini')
    smtp_settings = config['smtp']
    sender_info = config['sender']

    # Determine the message and format
    message = ""
    is_html = False
    if args.content:
        message = read_message(args.content)
    elif args.html_content:
        message = read_message(args.html_content)
        is_html = True
    elif args.message:
        message = args.message

    # Read email addresses from the file and send emails
    with open(args.email_list, 'r') as file:
        for line in file:
            recipient_email = line.strip()
            if recipient_email:
                send_email(sender_info, smtp_settings, recipient_email, args.subject, message, is_html)

if __name__ == "__main__":
    main()
