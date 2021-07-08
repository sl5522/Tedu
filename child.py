import os
from time import sleep


def f1():
    sleep(2)
    print("fun1")


efefefefeffefe


pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    pid_0 = os.fork()  # 二级的子进程
    if pid_0 == 0:
        f1()  # 二级子进程执行
    else:
        os._exit(0)
else:
    os.wait()
    f2()
eeeeeeee
