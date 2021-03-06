"""
======================
Author: 柠檬班-小简
Time: 2020/6/3 21:42
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

# dicta = {"name":"111"}
# print(dicta["key"])
"""

1、先翻译报错
2、找到自己写的代码当中的，第几行出错了。

文件处理：文件不存在/路径不存在

捕获异常！！
在程序当中，抓到这个异常，可以加上我们自己额外的代码处理。然后再抛出异常。

我怎么知道哪一行要出错？
我怎么知道，我要捕获什么异常？

与第三方资源交互的时候，一定要处理异常。
资源释放的问题。--- http连接/数据库连接/excel操作
try:
    可能会出错的代码
except:(如果出错了，进入except)
    逮到异常。
    代码报错之后会执行的代码。
[else:
    try里面代码没报错的时候，会执行的代码。
finally:
    无论是否出现异常，一定会执行的代码。
]


如果你捕获到了异常，并且做了你想做的事情。然后再抛出这个异常给到：
raise
"""
# 如果文件打开成功，则接着写入数据。
# try:
#     fs = open(r"D:\Pychram-Workspace\py30\python练习.txt","r",encoding="utf-8")
#     # fs.write("成功写入")
# except:  # 捕获异常
#     print("代码出错了！！")  # 我做了我自己的事情。输出了一些内容。
#     raise  # 会把异常信息抛出。让python接收到
# else:
#     fs.write("成功写入")
# finally:
#     print("一定会执行的代码！！")
#     try:
#         fs.close()  # 清理收尾工作。无论成功还是失败都会执行的代码。
#     except:
#         pass  # 如果fs.close()失败了，不用处理。直接忽略异常。


fs = open(r"D:\Pychram-Workspace\py30\python练习.txt","r",encoding="utf-8")

# 1、使用外部资源，需要做清理工作。
# 2、你想捕获到异常，在异常情况下，做一些自己的处理。

# 模块引入： 相对于项目目录引入。 from 包 import 模块
# 路径处理：os模块。获取绝对路径。__file__   os.path.abspath(__file__)
#                获取所在的目录   os.path.dirname(绝对路径)
#                路径拼接   os.path.join(路径1,文件名)  --最终是个绝对路径。
# # 异常处理： try:
#                 可能会出现异常的代码
#            except:
#                   try里的代码有异常，则会执行此处的代码
#                   raise
#            [else:
#                     try里的代码没出现异常，则执行此处代码
#            finally:
#                    无论try里的代码有没有出异常，必定会执行的操作。
#                    一般来讲，清理工作。]


