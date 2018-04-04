#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年2月5日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/DSWT V1/public/AuthManage.py      #冒烟测试

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner

class DMOS(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(1)
        self.driver.get("https://lb.dev.dataman.com:8443")
        self.driver.maximize_window() 
    def test_DMOS(self):
        self.driver.find_element_by_id("inputUsername").send_keys("test_cluster_admin")
        time.sleep(1)
        self.driver.find_element_by_id("inputPassword").send_keys("LN0Dd97s4x39")
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/div[2]/button").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#user-dropdown > span.username.truncate.ng-binding").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div/default-header/nav/div/navbar-utility/ul/li[2]/ul/li[1]/a").click()       
        self.verificationErrors=1234
        self.assertEqual(1234, self.verificationErrors)
    
    def test_DMOS1(self):
        self.verificationErrors1=5678
        self.verificationErrors2=56783
        self.assertEqual(5678, self.verificationErrors1)
        self.assertEqual(56783, self.verificationErrors2)
        
    def tearDown(self):
        self.driver.quit()
      
if __name__ == '__main__':
    nowtime = "DMOS Smoke testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(DMOS("test_DMOS"))
    testunit.addTest(DMOS("test_DMOS1"))
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='DMOS冒烟测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    