#给 Day 10 函数补标注；读一段团队真实代码

#day10代码
lt: list[int]=[90,87,73,96,65,81,60,55,38]
def analyze_scores(lt: list[int]) -> None:
    x=max(lt)
    y=min(lt)
    print(x)
    print(y) 
analyze_scores(lt)

def fail__pass(lt:list[int]) -> None:
    for score in lt:
        if score>=60:
            print(f"{score}分:及格")
        else:
            print(f"{score}分:不及格")
fail__pass(lt)

def details(lt:list[int]) -> None:
    for index,score in enumerate(lt, start=1):
        if score>=60:
            result="及格"
        else:
            result="不及格"
        print(f"第{index}位学生:{score}分,{result}")
details(lt)
