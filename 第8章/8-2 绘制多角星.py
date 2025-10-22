import turtle as t
t.color('black', 'red')   # 设置画笔颜色，以及填充颜色
t.setup(450, 400)           # 设置主窗口的大小为450*400
t.begin_fill()              # 在绘制要填充的形状之前调用
while True:
    t.forward(150)          # 向当前画笔移动150个像素
    t.left(150)             # 逆时针移动150
    if abs(t.pos()) < 1:    # 如果当位置绝对值小于跳出循环
        break
t.end_fill()                # 结束填充位置
t.done()                    # 停止画笔绘制，窗体不关闭
