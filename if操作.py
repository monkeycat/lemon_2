"""
======================
Author: 柠檬班-小简
Time: 2020/5/25 21:33
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

score = input("本次考试成绩分数为:")
# 判断  如果为100分，一个么么哒！
#        如果大于60分，就及格！
# 对齐  换行  缩进
"""
看到冒号自动缩进。
if 条件1:
    条件1为真时，执行的代码。
    
    
if 条件1:
    条件1为真时，执行的代码。
else:
    条件1不满足的时候，执行的代码。干的事情。

   
if 条件1:
    条件1为真时，执行的代码。
elif 条件2：
    条件2为真时，执行的代码
elif 条件3：
    条件3为真时，执行的代码
else:
    条件1不满足的时候，执行的代码。干的事情。
"""
if int(score) == 100:
    print("一个么么哒！")
    print("干的漂亮！！")


if int(score) > 60:
    print("及格！")
else:
    print("通宵敲代码！")


# 你想在哪里让程序中断执行，由你自己来控制它的执行

if 85 <= int(score) <= 100:
    print("A")
elif 75 <= int(score) < 85:
    print("B")
elif 60 <= int(score) < 75:
    print("C")
else:
    print("D")



print("11111111")
