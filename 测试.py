import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
bg_image = Image.open("小程序/24点暴力计算器/2023.png")  # 替换为你的图片路径
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
root.mainloop()