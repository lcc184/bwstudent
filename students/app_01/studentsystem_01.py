import os
import re
from students.app_01 import app_1
# filename = str(r"D:\python_基础\新建文件夹\bwstudent\app_01\students.txt")

@app_1.route("/")
def main():
    ctrl = True # 标记是否退出系统
    while (ctrl):
        menu() # 显示菜单
        option = input("请选择：") #选择菜单项
        option_str = re.sub("\D","",option) # 提取数字
        if option_str in ["0","1","2","3","4","5","6","7",]:
            option_int = int(option_str)
            if option_int==0:# 退出系统
                print("您已退出学生信息系统！")
                ctrl = False
            elif option_int == 1:#  录入学生信息成绩
                insert()
            elif option_int == 2:#  查找学生信息成绩
                search()
            elif option_int == 3:#  删除学生信息成绩
                delete()
            elif option_int == 4:#  修改学生信息成绩
                modify()
            elif option_int == 5:#  排序学生信息成绩
                sort()
            elif option_int == 6:#  统计学生信息成绩
                total()
            elif option_int == 7:#  显示学生信息成绩
                show()



# 输出菜单
def menu():

    print("""
    ┏-------- 学生信息管理系统 ----------┓
    |                                    |
    |   ******** 功能菜单 ********        |
    |   1. 录入学生信息                   |
    |   2. 查找学生信息                   |
    |   3. 删除学生信息                   |
    |   4. 修改学生信息                   |
    |   5. 排序                          |
    |   6. 统计学生总人数                 |
    |   7. 显示所有学生信息               |
    |   8. 退出系统                      |
    |   *************************       |
    |   说明: 通过数字或↑↓方向键选择菜单   |
    ┗-----------------------------------┛

""")

#将学生信息保存到文件
def save(student):
    try:
        students_txt = open(filename, "a")# 以追加模式打开

    except Exception as e:
        students_txt = open(filename, "w") # 如果文件不存在，创建文件并打开

    for info in student:
        students_txt.write(str(info) + "\n") # 按行存储，添加换行符
    students_txt.close() # 关闭文件

# 录入学生信息
def insert():
    stdentList = []# 保存学生信息列表
    mark = True# 是否继续添加
    while mark:
        id = input("请输入ID (如 1001): ")
        if not id:#ID不能为空
            break
        name = input("请输入名字: ")# 名字不能为空
        if not name:
            break
        try:
            english = int(input("请输入英文成绩: "))
            python = int(input("请输入Python成绩: "))
            c = int(input("请输入C语言成绩: "))
        except:
            print("输入无效,不是整型数值.. 请重新录入信息")
            continue
        # 将输入的学生信息保存到字典
        stdent = {"id": id, "name": name, "english": english, "python": python, "c": c}
        stdentList.append(stdent)# 将学生字典添加到列表中
        inputMark = input("是否继续添加? (y/n) :")
        if inputMark == "y":# 是否继续添加
            mark = True
        else:# 不继续添加
            mark = False
    save(stdentList)# 将学生信息保存到文件
    print("学生信息录入完毕!!!")

# 查找学生信息
def search():
    mark = True
    students_query = [] # b保存查询结果的数据列表
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename): # 判断文件是否存在
            mode = input("按ID查输入1；按姓名查输入2：")
            if mode=="1": # 按学生编号查询
                id = input("请输入学生ID：")
            elif mode=="2": # 按学生姓名查询
                name = input("请输入学生姓名：")
            else:
                print("您输入有误，请重新输入！")
                search()# 重新查询  // 用的递归
            with open(filename,"r") as file: # 打开文件
                student = file.readlines() # 读取全部内容
                for list in student:
                    d = dict(eval(list))# 字符串转化成字典
                    if id is not "":
                        if d["id"]==id:
                            students_query.append(d)
                    elif name is not "":
                        if d["name"]==name:
                            students_query.append(d)
                print("{:^6}{:^12}\t{:12}\t{:12}\t{:12}\t{:12}".format("id", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
                for i in students_query:
                    print("{:^6}{:^12}\t{:11}\t{:12}\t{:12}\t{:12}".format(i.get("id"),i.get("name"),i.get("english"),i.get("python"),i.get("c"),int(i.get("english"))+int(i.get("python"))+int(i.get("c"))))
                students_query.clear()
                inputMark = input("是否继续查询？（y/n）：")
                if inputMark=="y":
                    mark=True
                else:
                    mark=False



        else:
            print("暂未保存数据信息---------")
            return

# 删除学生信息
def delete():
    pass

# 修改学生信息
def modify():
    pass

# 排序学生信息
def sort():
    pass

# 统计学生信息
def total():
    pass

# 显示学生信息
def show():
    pass

#


if __name__ == '__main__':
    main()