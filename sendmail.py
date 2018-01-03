# -*- coding: UTF-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
import time

class SendMail:

    def Send(from_address, password, to_address, name_facebook, message):
        subject = u'Facebook: Bạn có thông báo từ {}'.format(name_facebook)
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = "%s" % Header(subject, 'utf-8')
        
        text_message1 = u'"{}" đã gửi cho bạn lời nhắn:\n\n'.format(name_facebook)
        text_message2 = u'<b>"{}"</b>\n'.format(message)
        text_message3 = 'Vào lúc: {}\n'.format(time.strftime("%a, %d %b %Y %H:%M:%S"))
        text_message4 = u"""
        Thân mến\n
        Botchat
        """
        body = text_message1 + text_message2 + text_message3 + text_message4
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        s = smtplib.SMTP('smtp.gmail.com:587')
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(from_address, password)
        text = msg.as_string()
        s.sendmail(from_address, to_address, text)
        s.quit()

# if __name__ == "__main__":
#     x = SendMail
#     x.Send('Your mail', 'Password', 'To address', 'Name Facebook', 'Message')