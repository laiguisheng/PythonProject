import tkinter as tk
from tkinter import messagebox,ttk

op=['#','+','-','*','/']

def cal(x,y,op):
    if op==1:
        return x+y
    elif op==2:
        return x-y
    elif op==3:
        return x*y
    elif op==4:
        return x/y

#对应的表达式类型：((A#B)#C)#D
def calculate_model1(a,b,c,d,op1,op2,op3):
    r1=cal(a,b,op1)
    r2=cal(r1,c,op2)
    r3=cal(r2,d,op3)
    return r3
#对应的表达式类型：((A#(B#C))#D
def calculate_model2(a,b,c,d,op1,op2,op3):
    r1=cal(b,c,op1)
    r2=cal(r1,a,op2)
    r3=cal(r2,d,op3)
    return r3
#对应的表达式类型：A#(B#(C#D))
def calculate_model3(a,b,c,d,op1,op2,op3):
    r1=cal(c,d,op1)
    r2=cal(r1,b,op2)
    r3=cal(r2,a,op3)
    return r3
#对应的表达式类型：(A#B)#(C#D)
def calculate_model4(a,b,c,d,op1,op2,op3):
    r1=cal(a,b,op1)
    r2=cal(c,d,op2)
    r3=cal(r1,r2,op3)
    return r3
#对应的表达式类型：A#((B#C)#D)
def calculate_model5(a,b,c,d,op1,op2,op3):
    r1=cal(b,c,op1)
    r2=cal(r1,d,op2)
    r3=cal(r2,a,op3)
    return r3

#函数get24()用于寻找符合要求(计算结果为24)的表达式
def get24(a, b, c, d):
    solutions = []  # 存储所有找到的解法
    for op1 in range(1, 5):
        for op2 in range(1, 5):
            for op3 in range(1, 5):
                # 对应的表达式类型：((A#B)#C)#D
                try:
                    if calculate_model1(a, b, c, d, op1, op2, op3) == 24:
                        expr = f"(({a}{op[op1]}{b}){op[op2]}{c}){op[op3]}{d}=24"
                        solutions.append(expr)
                except:
                    pass
                # 对应的表达式类型：(A#(B#C))#D
                try:
                    if calculate_model2(a, b, c, d, op1, op2, op3) == 24:
                        expr = f"({a}{op[op2]}({b}{op[op1]}{c})){op[op3]}{d}=24"
                        solutions.append(expr)
                except:
                    pass
                # 对应的表达式类型：A#(B#(C#D))
                try:
                    if calculate_model3(a, b, c, d, op1, op2, op3) == 24:
                        expr = f"{a}{op[op3]}({b}{op[op2]}({c}{op[op1]}{d}))=24"
                        solutions.append(expr)
                except:
                    pass
                # 对应的表达式类型：(A#B)#(C#D)
                try:
                    if calculate_model4(a, b, c, d, op1, op2, op3) == 24:
                        expr = f"({a}{op[op1]}{b}){op[op3]}({c}{op[op2]}{d})=24"
                        solutions.append(expr)
                except:
                    pass
                # 对应的表达式类型：A#((B#C)#D)
                try:
                    if calculate_model5(a, b, c, d, op1, op2, op3) == 24:
                        expr = f"{a}{op[op3]}(({b}{op[op1]}{c}){op[op2]}{d})=24"
                        solutions.append(expr)
                except:
                    pass
    # 去重
    unique_solutions = []
    for sol in solutions:
        if sol not in unique_solutions:
            unique_solutions.append(sol)
    return unique_solutions


def calculate_click():
    """计算按钮点击事件处理"""
    # 清空之前的结果
    result_text.delete(1.0, tk.END)
    # 获取输入内容
    input_str = input_entry.get().strip()
    if not input_str:
        messagebox.showwarning("提示", "请输入4个数字")
        return
    # 处理中文逗号
    input_str = input_str.replace('，', ',')

    try:
        # 解析输入的数字
        nums = list(map(int, input_str.split(',')))
        if len(nums) != 4:
            messagebox.showerror("错误", "请输入 exactly 4个数字")
            return
        a, b, c, d = nums
        # 验证数字范围
        for num in nums:
            if not (1 <= num <= 10):
                messagebox.showerror("错误", "数字必须在1-10之间")
                return
        # 计算所有可能的解法
        solutions = get24(a, b, c, d)

        # 显示结果
        if solutions:
            result_text.insert(tk.END, f"找到 {len(solutions)} 种解法：\n\n")
            for i, sol in enumerate(solutions, 1):
                result_text.insert(tk.END, f"{i}. {sol}\n")
        else:
            result_text.insert(tk.END, "没有找到可以计算出24的方法")

    except ValueError:
        messagebox.showerror("错误", "输入格式不正确，请使用逗号分隔数字")
    except Exception as e:
        messagebox.showerror("错误", f"发生错误：{str(e)}")

def clear_click():
    """清空按钮点击事件处理"""
    input_entry.delete(0, tk.END)  # 清空输入框
    result_text.delete(1.0, tk.END)  # 清空结果框

root = tk.Tk()
root.title("24点暴力计算器")
root.geometry("800x500")
root.resizable(True, True)
paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
left_frame = ttk.LabelFrame(paned_window, text="输入十以内的四个整数", width=250, height=400)
paned_window.add(left_frame, weight=1)
right_frame = ttk.LabelFrame(paned_window, text="计算结果", width=500, height=400)
paned_window.add(right_frame, weight=2)# weight控制拉伸比例
input_label = ttk.Label(left_frame, text="请输入4个1-10的数字(用逗号分隔):")
input_label.pack(pady=10, padx=10, anchor=tk.W)
input_entry = ttk.Entry(left_frame, width=30)
input_entry.pack(pady=5, padx=10, fill=tk.X)
button_frame = ttk.Frame(left_frame)
button_frame.pack(pady=20, padx=10, fill=tk.X)
#计算按钮
calculate_btn = ttk.Button(button_frame, text="计算24点",command=calculate_click)
calculate_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
# 清空按钮
clear_btn = ttk.Button(button_frame, text="清空",command=clear_click)
clear_btn.pack(side=tk.RIGHT, padx=5, fill=tk.X, expand=True)
# 在右侧视图添加结果显示区域
result_text = tk.Text(right_frame, wrap=tk.WORD, width=50, height=20)
result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
# 添加滚动条
scrollbar = ttk.Scrollbar(result_text, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

root.mainloop()


