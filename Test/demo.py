# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 7:58
# @Author  : Liangxiaohui
# @FileName: demo.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/youngleesin

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

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

# desired_caps['automationName'] = 'uiautomator2'
# 声明我们的driver对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#driver.find_element_by_xpath("//*[contains(@text,'全部')]").click()
WebDriverWait(driver,10,0.5,None).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'全部')]")).click()
status=driver.find_element_by_id("com.android.settings:id/switchWidget").get_attribute("checked")
print("status:",status)
