"""
帮一家快递点开发一个快递价格计费系统，业务如下：
提示用户输入：1.重量。2.地区编号
首重 3公斤
3公斤以内
编号01：华东地区 13元  华南地区 12元  华北地区 14元
3公斤以外
       华东地区3元/kg  华南地区 2元/kg  华北地区4元/kg

"""

# weight = int(input("请输入快递重量："))
weight = float(input("请输入快递重量："))
print('编号01：华东地区 编号02：华南地区 编号03：华北地区')
place = input("请输入地区编号：")
if weight <= 2:
    if place == '01':
        print('快递费为13元')
    elif place == '02':
        print('快递费12元')
    elif place == '03':
        print('快递费14元')
else:
    excess_weight = weight - 2
    if place == '01':
        many = excess_weight * 3 + 13
        print('快递费为%.1f元' % many)
    elif place == '02':
        many = excess_weight * 2 + 12
        print('快递费为%.1f元' % many)
    elif place == '03':
        many = excess_weight * 4 + 14
        print('快递费为%.1f元' % many)
