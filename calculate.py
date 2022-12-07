import tkinter.messagebox

# 定义窗口
root = tkinter.Tk()
root.title('标准计算器')
root.geometry('350x660')
# 定义历史记录文本框
history_list = tkinter.Listbox(root, width=45, height=15)
history_list.place(x=10, y=60)
# 定义按键
btn_list = []
btn_text = [
    'C', '=', '%', '√', '1',
    '2', '3', '+', '4', '5',
    '6', '-', '7', '8', '9',
    '*', '.', '0', '1/x', '/'
]


# 定义按键函数
def btn_click(btn_text):
    if btn_text == '=':
        result = eval(show_result.get())
        history_list.insert(0, show_result.get() + '=' + str(result))
        show_result.set(str(result))
    elif btn_text == 'C':
        show_result.set('')
    elif btn_text == '√':
        result = eval(show_result.get()) ** 0.5
        show_result.set(str(result))
    elif btn_text == '%':
        result = eval(show_result.get()) / 100
        show_result.set(str(result))
    elif btn_text == '1/x':
        result = 1 / eval(show_result.get())
        show_result.set(str(result))
    else:
        show_result.set(show_result.get() + btn_text)


# 定义显示结果文本框
show_result = tkinter.StringVar()
result_text = tkinter.Entry(root, textvariable=show_result, width=50, font=('微软雅黑', 20))
result_text.place(x=10, y=10)
# 定义按键
for i in range(len(btn_text)):
    btn_list.append(
        tkinter.Button(root, text=btn_text[i], width=5, height=2, command=lambda x=btn_text[i]: btn_click(x)))
# 放置按键
for i in range(5):
    for j in range(4):
        btn_list[i * 4 + j].place(x=10 + (j * 90), y=360 + (i * 60))

# 进入消息循环
tkinter.mainloop()
