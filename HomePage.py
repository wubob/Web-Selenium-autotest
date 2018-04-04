#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年2月5日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/DSWT V1/public/ClusterAdmin.py     #用户首页

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox

driver = webdriver.Chrome()
time.sleep(1)
driver.get("https://lb.dev.dataman.com:8443")
driver.maximize_window()
time.sleep(1)
 
def ClusterUser():
    driver.find_element_by_id("inputUsername").send_keys("test_cluster_admin")
    time.sleep(1)
    driver.find_element_by_id("inputPassword").send_keys("LN0Dd97s4x39")
    driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/div[2]/button").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#user-dropdown > span.username.truncate.ng-binding").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/default-header/nav/div/navbar-utility/ul/li[2]/ul/li[1]/a").click()
    time.sleep(1)
    result=messagebox.askokcancel("登录", "登录测试OK.")
    if result==True:
        ShouPage()
    else:
        driver.quit() 
       
def ShouPage():
    driver.find_element_by_xpath('''//*[@id="app"]/div/section/ul/div/li[1]/span''').click()
    time.sleep(1)
    text=driver.find_element_by_class_name("welcome").text    
    if text=="欢迎登录 DMOS 集群管理端":
        messagebox.askokcancel("首页", "首页测试OK.")
        driver.find_element_by_css_selector("#app > div > ul > div > div.el-col.el-col-2 > div > div > span").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/ul/li[3]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/a").click()
        messagebox.askokcancel("首页", "首页测试结束.")   
    else:
        messagebox.askokcancel("首页", "首页测试失败.")
   
if __name__ == '__main__':
    ClusterUser()