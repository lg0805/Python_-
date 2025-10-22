palindrome_num = int(input("请输入一个四位数："))
single = int(palindrome_num / 1000)
ten = int(palindrome_num / 100 % 10)
hundred = int(palindrome_num / 10 % 10)
ths = int(palindrome_num % 10)
reverse_order = ths * 1000 + hundred * 100 + ten * 10 + single
if palindrome_num == reverse_order:
    print(palindrome_num,"是回文数")
else:
    print(palindrome_num,"不是回文数")
