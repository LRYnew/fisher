# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 0024 16:46
# @Author  : YJob
import threading

import time
from werkzeug.local import Local

# 普通类 没有做到线程隔离
class A:
    b = 1

new_a = A()
new_local = Local()
new_local.b = 1

def work():
    new_a.b = 2
    print('i am thread new_a.b:' + str(new_a.b))


def work1():
    new_local.b = 2
    print('i am thread new_local.b:' + str(new_local.b))


new_t1 = threading.Thread(target=work)
new_t1.start()

new_t2 = threading.Thread(target=work1)
new_t2.start()

time.sleep(1)

# 没有线程隔离，new_a.b 受另一教程影响 new.b = 2
print('i am thread new_a.b:' + str(new_a.b))
print('i am thread new_local.b:' + str(new_local.b))
