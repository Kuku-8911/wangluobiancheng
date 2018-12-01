#!/usr/bin/env.python
#._*_ coding:utf-8 _*_
import socket

def tcp_receive():

    #  socket.SOCK_STREAM为tcp协议
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.bind(("", 8081))

    tcp_socket.listen(128) #  设置为接收模式，必须有

    #  等待连接，如果有客服端连接，返回包含两个值的元组一个新的socket用来专门服务该客户端，以及该客户端地址
    new_socket, address = tcp_socket.accept()

    message = new_socket.recv(1024) #  用新socket接收信息
    message = message.decode('utf-8') #  信息解码

    new_socket.send("received".encode('utf-8')) # 返回一些信息

    print(message)

if __name__ == '__main__':
    tcp_receive()