#!/usr/bin/env.python
#._*_ coding:utf-8 _*_
import socket

def tcp_send():

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = ("192.168.130.1", 8080)
    # 连接服务器
    tcp_socket.connect(address)

    while True:
        send_message = input("请输入要发送的内容：")
        # 发送给服务器
        tcp_socket.send(send_message.encode('utf-8'))

if __name__ == '__main__':
    tcp_send()