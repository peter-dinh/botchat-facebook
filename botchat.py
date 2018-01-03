# -*- coding: UTF-8 -*-

from fbchat import log, Client
from fbchat.models import *
from sendmail import SendMail
import getpass

# Subclass fbchat.Client and override required methods
class Run_App(Client):

    action = 1
    def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type, **kwargs):
        """
            Dung de bat su kien khi co tin nhan moi!
        """
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)

        # if message_object.text == 'Talk with strangers!':
        #     self.action = 2

        if author_id == self.uid:
            if message_object.text == 'Stop!':
                self.action = 0
                message_relay = 'Đã tiếp nhận yêu cầu!!'
                relay = Message(text = message_relay)
                self.send(relay, thread_id=thread_id, thread_type=thread_type)
            if message_object.text == 'Start!':
                self.action = 1
                message_relay = 'Đã tiếp nhận yêu cầu!!'
                relay = Message(text = message_relay)
                self.send(relay, thread_id=thread_id, thread_type=thread_type)

        if self.action == 0:
            return
        else:
            log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
            
            # If you're not the author, echo
            if author_id != self.uid:
                user = self.fetchUserInfo(author_id)[author_id]
                # Đánh dấu “Yêu thích” tin nhắn người gửi
                self.reactToMessage(mid, MessageReaction.LOVE)

                # message_relay = 'Vui lòng chờ trong giây lát!'
                # relay = Message(text = message_relay)
                # self.send(relay, thread_id=thread_id, thread_type=thread_type)

                # message_relay = 'Thông tin người gửi: {}\n'.format(user.name)
                # relay = Message(text = message_relay)
                # self.send(relay, thread_id=thread_id, thread_type=thread_type)

                # message_relay = 'Mã người gửi: {}\n'.format(user.uid)
                # relay = Message(text = message_relay)
                # self.send(relay, thread_id=thread_id, thread_type=thread_type)

                # message_relay = 'Hình ảnh người gửi: {}'.format(user.photo)
                # relay = Message(text = message_relay)
                # self.send(relay, thread_id=thread_id, thread_type=thread_type)

                # message_relay = 'Có phải bạn của chủ nhân: {}\n'.format(user.is_friend)
                # relay = Message(text = message_relay)
                # self.send(relay, thread_id=thread_id, thread_type=thread_type)

                # message_relay = 'Giới tính: {}\n'.format(user.gender)
                # relay = Message(text = message_relay)
                # self.send(relay, thread_id=thread_id, thread_type=thread_type)

                # message_relay = 'Địa chỉ profile: {}\n'.format(user.url)
                # relay = Message(text = message_relay)
                # self.send(relay, thread_id=thread_id, thread_type=thread_type)

                message_relay = 'Bot: Đã nhận được tin nhắn từ "{}" với nội dung là: "{}"'.format(self.fetchThreadInfo(thread_id)[thread_id].name, message)
                relay = Message(text = message_relay)
                self.send(relay, thread_id=thread_id, thread_type=thread_type)

                message_relay = 'Bot: Đang tiến hành gửi mail!'
                relay = Message(text = message_relay)
                self.send(relay, thread_id=thread_id, thread_type=thread_type)
                # Gửi mail
                send_mail = SendMail
                email_from = 'Gmail botchat gửi tin nhắn'
                password = 'Password gmail do google cấp'
                email_to = 'Gmail nhận tin nhắn của botchat'
                send_mail.Send(email_from, password, email_to, user.name, message)

                message_relay = """
                Bot: Thư đã được gửi đến Peter.
                Đừng đi đâu hết!
                Peter sẽ trả lời bạn ngay ~~
                """
                relay = Message(text = message_relay)
                self.send(relay, thread_id=thread_id, thread_type=thread_type)

if __name__ == '__main__':
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    client = Run_App(username,password)
    client.listen()
