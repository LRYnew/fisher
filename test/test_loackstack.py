# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 0025 11:40
# @Author  : YJob
import threading

import time
from werkzeug.local import LocalStack

s = LocalStack()
s.push(1)

print('主线程 推入栈后取值:' + str(s.top))

def work():
    # 新线程因线程隔离，栈内的值并不相同，所以 推入前取值不会是 1，而是None
    print('新线程 推入栈前取值:' + str(s.top))
    s.push(2)
    print('新线程 推入栈后取值:' + str(s.top))

new_t = threading.Thread(target=work)
new_t.start()

time.sleep(1)
print('主线程 最后取值:' + str(s.top))
