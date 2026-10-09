#Mini Project 2：多轮连续对话的命令行聊天机器人
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
print(f"当前工作目录是: {os.getcwd()}")
api_key=os.getenv("DEEPSEEK_API_KEY")
print(f"Deepseek的API是:{api_key[:5]}*****{api_key[-4:]}")

messages=[
    {
        "role":"system",
        "content":"你是一位专业且厉害的python高手"
    }
]

while True:
    user_input=input("我有什么可以帮您？")
    if user_input=="没有":
        print("祝您生活愉快,再见！")
        break
    if user_input=="no":
        print("祝您生活愉快,再见！")
        break
    if user_input=="没有了":
            print("祝您生活愉快,再见！")
            break
    # 把用户这一轮说的话存进历史记录，实现多轮上下文
    messages.append({"role":"user","content":user_input})

    url="https://api.deepseek.com/chat/completions"
    headers ={
        "Authorization": f"Bearer {api_key}",
        "Content-Type":"application/json"
    }
    payload={
        "model":"deepseek-chat",
        "messages":messages
    }
    response=requests.post(url,headers=headers,json=payload,timeout=30)
    if response.status_code==200:
        data=response.json()
        ai_reply = data["choices"][0]["message"]["content"]
        print(ai_reply)
        messages.append({"role": "assistant", "content": ai_reply})
    else:
        print(response.text)
        print(response.status_code)
