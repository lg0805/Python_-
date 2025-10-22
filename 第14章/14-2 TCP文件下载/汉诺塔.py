# def hanoi(n, ch1, ch2, ch3):
#     if n == 1:
#         print(ch1, '->', ch3)
#     else:
#         hanoi(n - 1, ch1, ch3, ch2)
#         print(ch1, '->', ch3)
#         hanoi(n - 1, ch2, ch1, ch3)
#
#
# plate_nums = int(input("请输入盘子的数量："))
# hanoi(plate_nums, 'A', 'B', 'C')

def hanoi(num, start_pos, end_pos, mid_pillar):
    if num == 1:  # 边界条件
        plate = start_pos[0].pop()
        print('移动 ' + str(plate) + ' 从 ' + start_pos[1] + ' 到 ' + end_pos[1])
        end_pos[0].append(plate)
    else:
        hanoi(num - 1, start_pos, mid_pillar, end_pos)
        plate = start_pos[0].pop()
        print('移动 ' + str(plate) + ' 从 ' + start_pos[1] + ' 到 ' + end_pos[1])
        end_pos[0].append(plate)
        hanoi(num - 1, mid_pillar, end_pos, start_pos)


if __name__ == '__main__':
    A = ([3, 2, 1], 'A')
    B = ([], 'B')
    C = ([], 'C')
    hanoi(len(A[0]), A, C, B)
