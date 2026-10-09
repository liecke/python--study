#写 Student 类并创建 3 个实例
class Student:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def show_info(self):
        print(f"我是{self.name},我的身高是{self.height}")

stu1=Student("小明",180)
stu2=Student("小红",168)
stu3=Student("小刚",176)

stu1.show_info()
stu2.show_info()
stu3.show_info()