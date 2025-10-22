select = input('是否需要下载？（y/n）：')
if select == 'y' or select == 'Y':
    print('----正在请求下载----')
elif select == 'n' or select == 'N':
    print('----3秒后将返回首页----')
elif select != 'y' and 'n':
    print('输入有误，请重新选择')



