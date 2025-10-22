# def hanoi(num, start_pos, end_pos, mid_pillar):
#     if num == 1:  # 边界条件
#         plate = start_pos[0].pop()
#         print('移动盘子 ' + str(plate) + ' 从 ' + start_pos[1] + ' 到 ' + end_pos[1])
#         end_pos[0].append(plate)
#     else:
#         hanoi(num - 1, start_pos, mid_pillar, end_pos)
#         plate = start_pos[0].pop()
#         print('移动盘子 ' + str(plate) + ' 从 ' + start_pos[1] + ' 到 ' + end_pos[1])
#         end_pos[0].append(plate)
#         hanoi(num - 1, mid_pillar, end_pos, start_pos)
#
#
# if __name__ == '__main__':
#     plate_nums = int(input("请输入盘子的数量："))
#     range_list = list(range(1, plate_nums + 1))
#     range_list.sort(reverse=True)
#     A = (range_list, 'A')
#     B = ([], 'B')
#     C = ([], 'C')
#     hanoi(plate_nums, A, C, B)

def hanoi(n, ch1, ch2, ch3):
    if n == 1:
        print(ch1, '->', ch3)
    else:
        hanoi(n - 1, ch1, ch3, ch2)
        print(ch1, '->', ch3)
        hanoi(n - 1, ch2, ch1, ch3)


plate_nums = int(input("请输入盘子的数量："))
hanoi(plate_nums, 'A', 'B', 'C')