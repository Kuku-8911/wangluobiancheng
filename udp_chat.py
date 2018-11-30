#!/usr/bin/env.python
#._*_ coding:utf-8 _*_
import socket

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
