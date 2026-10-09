#Mini Project 1：命令行 Todo List
tasks=[
    {
        "task": "今日打卡",
        "done": False
    },
    {
        "task": "今日学习",
        "done": True
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
        print(f"{index}. {status} {item['task']}")


#增
def get_tasks():
    works={
            "task": input("请输入代办事项"),
            "done": False
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
        print(f"{index}.{item['task']},完成状态：{item['done']}")
        
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
