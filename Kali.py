import tkinter as tk
from tkinter import Menu, Frame, Label, Text, Scrollbar

# 創建主視窗
root = tk.Tk()
root.title("Kali Linux 模擬畫面")
root.geometry("1080x720")  # 設置解析度為 1080x720

# 設置背景顏色為 Kali Linux 風格（黑色）
root.configure(bg="black")

# 創建下拉式選單
menu_bar = Menu(root)
root.config(menu=menu_bar)

# 添加選單項目
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="🐬", menu=file_menu)

# 添加指定的選單項目
    file_menu.add_command(label="📁 Favorites")
    file_menu.add_command(label="🗑️Recently Used")
    file_menu.add_command(label="⚙️ Settings")
    file_menu.add_separator()
    file_menu.add_command(label="⚲  01-Information Gathering")
    file_menu.add_command(label="🔓 02-Vulnerability Analysis")
    file_menu.add_command(label="🌐 03-Web Application Analysis")
    file_menu.add_command(label="⛁ 04-Database Assessment")
    file_menu.add_command(label="⚿ 05-Password Attacks")
    file_menu.add_command(label="📶 06-Wireless Attacks")
    file_menu.add_command(label="⛆ 07-Reverse Engineering")
    file_menu.add_command(label="♛  08-Exploitation Tools")
    file_menu.add_command(label="〠 09-Sniffing & Spoofing")
    file_menu.add_command(label="⎗ 10- Post Exploitation")
    file_menu.add_command(label="☝ 11-Forensics")
    file_menu.add_command(label="⎙ 12-Reporting Tools")
    file_menu.add_command(label="🤥 13-Social Enginnering Tools")
    file_menu.add_command(label="🐬 42-Kali & OffSec Links")
    file_menu.add_separator()
    file_menu.add_command(label="退出", command=root.quit)

# 添加 WiFi Password 選項
def show_wifi_password():
    wifi_window = tk.Toplevel(root)
    wifi_window.title("WiFi Password")
    wifi_window.geometry("300x200")
    label = tk.Label(wifi_window, text="Hello!", font=("Arial", 16))
    label.pack(pady=50)

menu_bar.add_command(label="WiFi Password", command=show_wifi_password)

# 右側分頁框架
right_frame = Frame(root, bg="gray", width=400, height=1080)
right_frame.pack(side="right", fill="y")

# 顯示 Password Attacks 分頁
def show_password_attacks():
    clear_right_frame()
    Label(right_frame, text="Password Attacks", bg="gray", fg="white", font=("Arial", 16)).pack(pady=10)
    
    # 添加 Offline Attacks 選項
    offline_menu = Menu(right_frame, tearoff=0)
    offline_menu.add_command(label="chntpw")
    offline_menu.add_command(label="hashcat")
    offline_menu.add_command(label="hashid", command=show_hashid_terminal)
    offline_menu.add_command(label="hash-identifier")
    offline_menu.add_command(label="john")
    offline_menu.add_command(label="ophcrack-cli")
    offline_menu.add_command(label="samdump2")
    
    # 添加 Online Attacks 選項
    online_menu = Menu(right_frame, tearoff=0)
    online_menu.add_command(label="hydra")
    online_menu.add_command(label="medusa")
    online_menu.add_command(label="ncrack")
    online_menu.add_command(label="onesixtyone")
    online_menu.add_command(label="patator")
    online_menu.add_command(label="thc-pptp-bruter")
    
    # 顯示選項
    Label(right_frame, text="⚲Offline Attacks", bg="gray", fg="white", font=("Arial", 12)).pack(anchor="w", padx=20)
    for item in offline_menu.winfo_children():
        item.pack(anchor="w", padx=40)
    
    Label(right_frame, text="⚲Online Attacks", bg="gray", fg="white", font=("Arial", 12)).pack(anchor="w", padx=20)
    for item in online_menu.winfo_children():
        item.pack(anchor="w", padx=40)
    
    Label(right_frame, text="⚲Passing the Hash Tools", bg="gray", fg="white", font=("Arial", 12)).pack(anchor="w", padx=20)
    Label(right_frame, text="⚲Password Profiling & Wordlists", bg="gray", fg="white", font=("Arial", 12)).pack(anchor="w", padx=20)

# 清除右側分頁內容
def clear_right_frame():
    for widget in right_frame.winfo_children():
        widget.destroy()

# 顯示 hashid Terminal 風格的視窗
def show_hashid_terminal():
    terminal_window = tk.Toplevel(root)
    terminal_window.title("hashid Terminal")
    terminal_window.geometry("600x400")
    
    terminal_text = Text(terminal_window, bg="black", fg="green", font=("Courier", 12))
    terminal_text.pack(fill="both", expand=True)
    
    scrollbar = Scrollbar(terminal_window, command=terminal_text.yview)
    scrollbar.pack(side="right", fill="y")
    terminal_text.config(yscrollcommand=scrollbar.set)
    
    terminal_text.insert("end", """
$ hash-identifier
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH:
""")

# 添加一個標籤模擬 Kali Linux 終端機
terminal_label = tk.Label(
    root,
    text="root@kali:~# ",
    fg="green",  # 文字顏色為綠色
    bg="black",  # 背景顏色為黑色
    font=("Courier", 14),
)
terminal_label.pack(anchor="w", padx=20, pady=20)

# 按下 F10 關閉程式
def close_program(event):
    root.destroy()

root.bind("<F10>", close_program)

# 運行主循環
root.mainloop()