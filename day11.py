#两个名单找缺勤、去重、统计实到率
name={"marry","jane","lily","lucy","tom","jerry"}
late={"jane","lucy","tom"}

late_list=name.intersection(late)
print(f"缺勤学生: {late_list}")

arrived_list=name.difference(late)
print(f"实到学生: {arrived_list}")

arrived_rate=len(arrived_list)/len(name)
print(f"实到率: {arrived_rate:.2%}")