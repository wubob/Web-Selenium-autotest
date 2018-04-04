#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年1月30日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/DSWT V1/src/UserLogin.py        #用户登录测试

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
import csv

 
def LoginUser():
    csv_file=csv.reader(open("../confile/login.csv", 'r'))
    for values in csv_file:
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.maximize_window()
        driver.get("https://lb.dev.dataman.com:8443")
        time.sleep(1)
        driver.find_element_by_id("inputUsername").send_keys(values[0])
        time.sleep(1)
        driver.find_element_by_id("inputPassword").send_keys(values[1])
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/div[2]/button").click()
        time.sleep(1)
        if values[0]=="cluster_admin" and values[1]=="123":
           pass
           print("登录成功！")
        else:
           dd=driver.find_element_by_xpath("/html/body/div/div[1]/div/div/span[2]").text
           print("登录失败！"+dd)
        driver.quit()

if __name__ == '__main__':
     LoginUser()