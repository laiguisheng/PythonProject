import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os
import uuid
import pyperclip
"""
tkinter是Python 的标准 GUI（图形用户界面）库。这是构建窗口、按钮、文本框等所有可视元素的基础。
tk是tkinter的核心模块
messagebox: 用于弹出提示框、警告框、确认框。
simpledialog: 用于弹出简单的输入对话框，方便快速获取用户的单行输入。
ttk: "主题化 Tk"，提供了更现代化的 UI 组件，如Treeview表格，它比tk自带的旧组件更美观、功能更强大。
json: 用于处理 JSON 数据格式。我们选择 JSON 文件来存储密码，因为它是一种轻量级的文本格式，结构清晰（键值对），
易于人类阅读和机器解析，非常适合存储这种结构化数据。
os: 用于与操作系统交互。在这里，我们用它来检查数据文件（passwords.json）是否已经存在，
避免在第一次运行时因文件不存在而报错。
uuid: 用于生成唯一标识符（Universally Unique Identifier）。当我们添加一个新密码时，需要一个独一无二的 
ID 来标识它。使用uuid可以确保即使两个密码的标题和内容完全相同，它们也不会被混淆。
pyperclip: 一个跨平台的库，用于访问剪贴板。这样我们就能实现 “复制密码到剪贴板” 这个非常方便的功能。
"""

# 数据文件路径
DATA_FILE = "../../Documents/passwords.json"
#DATA_FILE = "passwords.json": 定义一个常量来存储文件名。这样做的好处是，
# 如果以后想改名（比如改成my_secrets.json），
# 只需要修改这一处即可，不用在代码中到处寻找和替换。


def load_passwords():
    """加载已保存的密码数据"""
    if os.path.exists(DATA_FILE):#检查文件是否存在
        with open(DATA_FILE, 'r', encoding='utf-8') as f:#使用with语句打开文件能确保操作完成后文件自动关闭
            return json.load(f)#将json文件中的内容解析成一个python字典
    return {}#如果文件不存在就会返回一个空字典，使程序仍能启动


def save_passwords(data):
    """保存密码数据到文件"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:#'w'模式表示写入，如果文件已存在会被覆盖
        json.dump(data, f, ensure_ascii=False, indent=4)#将python字典data写入文件并格式化为json字符串
        #ensure_ascii=False: 允许我们在 JSON 中直接写入中文等非 ASCII 字符，而不是被转义成\uXXXX的形式。
        #indent=4: 让生成的 JSON 文件有 4 个空格的缩进，非常美观易读。


def add_password():
    """添加新密码条目"""
    title = simpledialog.askstring("添加密码", "请输入密码标题/名称:")
    if not title:
        return

    username = simpledialog.askstring("添加密码", "请输入用户名:")
    if not username:
        return

    password = simpledialog.askstring("添加密码", "请输入密码:", show='*')
    if not password:
        return

    notes = simpledialog.askstring("添加密码", "请输入备注信息 (可选):")

    passwords = load_passwords()
    entry_id = str(uuid.uuid4())
    #entry_id = str(uuid.uuid4()): 生成一个唯一 ID，并将其作为新密码条目的键（key）存入字典。
    #这样设计，使得后续的删除和查找操作非常高效（字典的键查找速度很快）。
    passwords[entry_id] = {
        "title": title,
        "username": username,
        "password": password,
        "notes": notes or ""
    }

    save_passwords(passwords)
    messagebox.showinfo("成功", "密码已成功添加！")
    refresh_list()


def delete_password():
    """删除选中的密码条目"""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("警告", "请先选择要删除的密码条目")
        return

    item_id = tree.item(selected_item[0])['tags'][0]
    passwords = load_passwords()

    if messagebox.askyesno("确认删除", "确定要删除这个密码条目吗？"):
        #messagebox.askyesno(...): 在执行删除这种不可逆的操作前，弹出一个确认对话框，防止用户误操作。这是一个非常重要的用户体验细节。
        del passwords[item_id]
        save_passwords(passwords)
        messagebox.showinfo("成功", "密码已成功删除！")
        refresh_list()


def copy_to_clipboard():
    """复制选中的密码到剪贴板"""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("警告", "请先选择要复制的密码条目")
        return

    item_id = tree.item(selected_item[0])['tags'][0]
    #tree.item(selected_item[0])['tags'][0]: 这是一个关键的技巧。
    # 我们在创建表格行时，将密码条目的唯一 ID（entry_id）作为 “标签”（tag）附加到了该行上。
    # 这样，当用户在界面上选中一行时，我们就能通过这个标签轻松地找到它在数据字典中对应的键，从而执行删除操作。
    passwords = load_passwords()

    if item_id in passwords:
        password = passwords[item_id]['password']
        pyperclip.copy(password)
        messagebox.showinfo("成功", "密码已复制到剪贴板！")


def refresh_list():
    """刷新密码列表"""
    for item in tree.get_children():
        tree.delete(item)

    passwords = load_passwords()
    for pid, data in passwords.items():
        tree.insert('', tk.END, values=(data['title'], data['username'], data['notes']), tags=(pid,))


def on_item_double_click(event):
    """双击条目时复制密码"""
    copy_to_clipboard()


# 创建主窗口
root = tk.Tk()#创建一个主窗口对象，它是所有其他 UI 元素的容器。
root.title("密码管理器")# 设置窗口标题。
root.geometry("800x500")#设置窗口初始大小。
root.resizable(True, True)

# 创建顶部按钮区域
top_frame = tk.Frame(root, padx=10, pady=10)
#创建一个框架（容器）来放置按钮。使用框架可以更好地组织 UI 布局，避免所有控件都直接堆在主窗口上。
top_frame.pack(fill=tk.X)

add_btn = tk.Button(top_frame, text="添加密码", command=add_password, width=15)
#创建按钮
#command=add_password: 这是事件绑定的核心。它告诉 Tkinter：“当这个按钮被点击时，请调用add_password这个函数。”
delete_btn = tk.Button(top_frame, text="删除选中", command=delete_password, width=15)
delete_btn.pack(side=tk.LEFT, padx=5)#让按钮们从左到右依次排列。
#pack：一种简单的布局管理器。
copy_btn = tk.Button(top_frame, text="复制密码", command=copy_to_clipboard, width=15)
copy_btn.pack(side=tk.LEFT, padx=5)

# 创建表格视图
columns = ("标题", "用户名", "备注")
tree = ttk.Treeview(root, columns=columns, show="headings")
#创建一个表格。columns定义了列名，show="headings"表示只显示列标题，不显示默认的第一列（它通常用于内部 ID）。

# 设置列标题
for col in columns:
    tree.heading(col, text=col)
    #设置每一列的标题文本。
    tree.column(col, width=200, anchor=tk.W)
    #设置列宽和对齐方式（W代表 West，即左对齐）。

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
#让表格填满整个可用空间，并且在窗口大小改变时，表格也会随之伸缩。

# 绑定双击事件
tree.bind("<Double-1>", on_item_double_click)
#这是另一种事件绑定方式。它监听tree控件上的特定事件。
#"<Double-1>": 代表鼠标左键双击事件。
#on_item_double_click: 当双击事件发生时，调用这个函数。在这里，我们用它来实现 “双击复制密码” 的快捷功能。

# 加载并显示现有密码
refresh_list()
#在程序启动后立即调用一次，以便加载并显示已有的密码数据。

# 运行主循环
root.mainloop()
# 启动 Tkinter 的事件循环。这行代码会 “卡住” 程序，直到你关闭窗口。
# 在此期间，程序会一直等待和响应用户的操作（如点击按钮、双击表格等）。
# 任何在mainloop()之后的代码都不会被执行，直到窗口关闭。