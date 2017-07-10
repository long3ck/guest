#coding=utf-8
__author__ = 'Chenkun'
__date__ = '2017/06/20 10:32'

import time

# 当前时间戳
now_time = time.time()
print('当前时间戳:'+str(now_time))
# 转换成日期格式
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time))
print('日期格式:'+str(otherStyleTime))