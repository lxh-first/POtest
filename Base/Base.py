# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 23:09
# @Author  : Liangxiaohui
# @FileName: Base.py
# @Software: UITest
# @Cnblogs ：https://www.cnblogs.com/youngleesin

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        '''
        #初始化
        :param driver:
        '''
        self.driver = driver

    def get_element(self, loc, timeout=10, freq=0.5,ignored_exception=None):
        '''
        #定位一个元素
        :param loc: 元组类型，定位元素时的定位方法和属性值，类似(By.ID,"id属性值") （By.XPATH,"xpath语句"） 使用*loc来进行解包
        :param timeout: 查找定位元素时的超时时间，即等待的最长时间（包括隐性等待的时间）
        :param freq:调用until或者until not方法的间隔时间，默认为0.5s
        :param ignored_exceptions:超时后抛出的异常；默认是NoSuchElementException；但可以作为忽略的异常，如果在调用until或until_not的过程中抛出这个元组中的异常，则不中断代码，继续等待，
                                  如果抛出的是这个元组外的异常，则中断代码，抛出异常。
        :return:返回找到的定位元素
        '''
        return WebDriverWait(self.driver, timeout, freq,ignored_exception).until(
            lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=10, freq=0.5, ignored_exception=None):
        '''
        #定位多个元素
        :param loc: 元组类型，定位元素时的定位方法和属性值，类似(By.ID,"id属性值") （By.XPATH,"xpath语句"） 使用*loc来进行解包
        :param timeout: 查找定位元素时的超时时间，即等待的最长时间（包括隐性等待的时间）
        :param freq: 调用until或者until not方法的间隔时间，默认为0.5s
        :param ignored_exception: 超时后抛出的异常；默认是NoSuchElementException；但可以作为忽略的异常，如果在调用until或until_not的过程中抛出这个元组中的异常，则不中断代码，继续等待，
                                  如果抛出的是这个元组外的异常，则中断代码，抛出异常。
        :return: 返回找到的定位元素
        '''
        return WebDriverWait(self.driver,timeout, freq, ignored_exception).until(
            lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        '''
        #点击元素
        :param loc:定位元素时的定位方法和属性值，类似(By.ID,"id属性值") （By.XPATH,"xpath语句"）
        :return:
        '''
        self.get_element(loc).click()

    def get_switch(self, loc):
        '''
        #读取单个元素的开关状态
        :param loc:定位元素时的定位方法和属性值，类似(By.ID,"id属性值") （By.XPATH,"xpath语句"）
        :return:返回单个元素的开关状态 True：打开  False：关闭
        '''
        return self.get_element(loc).get_attribute("checked")

    def get_switchs(self, loc, index):
        '''
        #读取多个元素的开关状态
        :param loc: 元组类型，定位元素时的定位方法和属性值，类似(By.ID,"id属性值") （By.XPATH,"xpath语句"）
        :param index: 索引序列从0开始
        :return: 返回多个元素的开关状态 True：打开 False：关闭
        '''
        elements = self.get_elements(loc)
        if (index < len(elements)):
            return elements[index].get_attribute("checked")
