# -*- coding: utf-8 -*-
import requests
from threading import Thread
import sys
import getopt

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
    print("渗透测试暴力发掘器1.0")
    print("**********************************************************")
    usage = '''
使用方法：
        -u:网址url
        -t:线程数
        -d:字典文件
例：python penetration.py -u http://www.scruffybank.com/YY -t 5 -d php.txt
默认-u参数为：http://zmister.com/YY，-t：5，-d：test.txt
    '''
    print(usage)

#创建线程并向目标站点发起请求以及获取响应
class request_performer(Thread):
    def __init__(self,word,url):
        Thread.__init__(self)
        try:
            self.word = word.split('\n')[0]
            self.new_url = url.replace("YY",self.word)
            self.url = self.new_url
        except Exception as e:
            print(e)

    def run(self):
        try:
            r = requests.get(self.url)
            print(self.url, "-", str(r.status_code))#打印url及其状态码
            i[0] = i[0]-1
        except Exception as e:
            print(e)

#遍历字典中的关键字组合成url生成新的进程
def launcher_thread(names,th,url):
    global i#执行的线程数
    i = []
    i.append(0)
    while len(names):
        try:
            if i[0]<int(th):
                first = names.pop(0)#取出names列表第一个值
                i[0] = i[0]+1
                thread = request_performer(first,url)
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
        "dicts":"test.txt"
    }
    banner()
    try:
        opts,args = getopt.getopt(sys.argv[1:],"u:t:d:",['url=','threads=','dicts='])
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
    try:
        f = open(config['dicts'],"r")
        words = f.readlines()#逐行读取文件内容，words是列表
    except Exception as e:
        print("文件打开错误！")
        print(e)
        sys.exit()
    launcher_thread(words, config['threads'], config['url'])

get_cmd()