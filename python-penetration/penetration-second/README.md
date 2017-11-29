### Python渗透测试器2.0

##### 1.程序功能

- 对某些web站点进行资源探测，对某些网页进行截图
- 使用selenium和phantomJS

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

- 添加打印

```python
==================================================
状态码	字符数	行数	单词数	哈希值	网址
==================================================
```

- selenium+phantomJS的使用

  ```python
  from selenium import webdriver

  driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs.exe")
  driver.get("http://zmister.com")
  driver.save_screenshot("zmister.com.png")#保存截图
  ```

3.结果展示

##### ![pene2](/python-penetration/screenshots/pene2.PNG)

![pene3](/python-penetration/screenshots/pene3.PNG)

![admin](/python-penetration/screenshots/admin.png)