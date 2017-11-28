### 使用Python编写一个渗透测试器

##### 1.程序功能

​	对某些web站点进行资源探测

##### 2.程序主要函数

```python
#程序标识
def banner()
#创建线程并向目标站点发起请求以及获取响应
class request_performer(Thread):
  def __init__(self,word,url):#构造目标url
  def run(self):#发起请求并获得响应
#遍历字典中的关键字组合成url生成新的进程
def launcher_thread(names,th,url):
 #接收命令行中的参数将其传递给launcher_thread()函数
def get_cmd():
```

##### 3.程序运行效果

命令输入：

```
python penetration.py -u http://www.scruffybank.com/ -t 5 -d php.txt
```

截图：

![pene1](/python-penetration/screenshots/pene1.PNG)
