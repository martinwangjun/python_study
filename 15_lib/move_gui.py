#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import pyautogui
# import time
# for i in range(3):
#     pyautogui.moveTo(100, 100, duration=1)
#     pyautogui.moveTo(200, 100, duration=1)
#     pyautogui.moveTo(200, 200, duration=1)
#     pyautogui.moveTo(100, 200, duration=1)
#     pyautogui.alert('这个消息弹窗是文字+OK按钮')

# print(pyautogui.position()[0])
# print(pyautogui.size())

# pyautogui.moveTo(
#     pyautogui.size()[0]//2,
#     pyautogui.size()[1]//2,
#     duration=0.1)
# pyautogui.click()

# pyautogui.FAILSAFE=True
# time.sleep(5)
# pyautogui.click()


# distance = 500
# DURATION = 0.001
# while distance > 0:
#     pyautogui.dragRel(distance, 0, duration=DURATION)
#     distance = distance - 5
#     pyautogui.dragRel(0, distance, duration=DURATION)
#     pyautogui.dragRel(-distance, 0, duration=DURATION)
#     distance = distance - 5
#     pyautogui.dragRel(0, -distance, duration=DURATION)


# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

import turtle, time
t = turtle.Pen()
t.color = "red"
for x in range(1, 201, 3):
    t.forward(x)
    t.left(90)
time.sleep(2)
