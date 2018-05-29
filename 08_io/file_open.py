#!/usr/bin/env python8
# -*- coding: utf-8 -*-

# f = open('somefile.txt', 'w', encoding='utf-8')
# f.write('你在不经意间看见过什么不该看见的东西或者事情？')
# f.close()

# with open('somefile.txt', 'w', encoding='utf-8') as f:
#     num = f.write('你在不经意间看见过什么不该看见的东西或者事情？')
#     print(num)


# 读写文件
with open('somefile.txt', 'a+', encoding='utf-8') as f:
    # num = f.write('贵州现在天天都是发展大数据')
    # print(num)
    text = f.read()
    print(text)
    f.write('你在不经意间看见过什么不该看见的东西或者事情？')

