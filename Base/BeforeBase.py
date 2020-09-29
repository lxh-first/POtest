# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 9:33
# @Author  : Liangxiaohui
# @FileName: BeforeBase.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/youngleesin
from appium import webdriver
from selenium.webdriver.common.by import By
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'ZTE B2015_7077'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.Settings'
# 中文输入允许
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

desired_caps['noReset'] = 'True'

# desired_caps['automationName'] = 'uiautomator2'
# 声明我们的driver对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.find_element_by_id("com.android.settings:id/switchWidget")
driver.find_element_by_xpath("//*[contains(@text,'全部')]")#封装了return self.find_element(by=By.XPATH, value=xpath)
#举例:
def getElem(by,value):
    if by=="ID":
        driver.find_element_by_id(value)
    if by=="XPATH":
        driver.find_element_by_xpath(value)
    sb={"ID","com.android.settings:id/switchWidget"}
    #sb.get("ID")
