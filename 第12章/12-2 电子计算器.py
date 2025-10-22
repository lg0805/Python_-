from tkinter import *
# from tkinter.ttk import *


def frame(master):
    """将共同的属性作为默认值, 以简化Frame创建过程"""
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH)
    return w


def btn(master, text, command):
    """提取共同的属性作为默认值, 使Button创建过程简化"""
    w = Button(master, text=text, command=command, width=6)
    w.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2)
    return w


def calc(text_data):
    """用eval方法计算表达式字符串"""
    try:
        if (separator_flag.get() == 0):
            return eval(del_separator(text_data))
        else:
            return add_separator(str(eval(del_separator(text_data))))
    except (SyntaxError, ZeroDivisionError, NameError):
        return 'Error'


def back(text_data):
    """将text_data最末的字符删除并返回"""
    if len(text_data) > 0:
        return text_data[:-1]
    else:
        return text_data


def add_separator(text_data):
    """向参数传入的数字串中添加千位分隔符

    这里考虑了三种情况: 无整数部份, 无小数部份, 同时有整数和小数部份
    由于字符串是不可改变的, 这里由字符串生成列表以便执行insert操作和
    extend操作, 操作完成后最由列表生成字符串返回
    """
    dot_index = text_data.find('.')
    if dot_index > 0:
        text_head = text[:dot_index]
        text_tail = text[dot_index:]
    elif dot_index < 0:
        text_head = text_data
        text_tail = ''
    else:
        text_head = ''
        text_tail = text_data

    list_ = [char for char in text_head]
    length = len(list_)
    tmp_index = 3
    while length - tmp_index > 0:
        list_.insert(length - tmp_index, ',')
        tmp_index += 3
    list_.extend(text_tail)
    new_text = ''
    for char in list_:
        new_text += char

    return new_text


def del_separator(text_data):
    """删除数字串中所有的千位分隔符"""
    return text_data.replace(',', '')


# 开始界面的实现
init_root = Tk()
init_root.resizable(width=False, height=False)

init_root.title("计算器")  # 添加标题

main_menus = Menu()  # 创建最上层主菜单

# 创建计算器菜单, 并加入到主菜单
calc_menu = Menu(main_menus, tearoff=0)
calc_menu.add_command(label='退出', command=lambda: exit())
main_menus.add_cascade(label='菜单', menu=calc_menu)

text = StringVar()
separator_flag = IntVar()
separator_flag.set(0)
view_menu = Menu(main_menus, tearoff=0)

init_root['menu'] = main_menus  # 将主菜单与root绑定

# 创建文本框
Entry(init_root, textvariable=text).pack(expand=YES, fill=BOTH, padx=2, pady=4)

# style = Style()
# style.configure('TButton', padding=3)

# 创建第一行三个按钮
first_line = frame(init_root)
btn(first_line, '回退', lambda t=text: t.set(back(t.get())))
btn(first_line, '清空', lambda t=text: t.set(''))

# 每行四个, 创建其余四行按钮
for key in ('789/', '456*', '123-', '0.=+'):
    others = frame(init_root)
    for char in key:
        if char == '=':
            btn(others, char,
                lambda data=text: data.set(calc(data.get())))
        else:
            btn(others, char,
                lambda data=text, c=char: data.set(data.get() + c))
if __name__ == '__main__':

    init_root.mainloop()
