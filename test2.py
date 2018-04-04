#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年2月6日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/DSWT V1/src/test2.py

'''
from time import sleep, ctime
import threading

# def music():
#     print('I was listening to music! %s' %ctime())
#     sleep(2)
# def move():
#     print('I was at the movies! %s' %ctime())
#     sleep(5)
#     
# if __name__ == '__main__':
#     music()
#     move()
# print('all end:', ctime())

# def muisc(func):
#     for i in range(2):
#         print('I was listening to %s! %s' %(func,ctime()))
#         sleep(2)
# #视频播放器
# def move(func):
#     for i in range(2):
#         print('I was at the %s! %s' %(func,ctime()))
#         sleep(5)
# if __name__ == '__main__':
#     muisc(u'爱情买卖')
#     move(u'阿凡达')
#     print('all end:', ctime())
#
# num=111 
# t=num / 2
#  
# while t>0:
#     if num % t ==0:
#         print("num=",num)
#         break
#     t-=1
# 
# print("jieshule")
#     

def tax(cost,rate=0.08):
    print("执行结果",cost +(cost*rate))


if __name__ == '__main__':
    tax(100)
    tax(100,0.05)


    
    