#word=("hello", "world")
#result=",".join(word)
#print(result)

diary="日期:2023-10-01  级别:重要  天气:晴朗  星期:星期日   内容:今天天气很好,适合出去玩"

to_two=diary[0:24:24]
print(to_two)
print(diary.split(":")[0])
#print(diary.split(":")[1].split(":")[0])
date=diary.split(":")[1].split("  ")[0]
level=diary.split(":")[2].split("  ")[0]
content=diary.split(":")[5]
print(f"日期: {date}")
print(f"级别: {level}")
print(f"内容: {content}")