# -*- coding: utf-8 -*-

# if...elif...else

age = 3

if (age >= 18):
    print('adult')
elif (age >= 10):
    print('teenager')
else:
    print('kid')

# 循环Circulation

top5 = ['Russia', 'USA', 'China', 'UK', 'France']
for country in top5:
    print(country)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while (n > 0):
    sum = sum + n
    n = n - 2
print(sum)

birth = int(raw_input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')
