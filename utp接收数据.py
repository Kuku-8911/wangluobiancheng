#!/usr/bin/env.python
#._*_ coding:utf-8 _*_
import socket

def main():
    utp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    utp_socket.bind(('',6789))

    print('等待接收')
    while True:

        # 接收数据
        utp_recv = utp_socket.recvfrom(500)  #  指定最大接收字符串长度

        send_address = str(utp_recv[1][0]) + str(':') + str(utp_recv[1][1])

        # 接收数据为byte类型，需解码
        send_message = (utp_recv[0]).decode('utf-8')

        if send_message == 'exit':
            print('退出聊天')
            exit()

        print("%s:%s" %(send_address, send_message))

    utp_socket.close()

main()