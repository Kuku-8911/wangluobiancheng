#!/usr/bin/env.python
#._*_ coding:utf-8 _*_
import socket

class UdpChat(object):

    def __init__(self):
        pass

    def send(self):
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            win_address = ("192.168.130.1", 8080)
            send_message = input("Plese input the message to send:")

            send_socket.sendto(send_message.encode('utf-8'), win_address)

    def recve(self):
        recve_soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while True:

            ubuntu_address = ("",8081)
            recve_soket.bind(ubuntu_address)

            recve_soket.recvfrom(1024)

if __name__ == '__main__':
    chat = UdpChat()

    chat.send()
    chat.recve()
