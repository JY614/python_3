'''
定义一个学生类，用来形容学生

'''
#定义一个空的类
class Student():
    pass  #pass 代表一个空的类，先空着，此处必须由

# 定义一个对象
wangdachui = Student()

# 再定义一个类，用来描述听python的学生
class Python_Student():
    name = None #Name未定，先用None占位
    age  = 18
    course = "Python"
    #我想描述一个动作，用函数

    # 1. def doHomework的缩进层级，小于class
    def doHomework(self):   #系统默认self参数
        print("在做作业")
        return None     #建议在函数末尾使用return语句


# 实例化一个叫大锤的学生
dachui = Python_Student()
#注意成员函数的调用没有传递进入参数
dachui.doHomework() # 实例化后用dachui.来调用class里的东西
print(dachui.age)
print(dachui.course)

