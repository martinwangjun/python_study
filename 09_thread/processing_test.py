#!/usr/bin/python
# -*- coding: utf-8 -*-

# 多进程
# 该程序可以在Windows下运行
from multiprocessing import Process
import os, time

# 要调用的多进程体
def run_proc(name):
    print('Run child process %s (%s), its parent process id = %s' % 
        (name, os.getpid(), os.getppid()))
    time.sleep(20)

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('ProcessName', ))
    print('Child process is going to start...')
    p.start()
    p.join()
    print('Child process end.')

# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))


# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('WhatTheFuck',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
