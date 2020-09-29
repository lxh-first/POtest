# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 0:03
# @Author  : Liangxiaohui
# @FileName: test_switch.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/youngleesin
import sys, os
sys.path.append(os.getcwd())

from appium import webdriver
from Business.Switch_Ope import Switch_Ope
import pytest


class Test_switch:
    '''
    测试各开关状态
    Attributes:
        desired_caps 存储设备信息
    '''
    def setup(self):
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
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.obj = Switch_Ope(self.driver)

    #@pytest.fixture()
    '''def clickAll(self):
        print("进入到全部设置界面")
        self.obj.click_tab()'''

    @pytest.mark.run(order=5)
    def test_WLANSwitch(self):
        #self.obj.click_tab()
        status = self.obj.check_WLANSwitch()
        print("WLANstatus:",status)
        assert status, "判断Wifi开关状态是打开的，当前wifi状态是：%s" % status

    @pytest.mark.run(order=3)
    def test_BlueSwitch(self):
        self.obj.click_tab()
        status = self.obj.check_BlueSwitch()
        print("Bluestatus:",status)
        assert status, "判断Blue开关状态是打开的，当前状态是：%s" % status

    def teardown(self):
        self.driver.quit()

help(Test_switch)