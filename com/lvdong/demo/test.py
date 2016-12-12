# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 学习测试使用
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('''this
is
a
test
case''')

if True:
    print("true")

print('\n')

print(True and False)
print(True and True)
print("中文，你好！")

print('\n')

list = ['a', 'b', 'c', 'd']
print(list)
list.insert(2, 'three')
print(list)
list.append('e')
print(list)
list.pop(-1)
print(list)
list[1] = 'one'
print(list)
list.insert(1, [1, 2, 3, 4, 5])
print(list)

print('\n')

t = (1,)
print(len(t))
print(t)

print('\n')
# input = input("input your birth year : ")
input = 2001
birth = int(input)
if birth >= 2000:
    print('you are a 00 child!')
else:
    print('hello,old man!')

print('\n')


def func1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def func2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


func1(1, 2)
func1(1, 2, c=3)
func1(1, 2, 3, 'a', 'b')
func1(1, 2, 3, 'a', 'b', x=99)
func1(1, 2, d=99, ext=None)

print('\n')

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '###'}
func1(*args, **kw)

print('\n')
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
func2(*args, **kw)

print('\n')


def func3(n):
    if n == 1:
        return 1
    return n * func3(n - 1)


print(func3(5))

print(func3(100))


def func5(n, result):
    if n == 1:
        return result
    return func5(n - 1, n * result)


def func4(n):
    return func5(n, 1)


print('\n')
print(func4(5))
