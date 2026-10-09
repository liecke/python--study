#把 Day 5 成绩统计改写成 3 个函数
lt=[90,87,73,96,65,81,60,55,38]
def analyze_scores(lt): 
    x=max(lt)
    y=min(lt)
    print(x)
    print(y) 
analyze_scores(lt)

def fail__pass(lt):
    for score in lt:
        if score>=60:
            print(f"{score}分:及格")
        else:
            print(f"{score}分:不及格")
fail__pass(lt)

def details(lt):
    for index,score in enumerate(lt, start=1):
        if score>=60:
            result="及格"
        else:
            result="不及格"
        print(f"第{index}位学生:{score}分,{result}")
details(lt)
