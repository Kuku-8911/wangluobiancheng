#!/usr/bin/env.python
#._*_ coding:utf-8 _*_

import socket

def down_file():

    file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 服务器地址
    server_address = ("192.168.130.1", 8081)

    # 连接服务器
    file_socket.connect(server_address)

    # 输入文件名
    file_name = input("请输入要下载的文件:")

    while True:
        # 发送给服务器要下载的文件名
        file_socket.send(file_name.encode('utf-8'))

        # 接收最大为1M的文件
        receive_message = file_socket.recv(1024 * 1024)

    # 在本地写入接收到的文件
        try:
            with open("d" + file_name, "ab") as f: # a为追加模式
                f.write(receive_message)

        except:
            print("写入文件失败")

        # 判断最后两个符号是否为传输完成符号，如果是退出当前下载
        if (receive_message.decode('utf-8')[-1] == '^' and
                receive_message.decode('utf-8')[-2] == '^'):
            print('--[' + file_name + ']下载成功--')
            file_socket.close()
            break



if __name__ == '__main__':
    down_file()
