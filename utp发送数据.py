#!/usr/bin/env.python
#._*_ coding:utf-8 _*_
import socket

def main():

    utp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    utp_socket.bind(("", 6788))

    win_address = ("192.168.130.1", 8080)

    while True:

        send_input = input("请输入：")
        utp_socket.sendto(send_input.encode("utf-8"), win_address)

        if send_input == 'exit':
            print('退出聊天')
            print('哈哈哈')
            exit()

    utp_socket.close()

main()
    