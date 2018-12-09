#!/usr/bin/env.python
#._*_ coding:utf-8 _*_
import socket
<<<<<<< HEAD

class UdpChat(object):

    def __init__(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(("192.168.130.1",8081))

    def chat(self):

        while True:
            self.send()
            self.recve()

    def send(self):
        win_address = ("192.168.130.1", 8080)

        send_message = input("Plese input the message to send:")

        self.udp_socket.sendto(send_message.encode('utf-8'), win_address)

    def recve(self):

        recve_message = self.udp_socket.recvfrom(1024)
        print(recve_message[0].decode('utf-8'))



if __name__ == '__main__':
    chat = UdpChat()

    chat.chat()
=======
import threading

class UdpChat(object):
    '''udp协议聊天'''

    def __init__(self):
        self.sockte = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sockte.bind(('', 8081))


    def send(self):

        while True:
            win_address = ("192.168.130.1", 8080)
            send_message = input("Plese input the message to send:")

            self.sockte.sendto(send_message.encode('utf-8'), win_address)

    def recve(self):

        while True:

            recve = self.sockte.recvfrom(1024)
            print("\n" + str(recve))

if __name__ == '__main__':
    chat = UdpChat()
    
    # 创建线程，target参数为函数， 可以带参数args,必须为元组类型
    t_send = threading.Thread(target = chat.send)
    t_recve = threading.Thread(target = chat.recve)

    t_send.start()
    t_recve.start()
>>>>>>> dev
