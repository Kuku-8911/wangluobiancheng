#!/usr/bin/env.python
#._*_ coding:utf-8 _*_

import socket

def down_file(file_name):

    file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 服务器地址
    server_address = ("192.168.130.1", 8081)

    # 连接服务器
    file_socket.connect(server_address)

    # 发送要下载的文件名
    file_socket.send(file_name.encode('utf-8'))

    # 接收最大为1M的文件
    receive_message = file_socket.recv(1024*1024)

    # 在本地写入接收到的文件
    with open("d" + file_name, "wb") as f:
        f.write(receive_message)

    file_socket.close()

if __name__ == '__main__':
    down_file("dt2.txt")
