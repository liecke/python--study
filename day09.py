#用 zip 把两个名单配成 (姓名, 分数) 对并遍历；
# 写 3 行代码踩一次 b = a 的坑
names=["marry","jane","lily"]
scores=[64,23,54]
result=zip(names,scores)
result_list=list(result)
print(result_list)

#使用zip进行迭代
for name,score in zip(names,scores):
    print(f"{name}的分数是{score}")

#踩坑，此时a列表值也发生改变
a = [1, 2, 3]
b = a
b.append(4)
print(a)

#正确做法
b=a.copy()
b.append(5)
print(a)
print(b)