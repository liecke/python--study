#学生信息管理：嵌套结构存 5 人，查询 / 添加 / 按条件统计（平均分、不及格名单），独立完成
students = [
    {'name': '张三', 'age': 18, 'score': 53},
    {'name': '李四', 'age': 19, 'score': 92},
    {'name': '王五', 'age': 20, 'score': 78}
]
# print(students)

# #查询
# def query_student(target_name):
#     for student in students:
#         if student['name']== target_name:
#             print(f"找到学生：{student['name']}, 年龄：{student['age']}, 分数：{student['score']}")
#             return student
#     print(f"未找到学生：{target_name}")
# query_student('张三')

# #添加
# def add_student():
#     name = "王五"       # 直接给变量赋值
#     age = 17
#     score = 68
#     students.append({'name': name, 'age': age, 'score': score})
#     print(f"学生 {name} 已添加到列表中。")
# add_student()
# print(students)

#按条件统计（平均分、不及格名单）
def statistics():
    total=0
    fail_list=[]
    for student in students:
        total +=student["score"]
    # if student["score"]<60:
    #     fail_list.append(student["name"])
    if student["score"] < 60:
            # 加上这一句调试代码
        print(f"调试：发现不及格学生 {student['name']}，分数是 {student['score']}")
        fail_list.append(student["name"])
    print(total)
    print(fail_list)
    average=total/len(students)
    print(average)
statistics()
     