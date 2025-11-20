#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python字典(dict)练习题集
适用于初学者的由浅入深练习
"""

# ====================================================================
# 第一部分：字典基础概念和创建方法
# ====================================================================
print("=" * 60)
print("第一部分：字典基础概念和创建方法")
print("=" * 60)

# 练习1-1：创建一个包含个人基本信息的字典
print("\n练习1-1：创建一个包含个人基本信息的字典")
print("""
上下文：创建一个表示学生信息的字典，包含姓名、年龄、所在城市三个字段。
要求：
- 字典名为student
- 姓名字段为"name"，值为"张三"
- 年龄字段为"age"，值为20
- 所在城市字段为"city"，值为"北京"
""")

# 用户需要完成的代码
print("请完成以下代码：")
print("# student = {...}")
print("# print(student)")
print("\n预期输出：")
print("{'name': '张三', 'age': 20, 'city': '北京'}")


# 练习1-2：使用dict()构造函数创建字典
print("\n" + "-" * 60)
print("练习1-2：使用dict()构造函数创建字典")
print("""
上下文：使用dict()构造函数创建一个表示商品信息的字典。
要求：
- 使用关键字参数创建字典
- 字典名为product
- 包含商品名称、价格和库存三个字段
- 商品名称为"laptop"，价格为5999.99，库存为50
""")

# 用户需要完成的代码
print("请完成以下代码：")
print("# product = dict(...)")
print("# print(product)")
print("\n预期输出：")
print("{'laptop': 5999.99, 'price': 5999.99, 'stock': 50}")


# 练习1-3：使用zip函数和列表创建字典
print("\n" + "-" * 60)
print("练习1-3：使用zip函数和列表创建字典")
print("""
上下文：有两个列表，一个包含课程名称，另一个包含对应的分数，
需要将它们组合成一个字典，其中课程名称为键，分数为值。
""")

# 已提供的代码
courses = ['math', 'english', 'science', 'history']
scores = [85, 92, 78, 88]

# 用户需要完成的代码
print("请完成以下代码：")
print("# courses = ['math', 'english', 'science', 'history']")
print("# scores = [85, 92, 78, 88]")
print("# course_scores = dict(...)")
print("# print(course_scores)")
print("\n预期输出：")
print("{'math': 85, 'english': 92, 'science': 78, 'history': 88}")


# ====================================================================
# 第二部分：字典访问和修改操作
# ====================================================================
print("\n" + "=" * 60)
print("第二部分：字典访问和修改操作")
print("=" * 60)

# 练习2-1：使用方括号访问字典元素
print("\n练习2-1：使用方括号访问字典元素")
print("""
上下文：有一个表示书籍信息的字典，需要获取其中的特定信息。
""")

# 已提供的代码
book = {"title": "Python编程入门", "author": "李老师", "price": 68.5, "rating": 4.8}

# 用户需要完成的代码
print("请完成以下代码：")
print("# book = {\"title\": \"Python编程入门\", \"author\": \"李老师\", \"price\": 68.5, \"rating\": 4.8}")
print("# title = ...")
print("# price = ...")
print("# print(f'书名: {title}, 价格: {price}元')")
print("\n预期输出：")
print("书名: Python编程入门, 价格: 68.5元")


# 练习2-2：使用get()方法安全访问字典
print("\n" + "-" * 60)
print("练习2-2：使用get()方法安全访问字典")
print("""
上下文：有一个表示用户信息的字典，但某些用户可能没有所有字段，
需要使用get()方法安全地获取信息，避免KeyError异常。
""")

# 已提供的代码
user = {"username": "zhangsan", "email": "zhangsan@example.com", "age": 25}

# 用户需要完成的代码
print("请完成以下代码：")
print("# user = {\"username\": \"zhangsan\", \"email\": \"zhangsan@example.com\", \"age\": 25}")
print("# username = user.get(...)")
print("# phone = user.get(...)")  # 这个键不存在，需要提供默认值
print("# print(f'用户名: {username}, 电话: {phone}')")
print("\n预期输出：")
print("用户名: zhangsan, 电话: 未提供")


# 练习2-3：修改字典元素和添加新键值对
print("\n" + "-" * 60)
print("练习2-3：修改字典元素和添加新键值对")
print("""
上下文：有一个表示商品信息的字典，需要更新价格和添加新的库存信息。
""")

# 已提供的代码
product = {"name": "智能手机", "brand": "小米", "price": 2999.0, "color": "黑色"}

# 用户需要完成的代码
print("请完成以下代码：")
print("# product = {\"name\": \"智能手机\", \"brand\": \"小米\", \"price\": 2999.0, \"color\": \"黑色\"}")
print("# # 修改价格为2599.0")
print("# product[...] = ...")
print("# # 添加库存信息，键为'stock'，值为100")
print("# product[...] = ...")
print("# print(product)")
print("\n预期输出：")
print("{'name': '智能手机', 'brand': '小米', 'price': 2599.0, 'color': '黑色', 'stock': 100}")


# ====================================================================
# 第三部分：字典方法和内置函数
# ====================================================================
print("\n" + "=" * 60)
print("第三部分：字典方法和内置函数")
print("=" * 60)

# 练习3-1：使用keys()、values()和items()方法
print("\n练习3-1：使用keys()、values()和items()方法")
print("""
上下文：有一个表示班级学生成绩的字典，需要分别获取所有学生姓名、
所有成绩以及学生姓名和成绩的对应关系。
""")

# 已提供的代码
scores = {"张三": 85, "李四": 92, "王五": 78, "赵六": 90}

# 用户需要完成的代码
print("请完成以下代码：")
print("# scores = {\"张三\": 85, \"李四\": 92, \"王五\": 78, \"赵六\": 90}")
print("# students = list(...)")  # 获取所有学生姓名
print("# all_scores = list(...)")  # 获取所有成绩
print("# student_score_pairs = list(...)")  # 获取学生和成绩的对应关系
print("# print(f'学生列表: {students}')")
print("# print(f'成绩列表: {all_scores}')")
print("# print(f'学生-成绩对应关系: {student_score_pairs}')")
print("\n预期输出：")
print("学生列表: ['张三', '李四', '王五', '赵六']")
print("成绩列表: [85, 92, 78, 90]")
print("学生-成绩对应关系: [('张三', 85), ('李四', 92), ('王五', 78), ('赵六', 90)]")


# 练习3-2：使用pop()和popitem()方法删除元素
print("\n" + "-" * 60)
print("练习3-2：使用pop()和popitem()方法删除元素")
print("""
上下文：有一个表示购物车的字典，需要删除特定商品以及最后添加的商品。
""")

# 已提供的代码
shopping_cart = {"苹果": 15.5, "香蕉": 8.5, "牛奶": 6.5, "面包": 12.0}

# 用户需要完成的代码
print("请完成以下代码：")
print("# shopping_cart = {\"苹果\": 15.5, \"香蕉\": 8.5, \"牛奶\": 6.5, \"面包\": 12.0}")
print("# # 删除'香蕉'并获取其价格")
print("# banana_price = shopping_cart.pop(...)")
print("# # 删除最后添加的商品")
print("# last_item = shopping_cart.popitem()")
print("# print(f'香蕉价格: {banana_price}元')")
print("# print(f'最后删除的商品: {last_item}')")
print("# print(f'剩余购物车: {shopping_cart}')")
print("\n预期输出：")
print("香蕉价格: 8.5元")
print("最后删除的商品: ('面包', 12.0)")
print("剩余购物车: {'苹果': 15.5, '牛奶': 6.5}")


# 练习3-3：使用update()方法更新字典
print("\n" + "-" * 60)
print("练习3-3：使用update()方法更新字典")
print("""
上下文：有一个表示配置信息的字典，需要更新多个配置项。
""")

# 已提供的代码
config = {"host": "localhost", "port": 8000, "debug": False}

# 用户需要完成的代码
print("请完成以下代码：")
print("# config = {\"host\": \"localhost\", \"port\": 8000, \"debug\": False}")
print("# # 使用字典更新配置")
print("# config.update(...)")  # 更新port为9000，debug为True
print("# # 使用关键字参数添加新配置")
print("# config.update(...)")  # 添加username为'admin'
print("# print(config)")
print("\n预期输出：")
print("{'host': 'localhost', 'port': 9000, 'debug': True, 'username': 'admin'}")


# ====================================================================
# 第四部分：字典遍历和常用操作
# ====================================================================
print("\n" + "=" * 60)
print("第四部分：字典遍历和常用操作")
print("=" * 60)

# 练习4-1：遍历字典的键值对
print("\n练习4-1：遍历字典的键值对")
print("""
上下文：有一个表示图书馆图书信息的字典，需要遍历并打印每本书的信息。
""")

# 已提供的代码
library = {
    "Python入门": {"author": "张三", "year": 2022},
    "Java基础": {"author": "李四", "year": 2021},
    "数据结构": {"author": "王五", "year": 2023}
}

# 用户需要完成的代码
print("请完成以下代码：")
print("# library = {")
print("#     \"Python入门\": {\"author\": \"张三\", \"year\": 2022},")
print("#     \"Java基础\": {\"author\": \"李四\", \"year\": 2021},")
print("#     \"数据结构\": {\"author\": \"王五\", \"year\": 2023}")
print("# }")
print("# print('图书馆图书信息：')")
print("# for ... in library.items():")
print("#     print(f'书名: {book_title}, 作者: {book_info["author"]}, 出版年份: {book_info["year"]}')")
print("\n预期输出：")
print("图书馆图书信息：")
print("书名: Python入门, 作者: 张三, 出版年份: 2022")
print("书名: Java基础, 作者: 李四, 出版年份: 2021")
print("书名: 数据结构, 作者: 王五, 出版年份: 2023")


# 练习4-2：字典合并操作
print("\n" + "-" * 60)
print("练习4-2：字典合并操作")
print("""
上下文：有两个表示学生信息的字典，需要将它们合并成一个完整的学生信息字典。
""")

# 已提供的代码
student_basic = {"name": "张三", "age": 20, "student_id": "2023001"}
student_scores = {"math": 85, "english": 92, "science": 78}

# 用户需要完成的代码
print("请完成以下代码：")
print("# student_basic = {\"name\": \"张三\", \"age\": 20, \"student_id\": \"2023001\"}")
print("# student_scores = {\"math\": 85, \"english\": 92, \"science\": 78}")
print("# # 方法1：使用update()方法合并")
print("# student_info1 = student_basic.copy()")
print("# student_info1.update(...)")
print("# ")
print("# # 方法2：使用字典解包操作符合并")
print("# student_info2 = {**..., **...}")
print("# ")
print("# print(f'方法1合并结果: {student_info1}')")
print("# print(f'方法2合并结果: {student_info2}')")
print("\n预期输出：")
print("方法1合并结果: {'name': '张三', 'age': 20, 'student_id': '2023001', 'math': 85, 'english': 92, 'science': 78}")
print("方法2合并结果: {'name': '张三', 'age': 20, 'student_id': '2023001', 'math': 85, 'english': 92, 'science': 78}")


# 练习4-3：使用字典进行简单统计
print("\n" + "-" * 60)
print("练习4-3：使用字典进行简单统计")
print("""
上下文：有一个字符串列表，需要统计每个字符出现的次数。
""")

# 已提供的代码
words = ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]

# 用户需要完成的代码
print("请完成以下代码：")
print("# words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'grape']")
print("# word_count = {}")
print("# for word in words:")
print("#     # 使用get()方法统计")
print("#     word_count[word] = word_count.get(..., ...) + ...")
print("# ")
print("# print('单词统计结果：')")
print("# for word, count in word_count.items():")
print("#     print(f'{word}: {count}次')")
print("\n预期输出：")
print("单词统计结果：")
print("apple: 3次")
print("banana: 2次")
print("orange: 1次")
print("grape: 1次")


# ====================================================================
# 第五部分：字典高级特性
# ====================================================================
print("\n" + "=" * 60)
print("第五部分：字典高级特性")
print("=" * 60)

# 练习5-1：操作嵌套字典
print("\n练习5-1：操作嵌套字典")
print("""
上下文：有一个表示公司部门和员工信息的嵌套字典，需要访问和修改特定员工的信息。
""")

# 已提供的代码
company = {
    "技术部": {
        "张三": {"position": "工程师", "salary": 15000},
        "李四": {"position": "高级工程师", "salary": 20000}
    },
    "市场部": {
        "王五": {"position": "专员", "salary": 12000},
        "赵六": {"position": "经理", "salary": 25000}
    }
}

# 用户需要完成的代码
print("请完成以下代码：")
print("# company = {...}")
print("# # 获取李四的职位")
print("# lisi_position = company[...]\n")
print("# # 修改王五的薪资为13000")
print("# company[...] = ...\n")
print("# # 在技术部添加新员工'钱七'")
print("# company['技术部'][...] = {"position": "实习生", "salary": 5000}\n")
print("# print(f'李四的职位: {lisi_position}')")
print("# print(f'王五的薪资: {company["市场部"]["王五"]["salary"]}')")
print("# print(f'技术部所有员工: {list(company["技术部"].keys())}')")
print("\n预期输出：")
print("李四的职位: 高级工程师")
print("王五的薪资: 13000")
print("技术部所有员工: ['张三', '李四', '钱七']")


# 练习5-2：使用字典推导式创建字典
print("\n" + "-" * 60)
print("练习5-2：使用字典推导式创建字典")
print("""
上下文：需要创建一些特殊的字典，使用字典推导式可以使代码更简洁。
""")

# 用户需要完成的代码
print("请完成以下代码：")
print("# # 练习5-2-1：创建一个数字到其立方的字典（1到5）")
print("# cubes = {x: ... for x in range(1, 6)}")
print("# print(f'数字到立方的字典: {cubes}')\n")
print("# # 练习5-2-2：创建一个只包含偶数的平方字典（1到10）")
print("# even_squares = {x: ... for x in range(1, 11) if ...}")
print("# print(f'偶数的平方字典: {even_squares}')\n")
print("# # 练习5-2-3：将字符串转换为字符到ASCII码的字典")
print("# text = 'Python'")
print("# ascii_dict = {...: ... for char in text}")
print("# print(f'字符到ASCII码的字典: {ascii_dict}')")
print("\n预期输出：")
print("数字到立方的字典: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}")
print("偶数的平方字典: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}")
print("字符到ASCII码的字典: {'P': 80, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}")


# 练习5-3：嵌套字典推导式
print("\n" + "-" * 60)
print("练习5-3：嵌套字典推导式")
print("""
上下文：有一个二维列表（矩阵），需要将其转换为嵌套字典形式，
其中外层字典的键是行号，内层字典的键是列号。
""")

# 已提供的代码
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 用户需要完成的代码
print("请完成以下代码：")
print("# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
print("# # 使用嵌套字典推导式转换矩阵")
print("# matrix_dict = {f'row_{i}': {f'col_{j}': ... for j, value in enumerate(row)} for i, row in enumerate(matrix)}")
print("# ")
print("# # 打印转换后的字典")
print("# print('转换后的矩阵字典：')")
print("# for row_key, row_value in matrix_dict.items():")
print("#     print(f'{row_key}: {row_value}')")
print("\n预期输出：")
print("转换后的矩阵字典：")
print("row_0: {'col_0': 1, 'col_1': 2, 'col_2': 3}")
print("row_1: {'col_0': 4, 'col_1': 5, 'col_2': 6}")
print("row_2: {'col_0': 7, 'col_1': 8, 'col_2': 9}")


# ====================================================================
# 第六部分：字典最佳实践和常见错误
# ====================================================================
print("\n" + "=" * 60)
print("第六部分：字典最佳实践和常见错误")
print("=" * 60)

# 练习6-1：使用get()方法安全访问
print("\n练习6-1：使用get()方法安全访问")
print("""
上下文：有一个表示配置信息的字典，但某些配置项可能不存在，
需要使用get()方法安全地获取配置，避免KeyError异常。
""")

# 已提供的代码
config = {
    "host": "localhost",
    "port": 8000,
    "username": "admin"
    # password配置项可能不存在
}

# 用户需要完成的代码
print("请完成以下代码：")
print("# config = {")
print("#     \"host\": \"localhost\",")
print("#     \"port\": 8000,")
print("#     \"username\": \"admin\"")
print("#     # password配置项可能不存在")
print("# }")
print("# ")
print("# # 使用方括号访问存在的配置")
print("# host = config['host']")
print("# ")
print("# # 使用get()方法访问可能不存在的配置")
print("# password = config.get(...)")  # 提供默认值"guest"
print("# ")
print("# print(f'连接到 {host}:{config["port"]}')")
print("# print(f'用户名: {config["username"]}, 密码: {password}')")
print("\n预期输出：")
print("连接到 localhost:8000")
print("用户名: admin, 密码: guest")


# 练习6-2：避免使用可变类型作为字典键
print("\n" + "-" * 60)
print("练习6-2：避免使用可变类型作为字典键")
print("""
上下文：需要创建一个字典来存储不同水果的价格，但要确保使用不可变类型作为键。
""")

# 用户需要完成的代码
print("请完成以下代码：")
print("# # 正确做法：使用字符串作为键")
print("# fruit_prices = {")
print("#     ...: 5.5,  # 苹果价格")
print("#     ...: 3.5,  # 香蕉价格")
print("#     ...: 8.0   # 橙子价格")
print("# }")
print("# print(f'水果价格字典: {fruit_prices}')")
print("# ")
print("# # 思考：为什么下面的代码会失败？")
print("# # mutable_key_dict = {[1, 2]: 'value'}  # 会引发TypeError")
print("# print('列表是可变类型，不能作为字典键！')")
print("\n预期输出：")
print("水果价格字典: {'苹果': 5.5, '香蕉': 3.5, '橙子': 8.0}")
print("列表是可变类型，不能作为字典键！")


# 练习6-3：避免在遍历字典时修改字典
print("\n" + "-" * 60)
print("练习6-3：避免在遍历字典时修改字典")
print("""
上下文：有一个表示学生成绩的字典，需要过滤掉不及格的成绩（低于60分），
但要避免在遍历字典时直接修改字典的错误做法。
""")

# 已提供的代码
scores = {"张三": 85, "李四": 58, "王五": 72, "赵六": 55, "钱七": 90}

# 用户需要完成的代码
print("请完成以下代码：")
print("# scores = {\"张三\": 85, \"李四\": 58, \"王五\": 72, \"赵六\": 55, \"钱七\": 90}")
print("# ")
print("# # 正确做法1：创建新字典只包含及格的成绩")
print("# passed_scores = {name: score for name, score in scores.items() if ...}")
print("# ")
print("# # 正确做法2：遍历字典的副本进行删除")
print("# scores_copy = scores.copy()")
print("# for name, score in scores_copy.items():")
print("#     if ...:")
print("#         del scores[name]")
print("# ")
print("# print(f'方法1-及格成绩: {passed_scores}')")
print("# print(f'方法2-过滤后成绩: {scores}')")
print("\n预期输出：")
print("方法1-及格成绩: {'张三': 85, '王五': 72, '钱七': 90}")
print("方法2-过滤后成绩: {'张三': 85, '王五': 72, '钱七': 90}")


print("\n" + "=" * 60)
print("Python字典练习题完成！")
print("请尝试完成所有练习题，巩固字典相关知识！")
print("=" * 60)