#日志统计：总行数、ERROR 次数、最长一行
log_txt="""INFO 程序开始
ERROR 数据库失常
INFO 用户登入成功
ERROR 网络异常
INFO 测试功能
INFO 这是一条非常非常长的日志，用来测试最长一行的统计功能
"""
with open("app.log","w",encoding="utf-8")as f:
 f.write(log_txt)
 #运行后生成app.log

#写入数据后读数据
with open("app.log","r",encoding="utf-8")as f:
 lines = f.readlines()
 print(lines)

total_lines=0
error_count=0
longest_line=""
for line in lines:
  total_lines+=1
  if "ERROR" in line:
   error_count+=1
   #直接用 len(line) 会算上末尾的换行符 \n。
   # 需要先用 .strip() 去掉首尾空白，得到一个干净的字符串 clean_line。
  clean_line = line.strip() 
  if len(clean_line) > len(longest_line):
        longest_line = clean_line

print(f"总行数: {total_lines}")
print(f"ERROR次数: {error_count}")
print(f"最长一行: {longest_line}")

# Path 拼路径 / 遍历
from pathlib import Path
log_file=Path("app.log")
# print(log_file)    不可以直接打印，只会输出app.log
if log_file.exists():
    lines = log_file.read_text(encoding="utf-8").splitlines()
    print(lines)
