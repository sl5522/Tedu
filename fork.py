import os
import time

print("======================")
a = 1

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    # time.sleep(3)
    print("The new process")
    print('a=', a)

    # time.sleep(1)
    print("The old process")
    print('a:', a)


print("fork test over")
print('all a=', a)


