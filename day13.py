#课堂点名器：随机点 3 人不重复
#迅速响应版
# import random
# print("欢迎使用课堂点名器,请问是否要开始随机点名？(yes/no)")
# while True:
#     if input()=="yes":
#        students=["marry","jack","tom","lucy","lily","james","john","jane","mike","susan"]
#        selected_student=random.choice(students)
#        print(f"被点到的学生是：{selected_student}")
#        print("是否继续点名？(yes/no)")
#     else:
#         print("退出点名器")
#         break


#加入time标准库
import random
import time
print("欢迎使用课堂点名器,请问是否要开始随机点名？(yes/no)")
while True:
    if input()=="yes":
      print("请告诉我你要抽取的学生人数(1-5)：")
      num_students=int(input())
      if 1<=num_students<=5:
       students=["marry","jack","tom","lucy","lily","james","john","jane","mike","susan"]
       selected_students=random.sample(students, num_students)
       time.sleep(1)
       print(f"被点到的学生是: {', '.join(selected_students)}")
       print("是否继续点名？(yes/no)")
    else:
     print("退出点名器")



