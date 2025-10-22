# 包含7和7的倍数小游戏（100以内）
# 1. 从1开始数数，遇到7或7的倍数时，拍手
# 2. 不包含7或7的倍数时，正常数数
# 3. 数到100结束游戏

count = 0
for i in range(1, 101):
    if i % 7 == 0 or '7' in str(i):
        print("拍手")
    else:
        print(i)
    count += 1
    print(f"当前数字是: {i}, 已经数了: {count} 次")
