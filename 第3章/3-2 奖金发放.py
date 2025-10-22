"""
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""
profit = float(input("请输入当月利润，单位为元："))
bonus = 0  # 奖金
if profit <= 100000:
    bonus = 10 * 0.1
elif 100000 < profit <= 200000:
    bonus = 100000 * 0.1 + (profit - 100000) * 0.075
elif 200000 < profit <= 400000:
    bonus = round(100000 * 0.1 + 100000 * 0.075 +
                  (profit - 200000) * 0.05)
elif 400000 < profit <= 600000:
    bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + \
            (profit - 400000) * 0.03
elif 600000 < profit <= 1000000:
    bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + \
            200000 * 0.03 + (profit - 600000) * 0.015
elif profit > 1000000:
    bonus = 100000 * 0.1 + 100000 * 0.075 + \
            200000 * 0.05 + 200000 * 0.03 + \
            400000 * 0.015 + (profit - 1000000) * 0.015
print('当月应发放奖金总数为%s元' % bonus)

# i = float(input('请输入利润：'))
# bonus = 0
# profit = (100000, 200000, 400000, 600000, 1000000,)
# royalty_rate = (0.1, 0.075, 0.05, 0.03, 0.015, 0.01)
# if i >= profit[4]:
#     bonus += (i-profit[4]) * royalty_rate[5]
#     i = profit[4]
# if profit[3] < i <= profit[4]:
#     bonus += (i-profit[3]) * royalty_rate[4]
#     i = profit[3]
# if profit[2] < i <= profit[3]:
#     bonus += (i - profit[2]) * royalty_rate[3]
#     i = profit[2]
# if profit[1] < i <= profit[2]:
#     bonus += (i - profit[1]) * royalty_rate[2]
#     i = profit[1]
# if profit[0] < i <= profit[1]:
#     bonus += (i - profit[0]) * royalty_rate[1]
#     i = profit[0]
# if i <= profit[0]:
#     bonus += i * royalty_rate[0]
# print('应发奖金%.2f元' % bonus)