# encoding: utf-8

"""

@Author: yedeguo
@File: main.py                                                               
@Time: 2017/9/12 下午6:10                                   
@Description: 

"""

from scrapy.cmdline import execute
import sys
import os

# 打断点调试py文件
# sys.path.append('D:\PyCharm\py_scrapyjobbole')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'tencent'])
