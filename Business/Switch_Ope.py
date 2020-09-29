# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 23:38
# @Author  : Liangxiaohui
# @FileName: Switch_Ope.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/youngleesin
from Base.Base import Base
import Page.setingMainPage
#import Page


class Switch_Ope(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)  # 子类继承父类，拥有父类的所有变量

    def click_tab(self):
        self.click_element(Page.setingMainPage.all_xpath)

    def check_WLANSwitch(self):
        status = self.get_switchs(Page.setingMainPage.switch_id, 0)
        return status

    def check_BlueSwitch(self):
        status = self.get_switchs(Page.setingMainPage.switch_id, 1)
        return status
