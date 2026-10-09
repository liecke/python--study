#修 5 段带 bug 的代码：读懂报错 → 定位 → 修复

# 目标：打印一句问候语
# name = "小明"
# if name == "小明"
#     print("你好，小明！")

#错误点，if语句后没加冒号
# name="小明"
# if name=="小明":
#     print("你好，小明！")

## 目标：计算并打印年龄
# my_age = 18
# print(f"我的年龄是: {my_age}")
# print(f"我的名字是: {my_name}")

#错误点，变量名未定义
# my_age=18
# my_name="小明"
# print(f"我的年龄是{my_age}")
# print(f"我的名字是{my_name}")

# 目标：计算总和
# price = "19.9"
# count = 3
# total = price * count
# print(f"总价是: {total}")

price = 19.9
count = 3
total =float(price * count)
print(f"总价是: {total}")

# deepseek的答案
# price =float( "19.9")
# count = 3
# total = price * count
# print(f"总价是: {total}")


# 目标：打印第 3 个同学的名字
# students = ["张三", "李四", "王五"]
# print(f"第3个同学是: {students[3]}")

students=["张三","李四","王五"]
print(f"第三个学生是:{students[2]}")


# 目标：打印学生的分数
# student = {"name": "小红", "age": 18}
# print(f"小红的分数是: {student['score']}")

#改法一
student = {"name": "小红", "age": 18}
student["score"] = 90  # 手动加进去
print(f"小红的分数是: {student['score']}")

#改法二
student = {"name": "小红", "age": 18}
score=student.get("score",90)
print(f"小红的分数是:{score}")