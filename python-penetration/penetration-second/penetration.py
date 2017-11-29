# -*- coding: utf-8 -*-
import hashlib
import re

import requests
from threading import Thread
import sys
import getopt

import time
from selenium import webdriver

#程序标识
def banner():
    print("\n*********************************************************")
    name='''
   ___      ___
   \  \    /  /
    \  \  /  /   _
     \__\/__/   (_)
       |  |      __
       |  |     |  |
       |__|     |__|
    '''
    print(name)
    print("渗透测试暴力发掘器2.0")
    print("**********************************************************")
    usage = '''
使用方法：
        -u:网址url
        -t:线程数
        -d:字典文件
        -h:不需要显示的网页状态码
例：python penetration.py -u http://www.scruffybank.com/YY -t 5 -d test.txt -h 404
默认参数为：-u:http://www.scruffybank.com/YY，-t：5，-d：test.txt -h 404
    '''
    print(usage)

#创建线程并向目标站点发起请求以及获取响应
class request_performer(Thread):
    def __init__(self,word,url,code):
        Thread.__init__(self)
        try:
            self.word = word.split('\n')[0]
            self.new_url = url.replace("YY",self.word)
            self.url = self.new_url
            self.hidecode = code
        except Exception as e:
            print(e)

    def run(self):
        try:
            r = requests.get(self.url)
            #网页行数
            lines = str(r.text.count("\n"))#text返回的是Unicode型
            #网页字符数
            charators = str(len(r.text))
            #网页单词数
            words = str(len(re.findall(r"\S+",r.text)))
            #哈希值
            hashs = str(hashlib.md5(r.content).hexdigest())#hashlib中含有很多加密函数，hexdigest是拿到加密字符串
            #状态码
            scode = str(r.status_code)
            if scode!=str(self.hidecode):
                if '200'<=scode<'300':
                    driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs.exe")
                    driver.get(self.url)
                    time.sleep(3)
                    driver.set_window_size(1024,768)#设置要截屏的大小
                    driver.save_screenshot(self.word+".png")
                    #绿色
                    print("\033[0;32m%s\033[0m" % scode+"\t"+charators+"\t"+lines+"\t"+words+"\t"+hashs+"\t"+self.url)
                elif '300'<=scode<'400':#蓝色
                    print("\033[0;34m%s\033[0m"  % scode,
                          + "\t" + charators + "\t" + lines + "\t" + words + "\t" + hashs + "\t" + self.url)
                elif '400'<=scode<'500':#红色
                    print("\033[0;31m%s\033[0m"  % scode,
                          + "\t" + charators + "\t" + lines + "\t" + words + "\t" + hashs + "\t" + self.url)
                else:#黄色
                    print("\033[0;33m%s\033[0m"  % scode
                          + "\t" + charators + "\t" + lines + "\t" + words + "\t" + hashs + "\t" + self.url)
           # print(self.url, "-", str(r.status_code))#打印url及其状态码
            i[0] = i[0]-1
        except Exception as e:
            print(e)

#遍历字典中的关键字组合成url生成新的进程
def launcher_thread(names,th,url,code):
    global i#执行的线程数
    i = []
    i.append(0)
    while len(names):
        try:
            if i[0]<int(th):
                first = names.pop(0)#取出names列表第一个值
                i[0] = i[0]+1
                thread = request_performer(first,url,code)
                thread.start()
        except KeyboardInterrupt:
            print("用户停止运行，已完成探测!")
            sys.exit()
    return True

#接收命令行中的参数将其传递给launcher_thread()函数
def get_cmd():
    config = {
        "url":'http://zmister.com/YY',
        "threads":"5",
        "dicts":"test.txt",
        "hidecode":"404"
    }
    banner()
    try:
        opts,args = getopt.getopt(sys.argv[1:],"u:t:d:h:",['url=','threads=','dicts=','hidecode='])
    except getopt.GetoptError:
        print("错误的参数")
        sys.exit()

    for opt, arg in opts:
        if opt == '-u':
            config['url'] = arg
        elif opt == '-t':
            config['threads'] = int(arg)
        elif opt == '-d':
            config['dicts'] = arg
        elif opt == '-h':
            config['hidecode'] = arg
    try:
        f = open(config['dicts'],"r")
        words = f.readlines()#逐行读取文件内容，words是列表
    except Exception as e:
        print("文件打开错误！")
        print(e)
        sys.exit()
    print("==================================================")
    print("状态码" + "\t" + "字符数" + "\t" + "行数" + "\t" + "单词数" + "\t" + "哈希值" + "\t" + "网址")
    print("==================================================")
    launcher_thread(words, config['threads'], config['url'],config['hidecode'])

get_cmd()