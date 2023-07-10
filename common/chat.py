import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random
import openai
import datetime
import pyperclip
import pandas as pd
import time


openai.api_key = "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"
# os.environ['NO_PROXY']='api.openai.com'

# chatGPT3.5支持连续对话
MAX_TEXT_LENGTH = 1024

# 创建一个DataFrame用于存储每次翻译结果
df = pd.DataFrame(columns=['发送的内容', '收到的回复'])
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

# 获取聊天窗口的初始问候语
def get_initial_greeting():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.5,
        max_tokens=MAX_TEXT_LENGTH,
        top_p=1,
        n=1
    )
    answer = response['choices'][0]['message']['content']
    return "聊天机器人: " + answer


# 根据用户输入选择回复
def get_chatgpt_response(user_message):
    conversation.append({"role": "user", "content": user_message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.5,
        max_tokens=MAX_TEXT_LENGTH,
        top_p=1,
        n=1
    )
    answer = response['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": answer})
    return answer

# 处理发送按钮点击事件
def send_message():
    user_message = entry.get("1.0", tk.END).strip()  # 获取用户输入的消息
    if user_message.lower() == '退出':  # 如果用户输入"退出"，关闭窗口
        window.destroy()
    else:
        response = get_chatgpt_response(user_message)  # 获取ChatGPT的回复
        add_chat_bubble("你: " + user_message, "blue")  # 在聊天窗口中显示用户消息
        add_chat_bubble("聊天机器人: " + response, "green")  # 在聊天窗口中显示机器人回复
        entry.delete("1.0", tk.END)  # 清空输入框
        chat_log.yview_moveto(1)  # 将聊天日志滚动到最底部

# 在聊天窗口中添加聊天气泡
def add_chat_bubble(message, color):
    chat_frame = ttk.Frame(chat_log, style="Chat.TFrame")
    chat_frame.pack(pady=5, anchor="w")

    bubble_label = ttk.Label(chat_frame, text=message, style=f"{color}.TLabel")
    bubble_label.pack(padx=10, pady=5, anchor="w")
    chat_log.yview_moveto(1)  # 将聊天日志滚动到最底部

# 创建主窗口
window = tk.Tk()
window.title("简历解析机器人")

# 创建网格布局
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)

# 创建可调整大小的窗口
paned_window = ttk.PanedWindow(window, orient=tk.VERTICAL)
paned_window.grid(row=0, column=0, sticky="nsew")

# 创建聊天日志的滚动文本框
chat_log_frame = ttk.Frame(window)
chat_log_frame.grid(row=0, column=0, sticky="nsew")

chat_log = ScrolledText(chat_log_frame, width=50, height=20)
chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(chat_log_frame, command=chat_log.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_log.configure(yscrollcommand=scrollbar.set)

# 创建输入框和发送按钮
entry = tk.Text(window, height=8)
entry.grid(row=1, column=0, sticky="ew")
send_button = tk.Button(window, text="发送", command=send_message)
send_button.grid(row=1, column=1)

# 设置聊天窗口样式
style = ttk.Style()
style.configure("Chat.TFrame", background="white")
style.configure("blue.TLabel", background="#DCF8C6", foreground="black", font=("Arial", 11), justify="right")
style.configure("green.TLabel", background="#F0F0F0", foreground="black", font=("Arial", 11), justify="left")

# 显示初始问候语
initial_greeting = get_initial_greeting()
add_chat_bubble(initial_greeting, "green")

# 绑定回车键与发送消息的函数
entry.bind("<Return>", lambda event: send_message())

# 启动主循环
window.mainloop()
