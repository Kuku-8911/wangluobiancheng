#!/usr/bin/env.python
#._*_ coding:utf-8 _*_

import socket
from . import parameter

def file_server():

    file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    file_socket.bind(parameter.ADDRESS_WIN)

    file_socket.listen(128) # 最大监听值

    new_socket, address = file_socket.accept()

    file_name = new_socket.recv(1024).decode('utf-8')

    try:
        f = open(file_name, 'rb')
        message = f.readline()

    except:
        print("打开文件失败")

    new_socket.send(message)

if __name__ == '__main__':
    file_server()