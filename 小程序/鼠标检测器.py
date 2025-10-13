import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from PIL import Image, ImageTk


root = tk.Tk()#创建一个主窗口对象，它是所有其他 UI 元素的容器。
root.title("鼠标检测器")# 设置窗口标题。
root.geometry("800x500")#设置窗口初始大小。
root.resizable(True, True)#允许鼠标拉伸自定义窗口大小

import os
import sys

def resource_path(relative_path):
    """获取打包后资源的绝对路径"""
    try:
        # PyInstaller 创建临时目录并将路径存入 _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # 开发环境直接使用当前目录
        base_path = os.path.abspath("小程序")
    return os.path.join(base_path, relative_path)
image_path = resource_path("喜报.jpg")
original_image = Image.open(image_path)

def show_image_and_ask_quit():
    # -------------------------- 子步骤1：弹出图片窗口 --------------------------
    # 创建独立的图片窗口（Toplevel 是 tkinter 的子窗口类）
    image_window = tk.Toplevel(root)
    image_window.title("触发后显示的图片")
    image_window.geometry("900x1200")  # 图片窗口初始大小
    # 锁定图片窗口（用户必须先处理图片窗口，才能操作主窗口）
    image_window.grab_set()

    try:
        # 1. 加载图片（替换为你的图片路径，支持 jpg/png 等格式）
        original_image = Image.open("喜报.png")
        # 2. 缩放图片以适应窗口（避免图片过大/过小）
        resized_image = original_image.resize((900, 1200), Image.LANCZOS)  # 平滑缩放
        # 3. 转换为 tkinter 可识别的图片格式
        tk_image = ImageTk.PhotoImage(resized_image)

        # 4. 用 Label 控件显示图片（Label 是显示图片的最佳选择）
        image_label = tk.Label(image_window, image=tk_image)
        # 关键：将图片对象绑定到 Label 属性（否则图片会被垃圾回收导致不显示）
        image_label.image = tk_image
        image_label.pack(padx=20, pady=20)  # 给图片添加边距

        # 5. 图片窗口的“关闭按钮”逻辑（关闭图片后才触发退出询问）
        def on_image_window_close():
            image_window.destroy()  # 关闭图片窗口
            # -------------------------- 子步骤2：询问是否退出 --------------------------
            # 弹出 yes/no 选项框（title=窗口标题，message=提示内容）
            quit_choice = messagebox.askyesno(
                title="退出确认",
                message="是否要退出程序？\n（选择“是”将关闭程序，“否”返回主界面）"
            )
            # 根据用户选择执行逻辑：True=是，False=否
            if quit_choice:
                root.destroy()  # 退出主程序
            # 选择“否”时不做任何操作，返回主界面

        # 绑定图片窗口的关闭事件（用户点击右上角×时触发）
        image_window.protocol("WM_DELETE_WINDOW", on_image_window_close)

    # 处理图片加载失败的异常（如路径错误、文件损坏）
    except FileNotFoundError:
        messagebox.showerror("错误", "找不到图片文件！\n请检查图片路径是否正确。")
        image_window.destroy()  # 关闭空的图片窗口
    except Exception as e:
        messagebox.showerror("错误", f"图片加载失败：{str(e)}")
        image_window.destroy()

# 创建按钮
center_button = tk.Button(
    root,
    text="开始检测",
    font=("Arial", 100,"bold"),
    padx=20,
    pady=10,
    bg="#2196F3",  # 按钮背景色（蓝色）
    fg="white",  # 按钮文字色（白色）
    command=show_image_and_ask_quit
)

center_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)#让表格填满整个可用空间，并且在窗口大小改变时，表格也会随之伸缩。

# 运行主循环
root.mainloop()
# 启动 Tkinter 的事件循环。这行代码会 “卡住” 程序，直到你关闭窗口。
# 在此期间，程序会一直等待和响应用户的操作（如点击按钮、双击表格等）。
# 任何在mainloop()之后的代码都不会被执行，直到窗口关闭。

