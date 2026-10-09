#猜数字游戏：随机数 + 循环 + 计数（BMI 计算器作热身）
import random
target=random.randint(1,100)
count=0
while True:
  guess = int(input("请猜一个 1-100 的整数："))
  count+=1
  if guess==target:
    print("恭喜你，猜对了！")
    print(f"你一共猜了 {count} 次。")
    break
  if guess<target:
    print("数字小了！")
  if guess>target:
    print("数字大了！")