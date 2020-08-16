'''

"""# 使用if~编写程序~实现以下功能
"""
从键盘获取用户名、密码
如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎进入xxx的世界”，
否则提示密码或者用户名错误
"""
username = input("请输入用户名：")# 用户名
pwd = input("请输入密码：")# 密码
# 检验不能为空
if username and pwd:
    # 判断用户名，密码是否正确
    if username=="lcc" and pwd=="123":
        print("欢迎进入xxx的世界")

    else:
        print("密码或者用户名错误")
else:
    print("不能为空")

"""
使用while，完成以下图形的输出
"""

i = 1
while i<=5:
    a = i * "*"
    print(a)
    i +=1
i = 1
while i<=4:
    a = 5
    a-=i
    print(a*"*")
    i+=1
'''
"""
strs = "i love beijing"
kg = ""
print(strs.capitalize())#首字母大写
print(strs.title())#每个首字母大写
print(strs.lower())#全小写
print(strs.upper())#全大写
print(strs.startswith("i"))#判断开头
print(strs.endswith("beijing"))#全大写
up_strs = strs.partition("love")
print(up_strs)#切成三部分
str_kg = kg.join(up_strs)
print(str_kg)#将元组转换成字符串
print(strs.splitlines())# 将字符串转化成列表
strs_nt = "\n\t I love you\t\n"
strip_strs = strs_nt.strip()#去空格字符
print(strip_strs)
"""

def month_day(month,day):
    month=int(month)
    day= input((day))

    return month,day

print(month_day(4,2))