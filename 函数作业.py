"""
======================
Author: 柠檬班-小简
Time: 2020/6/6 13:47
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
1、定义函数：（要求：定义函数处理逻辑。input输入操作在函数之外。）
将用户输入的所有数字相乘之后对20取余数
用户输入的数字个数不确定

字符串：,
split: 列表。列表里的成员，就都是数字(类型：字符串)
20，30，100

sum = 1  # 累乘的过程 
for

（20*30*100）%20
"""


"""
定义一个函数 def remove_element(m_list):，
将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
定义一个新列表a：[]
遍历这个列表: 如果当前值，在a当中，就pass。如果不在a当中，就扔到a里面。
"""

"""
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖

input: 输入一个人的身高(m)和体重(kg)
结果：我的BMI值是多少？？
函数：根据体重和身高，给出对应的BMI。
def 名称(体重,身高):
    # 根据公式算出值。
    bmi = 体重 / 身高 ** 2 
    判断

"""

"""
通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作
，选择之后返回对应操作的值。

函数：数字1，数字2，运算符(1,2,3,4)。
"""
def caculator(num1,num2,cacul): # num2为0要排除
    pass




"""
一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。
编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，
询问10次后，输出满足条件的总人数
要求：定义函数处理逻辑。但是input输入操作在函数之外。在for循环当中，调用input和自己定义的函数)
"""
"""
join_team

team_numbs = 0

for index in range(10):
    询问用词的性别和年龄(input)
    # 根据性别和年龄，判断是否符合条件。---函数
    res = jion_team(int(age),sex)
    # 如果符合要求，加入球队。
    if res == True:
        team_numbs += 1

print(team_numbs)
"""

def join_team(age,sex):
    if 15 <= age <= 22 and sex == "f":
        return True
    else:
        return False

