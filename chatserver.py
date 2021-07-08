"""
chat room
env:python
socket udp & fork
"""

from socket import *
import os, sys

# 服务器地址
ADDR = ('0.0.0.0', 8888)

# 存储用户信息{name:address}
user = {}


# 登录操作
def do_login(s, name, addr):
    if name in user or '管理员' in name:
        s.sendto('该用户存在'.encode(), addr)
        return
    s.sendto(b'OK', addr)
    # 通知其他人
    msg = "\n欢迎 %s 进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr


# 聊天处理
def do_chat(s, name, text):
    msg = "\n%s:%s" % (name, text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])


# 退出处理
def do_quit(s, name):
    msg = "\n%s退出聊天室" % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'EXIT', user[i])  # 让其本人退出


# 不断的接收客户端请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        tmp = data.decode().split(' ', 2)
        # tmp-->['L',]
        if tmp[0] == 'L':
            do_login(s, tmp[1], addr)
        elif tmp[0] == 'C':
            do_chat(s, tmp[1], tmp[2])
        elif tmp[0] == 'Q':
            do_quit(s, tmp[1])


# 网络搭建
def main():
    # udp服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid == 0:
        while True:
            msg = input("管理员消息：")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(), ADDR)
    else:
        do_request(s)


if __name__ == '__main__':
    main()
