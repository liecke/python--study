# lt=[1,2,9,7,3]
# x=max(lt)
# print(x)

#最大、最小
lt=[90,87,73,96,65,81,60,55,38]
x=max(lt)
y=min(lt)
print(x)
print(y)
#排序
lt.sort()
print(lt)
#平均
average=sum(lt)/len(lt)
print(average)
#求长度
a=len(lt)
print(a)
#判断及格
#及不及格判断（逐个打印）
for score in lt:
    if score >= 60:
        print(f"{score}分：及格")
    else:
        print(f"{score}分：不及格")
#for+emumrate
for index,score in enumerate(lt, start=1):
 if score>=60:
      result="及格"
 else:
    result="不及格"
 print(f"第{index}位学生:{score}分,{result}")#一开始不对是因为缩进的时候与else对齐，变成else里一部分

# for index, score in enumerate(lt, start=1):
#     if score >= 60:
#         result = "及格"
#     else:
#         result = "不及格"
    
#     # 同时打印序号、分数、结果
#     print(f"第{index}位学生：{score}分，{result}")
