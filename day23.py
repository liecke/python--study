#根据cline给的修改建议修改day12代码

#Mini Project 1：命令行 Todo List

PRIORITY_LEVELS = {"1": "高", "2": "中", "3": "低"}   # 用户输入 -> 标准值     字典写法
#__为什么键是字符串 `"1"` 而不是数字 `1`__：因为 `input()` __永远返回字符串__。
DEFAULT_PRIORITY = "中"                              # 兜底/默认值
#__避免"魔法字符串"__：如果哪天你想把默认值改成"低"，只改这一行就行；如果到处硬编码 `"中"`，你得全文搜一遍，漏一个就出 bug；
PRIORITY_ORDER = {"高": 0, "中": 1, "低": 2}          # 现在用不到，留给以后排序
#优先级之间的大小权重。数字越小越靠前。

# __表意__：`.get('priority', DEFAULT_PRIORITY)` 读起来就是"取优先级，取不到就用默认优先级"，比 `.get('priority', "中")` 更清楚。
#get('xxx','默认值')

tasks=[
    {
        "task": "今日打卡",
        "done": False,
        "priority":"中"
    },
    {
        "task": "今日学习",
        "done": True,
        "priority":"高"
    }
]

def todo_list():
    print("\n---代办清单---")
    if len(tasks)==0:
        print("暂无代办事项")
        return
    for index,item in enumerate(tasks,start=1):
        if item["done"]:
          status="[√]"
        else:
            status="[ ]"
        print(f"{index}. {status} {item['task']} [{item.get('priority', DEFAULT_PRIORITY)}]")



#增
def get_tasks():
    name = input("请输入代办事项\n")
    while True:
        level = input("请输入优先级(1高 2中 3低)\n")
        if level in PRIORITY_LEVELS:
            break   # 合法 → 跳出循环，后面才继续
        print("优先级输入有误，请输入 1、2 或 3")
    works = {
        "task": name,
        "done": False,
        "priority": PRIORITY_LEVELS[level]
    }
    tasks.append(works)
    print("添加成功")



#查，改，删
def get_details():
    print("点击查看任务(请输入yes)")
    if input() == "yes":
        print(tasks)
    while True:
     for index, item in enumerate(tasks,start=1):
        print(f"{index}.{item['task']},完成状态：{item['done']},优先级：{item.get('priority', DEFAULT_PRIORITY)}")
   
     print("接下来你想要？(1)标记完成任务 (2)删除任务 (3)修改任务 (4)退出")
     
     choice = input("请输入你的选择：")

     if choice=="1":
        task_index=int(input("请输入要标记完成的任务序号："))
        if 1 <= task_index <= len(tasks):
           tasks[task_index-1]["done"]=True
           print("任务已标记为完成")
        else:
              print("输入序号错误，请重新输入")
     elif choice=="2":
        task_index=int(input("请输入要删除的任务序号："))
        if 1 <= task_index <= len(tasks):
           del tasks[task_index-1]
           print("任务已删除")
        else:
           print("输入序号错误，请重新输入")
     elif choice=="3":
         task_index=int(input("请输入要修改的任务序号："))
         if 1 <= task_index <= len(tasks):
              new_task=input("请输入新的任务内容：")
              tasks[task_index-1]["task"]=new_task
              print("任务已修改")
         else:
                print("输入序号错误，请重新输入")
     elif choice=="4":
        print("退出任务管理")
        break


def main():
  while True:
    print("\n菜单：1.查看 2.添加 3.标记 4.删除 5.待办清单 6.退出")
    choice=input("请输入")
    if choice=="1":
        get_details()
    elif choice=="2":
        get_tasks()
    elif choice=="3":
        get_details()
    elif choice=="4":
        get_details()
    elif choice=="5":
        todo_list()
    else:
        print("退出任务管理")
        break 
main()
