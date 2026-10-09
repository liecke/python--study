#给 Todo 建 venv、锁依赖、把 DeepSeek Key 放进 .env 并读出来
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
print(f"当前工作目录是: {os.getcwd()}")
api_key=os.getenv("DEEPSEEK_API_KEY")
# 只显示前 5 位和后 4 位，中间隐藏
print(f"API Key 读取成功：{api_key[:5]}****{api_key[-4:]}")
