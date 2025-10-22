price_li = [399, 4369, 539, 288, 109, 749, 235, 190, 99,1000]
section_li = []
max_section = int(input("请输入最大价格:"))
min_section = int(input("请输入最小价格:"))
for i in price_li:
    if min_section <= i <= max_section:
        section_li.append(i)
print("1.价格降序排序")
print("2.价格升序排序")
choice_num = int(input("请选择排序方式:"))
if choice_num == 1:
    section_li.sort(reverse=True)
else:
    section_li.sort()
print(section_li)
