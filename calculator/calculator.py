# -*- coding: utf-8 -*-
"""
简单计算器（Calculator）
=======================

一个零依赖的命令行计算器：支持加、减、乘、除、幂（x 的 y 次方）五种运算，
带循环菜单与完整的输入错误处理。

运行方式::

    cd calculator
    python calculator.py

环境：Python 3.8+（只用标准库 math，无需安装任何第三方包）
"""

import math

# ===== 1. 运算函数 =====


def add(a, b):
    """加法：返回 a + b"""
    return a + b


def subtract(a, b):
    """减法：返回 a - b"""
    return a - b


def multiply(a, b):
    """乘法：返回 a * b"""
    return a * b


def divide(a, b):
    """除法：返回 a / b

    除数为 0 时抛出 ZeroDivisionError，由主循环统一转成友好提示，
    这样运算函数只负责"算数"，不负责"打字"。
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为 0")
    return a / b


def power(a, b):
    """幂运算：返回 a 的 b 次方（a ** b）

    只支持实数结果：
      - 负底数配非整数指数会得到复数，这里直接拒绝（抛 ValueError）
      - 0 的负数次方无意义，抛 ZeroDivisionError
    结果过大时由 a ** b 抛 OverflowError，交给主循环提示。
    """
    if a < 0 and b != int(b):
        raise ValueError("负数不能开非整数次方（结果不是实数）")
    if a == 0 and b < 0:
        raise ZeroDivisionError("0 不能取负数次方")
    return a ** b


# 菜单选项 -> (运算名称, 运算函数, 运算符号)，菜单显示与计算都靠查这张表
OPERATIONS = {
    "1": ("加法", add, "+"),
    "2": ("减法", subtract, "-"),
    "3": ("乘法", multiply, "×"),
    "4": ("除法", divide, "÷"),
    "5": ("幂运算", power, "^"),
}


# ===== 2. 输入解析 =====


def format_number(value):
    """整数结果去掉多余的 .0（例如 7.0 -> 7），其余原样输出

    只对 abs(value) < 1e16 的整数做转换，避免 1e308 被展开成 309 位数字。
    """
    if math.isfinite(value) and abs(value) < 1e16 and value == int(value):
        return str(int(value))
    return str(value)


def get_number(prompt):
    """读取一个数字。

    输入为空、不是数字、或是 inf / nan 这类特殊值时抛出 ValueError，
    由主循环统一转成友好提示，程序不会崩掉。
    """
    text = input(prompt).strip()
    if text == "":
        raise ValueError("输入不能为空")
    try:
        value = float(text)
    except ValueError:
        raise ValueError(f"[{text}] 不是有效数字（示例：3、-1.5、2e3）")
    if not math.isfinite(value):
        raise ValueError("不支持 inf / nan 这类特殊值")
    return value


# ===== 3. 菜单显示 =====


def show_menu():
    """打印操作菜单"""
    print("-" * 32)
    print("           简单计算器")
    print("-" * 32)
    for key, (name, _, symbol) in OPERATIONS.items():
        print(f"  {key}. {name} {symbol}")
    print("  0. 退出")
    print("-" * 32)


def calculate(choice):
    """按菜单选项执行一次计算，并打印算式与结果"""
    name, func, symbol = OPERATIONS[choice]
    a = get_number(f"请输入第一个数字（{name}）：")
    b = get_number("请输入第二个数字：")
    result = func(a, b)
    print(f"{format_number(a)} {symbol} {format_number(b)} = {format_number(result)}")


# ===== 4. 主循环 =====


def main():
    """主循环：显示菜单 -> 读取选项 -> 计算 / 退出

    try 只包住可能出错的语句，不吞掉真正的 bug：
      - 读菜单选项时只捕获 EOFError（管道输入结束）
      - 读数字 / 运算时只捕获 ValueError、ZeroDivisionError 与 OverflowError
      - KeyboardInterrupt 留给最外层统一处理
    """
    print("\n欢迎使用简单计算器！输入 1~5 进行运算，输入 0 退出。")
    while True:
        show_menu()
        try:
            choice = input("请选择操作：").strip()
        except EOFError:
            print("\n检测到输入结束（EOF），程序退出。")
            return

        if choice in ("0", "q", "quit", "exit"):
            print("已退出，欢迎下次使用！")
            return

        if choice not in OPERATIONS:
            print("[提示] 无效选项，请输入 1~5 进行运算，或输入 0 退出。")
            continue

        print("-" * 32)
        try:
            calculate(choice)
        except ValueError as error:
            print(f"[输入错误] {error}，已返回主菜单。")
        except ZeroDivisionError as error:
            print(f"[计算错误] {error}，已返回主菜单。")
        except OverflowError:
            print("[计算错误] 结果太大，超出浮点范围（最大约 1.8e308），已返回主菜单。")
        except EOFError:
            print("\n检测到输入结束（EOF），程序退出。")
            return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n已通过 Ctrl+C 中断，程序退出。")
