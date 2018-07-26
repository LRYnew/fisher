# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 0024 09:56
# @Author  : YJob
import threading

import time


def work():
    print('I an thread')
    t = threading.current_thread()
    time.sleep(10)
    print(t.getName())

new_t = threading.Thread(target=work, name='work_thread')
new_t.start()
# work() 直接调用 主线程会停滞10s后再运行
# 多线程 -> 为了充分利用CPU的性能优势

print('I am YJob')
t = threading.current_thread()
print(t.getName())


