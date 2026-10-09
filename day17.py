#给 Todo 加持久化：存成 todo.json，重启不丢
import json
TODO={'task1':'读懂','task2':'做笔记','task3':'写代码','task4':'记录'}
#将python字典变成json字符串
json_str = json.dumps(TODO, ensure_ascii=False)
print("这是转成字符串的结果：")
print(json_str)

with open("todo.json","w",encoding="utf-8")as f:
    f.write(json_str)
    print("已存档")

with open("todo.json","r",encoding="utf-8")as f:
    data=f.read()
    print(data)