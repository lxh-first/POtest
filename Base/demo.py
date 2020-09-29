# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 9:55
# @Author  : Liangxiaohui
# @FileName: demo.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/youngleesin
#传字典方式：
sb1={type:"ID","value":"com.android.settings:id/switchWidget"}
#print(sb1.get(type))
#print(sb1.get("value"))
#传元组方式
sb2=("ID","com.android.settings:id/switchWidget")
#单个字典
sb3={"ID":"com.android.settings:id/switchWidget"}
def test(name,pwd):
    print(name)
    print(pwd)
if __name__ == '__main__':
    #test(sb2)#该种情况只传了元组的第一个值，但test是两个参数
    #test(*sb2)#使用*将元组进行解包，则为两个参数
    #test(sb1)#该种情况只传了字典的第一个值，但test是两个参数
    test(**sb3)#遗留问题：字典解包使用方式有问题：

