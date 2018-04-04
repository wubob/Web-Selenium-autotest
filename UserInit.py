#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年1月30日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/DSWT V1/src/UserLogin.py         # test1 ~ test100用户初始化。

'''
from selenium import webdriver
import chromedriver_binary
import time
import csv

 
def InitUser():
    csv_file=csv.reader(open("../confile/user.csv", 'r'))
    #dmosurl="https://lb.dev.dataman.com:8443"                                      #测试环境
    #dmosurl="https://origin-dm-web.master1.dev.dataman.com:9443/"                   #测试环境
    dmosurl="https://origin-dm-web.master237.openshift.dataman:9443"                #开发环境
    for values in csv_file:
        driver = webdriver.Chrome()
        driver.get(dmosurl)
        time.sleep(1)
        driver.find_element_by_id("inputUsername").send_keys(values[0])
        time.sleep(1)
        driver.find_element_by_id("inputPassword").send_keys(values[1])
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/div[2]/button").click()
        time.sleep(1)
        driver.quit() 
 
if __name__ == '__main__':
    InitUser().main()
    
    
    