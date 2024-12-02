import configparser
import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailManager:
    def __init__(self, login: str, password: str):
        """
        Конструктор класса MailManager.

        Входные данные:
        login - адрес электронной почты
        password - пароль электронной почты
        """

        self.login = login
        self.password = password

    def send_mail(
        self, smtp_server: str, port: int,
        subject: str, recipients: list[str],
        text: str) -> None:
        """
        Метод для отправки сообщения через сервер smtp.

        Входные данные:
        smtp_server - имя сервера
        port - целочисленный порт
        subject - тема сообщения
        recipients - список электронных адресов получателей
        text - текст сообщения
        """

        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(text))

        smtp = smtplib.SMTP(smtp_server, port)

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(self.login, self.password)
        smtp.sendmail(self.login, recipients, message.as_string())

        smtp.quit()

    def receive_mail(
        self, imap_server: str, folder_name: str,
        header: str) -> email.message.Message:
        """
        Метод для получения сообщения через сервер imap.

        Входные данные:
        imap_server - имя сервера
        folder_name - папка с электронными письмами
        header - часть заголовка письма

        Возвращаемое значение:
        Последнее электронное письмо - объект класса email.message.Message
        """

        email_message = None
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(self.login, self.password)
        imap.select(folder_name)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'

        try:
            result, data = imap.uid('search', None, criterion)
            if not data[0]:
                raise Exception('There are no letters with current header')

            latest_email_uid = data[0].split()[-1]
            result, data = imap.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email.decode("utf-8"))

        except Exception as e:
            print(e)

        imap.logout()
        return email_message


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    login = config['AUTH']['login']
    password = config['AUTH']['password']
    smtp_server = config['SERVER']['smtp']
    port = config['SERVER']['port']
    imap_server = config['SERVER']['imap']
    subject = config['MAIL']['subject']
    recipients = config['MAIL']['recipients'].split(',')
    text = config['MAIL']['text']
    folder_name = config['MAIL']['folder_name']
    header = config['MAIL']['header']

    manager = MailManager(login, password)

    manager.send_mail(
        smtp_server, port, subject,
        recipients, text
    )

    manager.receive_mail(imap_server, folder_name, header)
