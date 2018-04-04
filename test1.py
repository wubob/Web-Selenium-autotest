#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年2月5日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/DSWT V1/public/UserGroup.py  #用户组测试。

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import random
import itertools

driver = webdriver.Chrome()
time.sleep(1)
driver.get("https://lb.dev.dataman.com:8443")
driver.maximize_window()
time.sleep(1)
 
def ClusterUser():
    driver.find_element_by_id("inputUsername").send_keys("cluster_admin")
    time.sleep(1)
    driver.find_element_by_id("inputPassword").send_keys("123")
    driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/div[2]/button").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#user-dropdown > span.username.truncate.ng-binding").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/default-header/nav/div/navbar-utility/ul/li[2]/ul/li[1]/a").click()
    time.sleep(1)
    ShouPage()

       
def ShouPage():
    count=1
    for strkey in map(lambda x : x[0]+x[1]+x[2]+x[3]+x[4], itertools.product('abcdefghijklmnopqrstuvwxyz', repeat = 5)):
        count=count+1
        driver.find_element_by_xpath('''//*[@id="app"]/div/section/ul/div/li[1]/span''').click()
        time.sleep(1)
        driver.find_element_by_xpath('''//*[@id="app"]/div/section/ul/div/li[2]/div/span''').click()
        time.sleep(1)
        driver.find_element_by_xpath('''//*[@id="app"]/div/section/ul/div/li[2]/ul/div[2]/li/span''').click()
        time.sleep(2)
        driver.find_element_by_xpath('''//*[@id="app"]/div/section/section/div/div[1]/div/div[2]/div/button/span''').click()
        time.sleep(1)  
        driver.find_element_by_xpath('''//*[@id="app"]/div/section/section/div/form/div[1]/div/div/div/div[1]/input''').click()
        time.sleep(1)
#         driver.find_element_by_xpath('''//*[@id="app"]/div/section/section/div/form/div[1]/div/div/div/div[1]/input''').send_keys(random.randrange(1000000000,9999999999,2))
#         for strkey in map(lambda x : x[0]+x[1]+x[2]+x[3]+x[4], itertools.product('abcdefghijklmnopqrstuvwxyz', repeat = 5)):
        driver.find_element_by_xpath('''//*[@id="app"]/div/section/section/div/form/div[1]/div/div/div/div[1]/input''').send_keys(strkey)
        time.sleep(2)
        driver.find_element_by_xpath('''//*[@id="app"]/div/section/section/div/form/div[3]/div/button[1]/span''').click()
        time.sleep(3)
        f = open("D:\count.txt",'w+')
        f.write("执行"+str(count)+"次")
        f.close()
              
if __name__ == '__main__':
    ClusterUser()