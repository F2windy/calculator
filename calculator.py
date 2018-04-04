#!/user/bin/env python#  -*-coding:utf-8-*-
# calculator.py
# 导入tkinter模块所有内容
from tkinter import *
reset = True
# 点击按钮执行的事件
def buttonCallBack(event):
    global label  # 全局变量
    global reset
    num = event.widget['text']
    if num == 'C':
        label['text'] = " "
        return
    if num in "=":
        # eval() 函数用来执行一个字符串表达式，并返回表达式的值
        if label['text'][-1] == "0":
            label['text'] = "除数不能是0"
        label['text'] = str(eval(label['text']))
        reset = False
        return
    s = label['text']
    if reset == True:
        s = ""
        reset = False
    label['text'] = s + num
# 主窗口
root = Tk()
root.wm_title("计算器")
# 显示栏1
label = Label(root, text=" ", background="green", anchor="e")  # 文本或图像在Label的位置 east
label['width'] = 35
label['height'] = 2
label.grid(row=1, columnspan=4, sticky=W)  # 行1列4 sticky对齐方式为west
# 按钮
showText = "789/456*123-0.C+"  # 按键内容
# 将按键以4*4矩阵排列
for i in range(4):
    for j in range(4):
        # 设置按钮位置和大小
        b = Button(root, text=showText[i * 4 + j], width=7, bg="green")
        # Grid(网格)布局管理器
        b.grid(row=i + 2, column=j)
        # 将控件事件与控件做绑定（事件类型，事件名）
        b.bind("<Button-1>", buttonCallBack)  # 将按钮与事件关联
# 等号与括号布局
showText = "()"
for i in range(2):
    b = Button(root, text=showText[i], width=7, bg="green")
    b.grid(row=6, column=2 + i)
    b.bind("<Button-1>", buttonCallBack)  # 将按钮与事件关联
b = Button(root, text="=", bg="green")
b.grid(row=6, columnspan=2, sticky="we")  # westeast
b.bind("<Button-1>", buttonCallBack)
# 执行后程序进入主事件循环
root.mainloop()
# 缺点：没有异常处理
