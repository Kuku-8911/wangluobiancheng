#!/usr/bin/env.python
#._*_ coding:utf-8 _*_
import socket

def main():

    #  AF_INET为IPV4协议，SOCK_DGRAM为udp通信协议
    utp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    win_address = ("192.168.232.129", 6789)

    while True:

        send_input = input("请输入：")

        # 发送数据，只能发送编码，解码为.decode
        utp_socket.sendto(send_input.encode("utf-8"), win_address)

        if send_input == 'exit':
            print('退出聊天')
            print('哈哈哈')
            exit()

    utp_socket.close()

main()
    