#!/usr/bin/env.python
#._*_ coding:utf-8 _*_

import socket
from parameter import *

def file_server():

    file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    file_socket.bind(ADDRESS_WIN)

    file_socket.listen(128) # 最大监听值
    print("等待客户端连接...")

    while True:

        # 接收客户
        new_socket, address = file_socket.accept()

        if address:
            print("客户端:%s:%s 连接成功"% (address[0], address[1]))

        while True: # 进入到单个客户循环
            # 接收要下载的文件名
            file_name = new_socket.recv(1024).decode('utf-8')

            # 客户退出连接时，file_name解阻塞，并且返回值为空，退出当前客户循环
            if not file_name:
                print("客户端:%s:%s 已退出连接" % (address[0], address[1]))
                break
             # 发送文件
            try:
                f = open(file_name, 'rb')
                print("正在发送文件...")
                for index, line in enumerate(f): # 返回文件行数，已及每行内容

                    if line:
                        new_socket.send(line)

                # 文件传输完成后发送传输完成标志
                new_socket.send(("^^").encode('utf-8'))


                print("已经将文件[%s]发送给了%s"% (file_name, address))

            except:
                print("没有该文件，请重新输入要下载的文件名")

        new_socket.close()

    file_socket.close()

if __name__ == '__main__':
    file_server()