#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python字典(dict)学习教程
适用于初学者的系统学习指南
"""

# ====================================================================
# 第一部分：字典基础概念
# ====================================================================
print("=" * 50)
print("第一部分：字典基础概念")
print("=" * 50)

"""
字典是Python中一种非常重要的数据结构，它是一个无序的键值对(key-value pair)集合。
特点：
1. 字典中的键(key)必须是不可变类型（如字符串、数字或元组）
2. 字典中的值(value)可以是任何类型（包括列表、字典等）
3. 字典是可变的，可以添加、修改和删除键值对
4. 字典在Python 3.7+中保持插入顺序
5. 字典查找操作的时间复杂度为O(1)，非常高效
"""

# ====================================================================
# 第二部分：字典的创建
# ====================================================================
print("\n" + "=" * 50)
print("第二部分：字典的创建")
print("=" * 50)

# 方法1：使用大括号创建空字典
empty_dict = {}
print("1. 创建空字典:")
print(f"   empty_dict = {empty_dict}")
print(f"   类型: {type(empty_dict)}")

# 方法2：使用大括号创建带有初始键值对的字典
person = {"name": "张三", "age": 25, "city": "北京"}
print("\n2. 创建带有初始键值对的字典:")
print(f"   person = {person}")

# 方法3：使用dict()构造函数创建字典
# 3.1 使用关键字参数
student = dict(name="李四", age=20, school="北京大学")
print("\n3.1 使用dict()构造函数和关键字参数:")
print(f"   student = {student}")

# 3.2 使用可迭代对象（如列表的列表或元组的元组）
items = [("fruit", "apple"), ("color", "red"), ("price", 10)]
fruit_dict = dict(items)
print("\n3.2 使用可迭代对象:")
print(f"   items = {items}")
print(f"   fruit_dict = {fruit_dict}")

# 3.3 从两个列表创建字典（使用zip函数）
keys = ["a", "b", "c"]
values = [1, 2, 3]
# zip函数将两个列表中对应位置的元素组合成元组
# 然后dict()构造函数将这些元组转换为键值对
zip_dict = dict(zip(keys, values))
print("\n3.3 使用zip函数从两个列表创建字典:")
print(f"   keys = {keys}")
print(f"   values = {values}")
print(f"   zip_dict = {zip_dict}")

# 扩展：zip函数的工作原理
print("\n   扩展：zip函数的工作原理")
print("   # zip(keys, values) 返回可迭代的zip对象，包含元组 ('a', 1), ('b', 2), ('c', 3)")
zipped_items = list(zip(keys, values))
print(f"   list(zip(keys, values)) = {zipped_items}")

# 扩展：列表长度不匹配的情况
print("\n   扩展：列表长度不匹配的情况")
short_keys = ["a", "b"]
long_values = [1, 2, 3, 4]
mismatch_dict = dict(zip(short_keys, long_values))
print(f"   short_keys = {short_keys}")
print(f"   long_values = {long_values}")
print(f"   长度不匹配时创建的字典: {mismatch_dict}  # 注意：只匹配到较短列表的长度")

# 扩展：使用*解包zip对象
try:
    # 尝试解包zip对象
    dict_keys, dict_values = zip(*zip(keys, values))
    print(f"\n   扩展：使用*解包zip对象重新获取原列表")
    print(f"   dict_keys = {dict_keys}")
    print(f"   dict_values = {dict_values}")
except ValueError:
    # 如果解包失败，提供替代的解释
    print("   注意：可以使用zip(*zip(keys, values))将键值对重新解包为两个元组")

# 方法4：使用字典推导式（高级特性，后面会详细介绍）
square_dict = {x: x*x for x in range(1, 6)}
print("\n4. 使用字典推导式:")
print(f"   square_dict = {square_dict}")

# ====================================================================
# 第三部分：访问字典中的元素
# ====================================================================
print("\n" + "=" * 50)
print("第三部分：访问字典中的元素")
print("=" * 50)

# 示例字典
book = {"title": "Python编程", "author": "Eric", "year": 2022, "price": 99.0}
print(f"示例字典: book = {book}")

# 方法1：使用方括号和键访问
print("\n1. 使用方括号和键访问:")
title = book["title"]
author = book["author"]
print(f"   book['title'] = {title}")
print(f"   book['author'] = {author}")

# 注意：如果键不存在，会引发KeyError异常
print("\n   注意：如果尝试访问不存在的键，会引发KeyError异常")
print("   # book['publisher']  # 这行会引发KeyError")

# 方法2：使用get()方法访问（更安全的方式）
print("\n2. 使用get()方法访问:")
year = book.get("year")
publisher = book.get("publisher")  # 键不存在时返回None
print(f"   book.get('year') = {year}")
print(f"   book.get('publisher') = {publisher}")

# 可以为get()方法提供默认值
publisher = book.get("publisher", "未知")
print(f"   book.get('publisher', '未知') = {publisher}")

# 方法3：使用setdefault()方法访问（如果键不存在，会添加键值对并返回默认值）
print("\n3. 使用setdefault()方法访问:")
rating = book.setdefault("rating", 5.0)
print(f"   book.setdefault('rating', 5.0) = {rating}")
print(f"   更新后的book = {book}")

# ====================================================================
# 第四部分：修改字典
# ====================================================================
print("\n" + "=" * 50)
print("第四部分：修改字典")
print("=" * 50)

# 示例字典
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(f"原始字典: car = {car}")

# 1. 添加新的键值对
print("\n1. 添加新的键值对:")
car["color"] = "red"
print(f"   添加color后: car = {car}")

# 2. 修改现有键的值
print("\n2. 修改现有键的值:")
car["year"] = 2023
print(f"   修改year后: car = {car}")

# 3. 使用update()方法添加或更新多个键值对
print("\n3. 使用update()方法添加或更新多个键值对:")
car.update({"price": 150000, "mileage": 0})
print(f"   update后: car = {car}")

# 也可以使用关键字参数
car.update(warranty="3年", service="免费首保")
print(f"   使用关键字参数update后: car = {car}")

# 4. 删除键值对
print("\n4. 删除键值对:")

# 4.1 使用del语句
print("\n4.1 使用del语句删除:")
del car["mileage"]
print(f"   删除mileage后: car = {car}")

# 4.2 使用pop()方法删除（并返回值）
print("\n4.2 使用pop()方法删除（并返回值）:")
warranty = car.pop("warranty")
print(f"   弹出的warranty值: {warranty}")
print(f"   删除warranty后: car = {car}")

# 可以为pop()提供默认值，当键不存在时返回
insurance = car.pop("insurance", "未购买")
print(f"   弹出不存在的insurance键，返回默认值: {insurance}")

# 4.3 使用popitem()方法删除最后插入的键值对（返回键值对）
print("\n4.3 使用popitem()方法删除最后插入的键值对:")
last_item = car.popitem()
print(f"   弹出的最后一项: {last_item}")
print(f"   删除后: car = {car}")

# 4.4 使用clear()方法清空字典
print("\n4.4 使用clear()方法清空字典:")
car.clear()
print(f"   清空后: car = {car}")

print("\n" + "=" * 50)
print("字典基础操作学习完成！")
print("=" * 50)

# ====================================================================
# 第五部分：字典方法和内置函数
# ====================================================================
print("\n" + "=" * 50)
print("第五部分：字典方法和内置函数")
print("=" * 50)

# 示例字典
computer = {"brand": "Dell", "model": "XPS", "ram": "16GB", "storage": "512GB", "price": 9999}
print(f"示例字典: computer = {computer}")

# 1. keys() 方法 - 返回字典中所有的键
print("\n1. keys() 方法 - 返回字典中所有的键:")
keys = computer.keys()
print(f"   computer.keys() = {keys}")
print(f"   转换为列表: {list(keys)}")

# 2. values() 方法 - 返回字典中所有的值
print("\n2. values() 方法 - 返回字典中所有的值:")
values = computer.values()
print(f"   computer.values() = {values}")
print(f"   转换为列表: {list(values)}")

# 3. items() 方法 - 返回字典中所有的键值对（元组形式）
print("\n3. items() 方法 - 返回字典中所有的键值对:")
items = computer.items()
print(f"   computer.items() = {items}")
print(f"   转换为列表: {list(items)}")

# 4. copy() 方法 - 创建字典的浅拷贝
print("\n4. copy() 方法 - 创建字典的浅拷贝:")
computer_copy = computer.copy()
print(f"   原始字典: {computer}")
print(f"   复制的字典: {computer_copy}")

# 修改复制的字典，不会影响原始字典
computer_copy["price"] = 8999
print(f"   修改复制字典后的原始字典: {computer}")
print(f"   修改后的复制字典: {computer_copy}")

# 5. fromkeys() 方法 - 创建新字典，指定键和默认值
print("\n5. fromkeys() 方法 - 创建新字典:")
# 5.1 使用默认值None
new_keys = ["a", "b", "c"]
dict_from_keys = dict.fromkeys(new_keys)
print(f"   dict.fromkeys([\"a\", \"b\", \"c\"]) = {dict_from_keys}")

# 5.2 指定默认值
scores = dict.fromkeys(["math", "english", "science"], 0)
print(f"   dict.fromkeys([\"math\", \"english\", \"science\"], 0) = {scores}")

# 6. clear() 方法 - 清空字典
print("\n6. clear() 方法 - 清空字典:")
temp_dict = {"x": 1, "y": 2}
print(f"   清空前: {temp_dict}")
temp_dict.clear()
print(f"   清空后: {temp_dict}")

# 7. 内置函数 - 适用于字典
print("\n7. 内置函数 - 适用于字典:")

# 7.1 len() - 获取字典中键值对的数量
print("\n7.1 len() - 获取字典长度:")
print(f"   len(computer) = {len(computer)}")

# 7.2 in 和 not in - 检查键是否存在
print("\n7.2 in 和 not in - 检查键是否存在:")
print(f"   'brand' in computer: {'brand' in computer}")
print(f"   'color' in computer: {'color' in computer}")
print(f"   'color' not in computer: {'color' not in computer}")

# 7.3 sorted() - 对字典的键进行排序
print("\n7.3 sorted() - 对字典的键进行排序:")
sorted_keys = sorted(computer.keys())
print(f"   sorted(computer.keys()) = {sorted_keys}")

# 7.4 min() 和 max() - 获取字典中的最小和最大键
print("\n7.4 min() 和 max() - 获取最小和最大键:")
print(f"   min(computer.keys()) = {min(computer.keys())}")
print(f"   max(computer.keys()) = {max(computer.keys())}")

# 7.5 str() - 将字典转换为字符串
print("\n7.5 str() - 将字典转换为字符串:")
dict_str = str(computer)
print(f"   str(computer) = {dict_str}")
print(f"   类型: {type(dict_str)}")

# 7.6 all() 和 any() - 对字典的键进行逻辑判断
print("\n7.6 all() 和 any() - 对字典的键进行逻辑判断:")
# all() - 如果所有键都为True（非空、非零等），返回True
# any() - 如果至少有一个键为True，返回True
print(f"   all(computer) = {all(computer)}")
print(f"   any(computer) = {any(computer)}")

# 空字符串作为键时的示例
empty_key_dict = {"": "empty key", "a": "value"}
print(f"   有空字符串键的字典: {empty_key_dict}")
print(f"   all(empty_key_dict) = {all(empty_key_dict)}  # 因为有空字符串键")
print(f"   any(empty_key_dict) = {any(empty_key_dict)}")

print("\n" + "=" * 50)
print("字典方法和内置函数学习完成！")
print("=" * 50)

# ====================================================================
# 第六部分：字典遍历和常用操作
# ====================================================================
print("\n" + "=" * 50)
print("第六部分：字典遍历和常用操作")
print("=" * 50)

# 示例字典
phone_book = {"张三": "13800138001", "李四": "13900139001", "王五": "13700137001", "赵六": "13600136001"}
print(f"示例字典: phone_book = {phone_book}")

# 1. 遍历字典的键
print("\n1. 遍历字典的键:")
print("   方法1：直接遍历字典（默认遍历键）")
for name in phone_book:
    print(f"   姓名: {name}")

print("\n   方法2：使用keys()方法遍历键")
for name in phone_book.keys():
    print(f"   姓名: {name}")

# 2. 遍历字典的值
print("\n2. 遍历字典的值:")
print("   使用values()方法遍历值")
for phone in phone_book.values():
    print(f"   电话: {phone}")

# 3. 遍历字典的键值对
print("\n3. 遍历字典的键值对:")
print("   使用items()方法遍历键值对")
for name, phone in phone_book.items():
    print(f"   姓名: {name}, 电话: {phone}")

# 4. 常用操作示例
print("\n4. 常用操作示例:")

# 4.1 字典合并
print("\n4.1 字典合并:")
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(f"   dict1 = {dict1}")
print(f"   dict2 = {dict2}")

# 方法1：使用update()方法（会修改原字典）
merged_dict1 = dict1.copy()  # 复制原字典以避免修改
merged_dict1.update(dict2)
print(f"   使用update()合并: {merged_dict1}")

# 方法2：使用字典解包操作符 **（Python 3.5+）
dict1 = {"a": 1, "b": 2}  # 重新设置dict1，因为上面的操作可能修改了它
dict2 = {"b": 3, "c": 4}
merged_dict2 = {**dict1, **dict2}
print(f"   使用**解包操作符合并: {merged_dict2}")

# 方法3：使用字典的 union 操作（Python 3.9+）
# merged_dict3 = dict1 | dict2

# 4.2 字典比较
print("\n4.2 字典比较:")
dict_a = {"a": 1, "b": 2}
dict_b = {"b": 2, "a": 1}  # 顺序不同但内容相同
dict_c = {"a": 1, "c": 3}  # 内容不同
print(f"   dict_a = {dict_a}")
print(f"   dict_b = {dict_b}")
print(f"   dict_c = {dict_c}")
print(f"   dict_a == dict_b: {dict_a == dict_b}  # 字典比较不考虑顺序")
print(f"   dict_a == dict_c: {dict_a == dict_c}")

# 4.3 字典转换为其他数据类型
print("\n4.3 字典转换为其他数据类型:")

# 转换为列表
print("   转换为列表:")
keys_list = list(phone_book.keys())
values_list = list(phone_book.values())
items_list = list(phone_book.items())
print(f"   键列表: {keys_list}")
print(f"   值列表: {values_list}")
print(f"   键值对列表: {items_list}")

# 转换为元组
print("   转换为元组:")
keys_tuple = tuple(phone_book.keys())
values_tuple = tuple(phone_book.values())
items_tuple = tuple(phone_book.items())
print(f"   键元组: {keys_tuple}")
print(f"   值元组: {values_tuple}")
print(f"   键值对元组: {items_tuple}")

# 4.4 计算字典中值的总和、最大值、最小值等
print("\n4.4 计算字典中值的总和、最大值、最小值等:")
scores = {"math": 85, "english": 92, "science": 78, "history": 88}
print(f"   成绩字典: {scores}")
print(f"   成绩总和: {sum(scores.values())}")
print(f"   最高成绩: {max(scores.values())}")
print(f"   最低成绩: {min(scores.values())}")
print(f"   平均成绩: {sum(scores.values()) / len(scores) if scores else 0}")

# 找出最高分的科目
max_score = max(scores.values())
max_subject = [subject for subject, score in scores.items() if score == max_score]
print(f"   最高分科目: {max_subject}")

# 4.5 使用字典进行简单的统计
print("\n4.5 使用字典进行简单的统计:")
words = ["apple", "banana", "apple", "orange", "banana", "apple", "grape", "apple"]
word_count = {}

# 统计单词出现次数
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"   原始单词列表: {words}")
print(f"   单词统计结果: {word_count}")

# 或者使用更简洁的方式（使用get方法）
word_count_alt = {}
for word in words:
    word_count_alt[word] = word_count_alt.get(word, 0) + 1

print(f"   使用get方法的统计结果: {word_count_alt}")

print("\n" + "=" * 50)
print("字典遍历和常用操作学习完成！")
print("=" * 50)

# ====================================================================
# 第七部分：字典高级特性
# ====================================================================
print("\n" + "=" * 50)
print("第七部分：字典高级特性")
print("=" * 50)

# 1. 嵌套字典
print("\n1. 嵌套字典 - 字典中包含字典:")

# 创建嵌套字典
students = {
    "张三": {
        "age": 20,
        "major": "计算机科学",
        "scores": {
            "math": 85,
            "english": 92,
            "programming": 95
        }
    },
    "李四": {
        "age": 21,
        "major": "电子工程",
        "scores": {
            "math": 90,
            "english": 88,
            "programming": 82
        }
    },
    "王五": {
        "age": 19,
        "major": "数学",
        "scores": {
            "math": 95,
            "english": 84,
            "programming": 78
        }
    }
}

print(f"嵌套字典示例: students = {...}  # 为简洁起见，未显示完整内容")

# 访问嵌套字典中的元素
print("\n   访问嵌套字典中的元素:")
# 获取张三的年龄
zhangsan_age = students["张三"]["age"]
print(f"   张三的年龄: {zhangsan_age}")

# 获取李四的编程成绩
lisi_programming = students["李四"]["scores"]["programming"]
print(f"   李四的编程成绩: {lisi_programming}")

# 修改嵌套字典中的元素
print("\n   修改嵌套字典中的元素:")
students["张三"]["scores"]["programming"] = 98
print(f"   修改后张三的编程成绩: {students['张三']['scores']['programming']}")

# 遍历嵌套字典
print("\n   遍历嵌套字典:")
for name, info in students.items():
    print(f"   学生: {name}")
    print(f"     年龄: {info['age']}")
    print(f"     专业: {info['major']}")
    print(f"     成绩:")
    for subject, score in info['scores'].items():
        print(f"       {subject}: {score}")

# 2. 字典推导式
print("\n2. 字典推导式 - 类似于列表推导式的简洁创建字典方式:")

# 2.1 基本字典推导式
print("\n2.1 基本字典推导式:")
# 创建一个数字到其平方的字典
squares = {x: x*x for x in range(1, 6)}
print(f"   数字到平方的字典: {squares}")

# 创建一个字母到ASCII码的字典
letters = {chr(c): c for c in range(65, 70)}  # A到E的ASCII码
print(f"   字母到ASCII码的字典: {letters}")

# 2.2 带条件的字典推导式
print("\n2.2 带条件的字典推导式:")
# 只包含偶数的平方
even_squares = {x: x*x for x in range(1, 11) if x % 2 == 0}
print(f"   偶数的平方字典: {even_squares}")

# 2.3 从其他字典创建新字典
print("\n2.3 从其他字典创建新字典:")
original_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

# 过滤并转换值
filtered_dict = {k: v*2 for k, v in original_dict.items() if v > 2}
print(f"   原始字典: {original_dict}")
print(f"   值大于2并乘以2的字典: {filtered_dict}")

# 键值对交换
reversed_dict = {v: k for k, v in original_dict.items()}
print(f"   键值交换后的字典: {reversed_dict}")

# 2.4 复杂字典推导式示例
print("\n2.4 复杂字典推导式示例:")
# 使用两个列表创建字典
keys = ["name", "age", "city"]
values = ["张三", 25, "北京"]
person_dict = {k: v for k, v in zip(keys, values)}
print(f"   使用zip创建的字典: {person_dict}")

# 嵌套字典推导式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_dict = {f"row_{i}": {f"col_{j}": value for j, value in enumerate(row)} for i, row in enumerate(matrix)}
print(f"   嵌套字典推导式结果: {matrix_dict}")

# 3. 特殊字典类型
print("\n3. 特殊字典类型:")

# 3.1 collections.defaultdict
print("\n3.1 collections.defaultdict - 带有默认值的字典:")
print("   需要导入collections模块")
# 示例：统计单词频率
print("   # 使用defaultdict统计单词频率的示例:")
print("   # from collections import defaultdict")
print("   # word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']")
print("   # word_counts = defaultdict(int)  # 默认值为0")
print("   # for word in word_list:")
print("   #     word_counts[word] += 1")

# 3.2 collections.OrderedDict
print("\n3.2 collections.OrderedDict - 保持插入顺序的字典:")
print("   在Python 3.7+中，普通字典也保持插入顺序，但OrderedDict提供额外的方法")
print("   # 需要导入collections模块")
print("   # from collections import OrderedDict")
print("   # ordered_dict = OrderedDict()")
print("   # ordered_dict['c'] = 3")
print("   # ordered_dict['a'] = 1")
print("   # ordered_dict['b'] = 2")

# 3.3 collections.Counter
print("\n3.3 collections.Counter - 用于计数的字典子类:")
print("   # 需要导入collections模块")
print("   # from collections import Counter")
print("   # word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']")
print("   # counter = Counter(word_list)")
print("   # print(counter)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})")

# 4. 字典的哈希性和不可变类型
print("\n4. 字典的哈希性和不可变类型:")
print("   字典的键必须是不可变类型（可哈希的），如字符串、数字、元组等")
print("   值可以是任何类型，包括可变类型")

# 示例：使用元组作为键
print("\n   示例：使用元组作为键:")
point_info = {}
point_info[(1, 2)] = "这是点(1,2)"
point_info[(3, 4)] = "这是点(3,4)"
print(f"   使用元组作为键的字典: {point_info}")
print(f"   获取点(1,2)的信息: {point_info[(1, 2)]}")

# 注意：列表不能作为字典的键，因为它是可变的
print("\n   注意：列表不能作为字典的键，因为它是可变的")
print("   # 以下代码会引发TypeError")
print("   # invalid_dict = {[1, 2]: 'value'}  # TypeError: unhashable type: 'list'")

print("\n" + "=" * 50)
print("字典高级特性学习完成！")
print("=" * 50)

# ====================================================================
# 第八部分：字典最佳实践和常见错误
# ====================================================================
print("\n" + "=" * 50)
print("第八部分：字典最佳实践和常见错误")
print("=" * 50)

# 1. 字典最佳实践
print("\n1. 字典最佳实践:")

# 1.1 使用get()方法安全地访问可能不存在的键
print("\n1.1 使用get()方法安全地访问可能不存在的键:")
print("   # 推荐的方式")
person_data = {"name": "张三", "age": 25}
# 不推荐：可能引发KeyError
print("   # address = person_data['address']  # 如果键不存在会引发KeyError")
# 推荐：使用get()方法并提供默认值
address = person_data.get("address", "未知地址")
print(f"   address = person_data.get('address', '未知地址')  # 更安全")
print(f"   结果: {address}")

# 1.2 使用in操作符检查键是否存在
print("\n1.2 使用in操作符检查键是否存在:")
if "email" not in person_data:
    person_data["email"] = "example@example.com"
print(f"   检查并添加后: {person_data}")

# 1.3 使用字典推导式创建新字典
print("\n1.3 使用字典推导式创建新字典:")
print("   # 推荐：简洁且高效")
numbers = range(1, 6)
squares_dict = {n: n**2 for n in numbers}
print(f"   squares_dict = {squares_dict}")

# 1.4 使用dict()构造函数从其他数据结构创建字典
print("\n1.4 使用dict()构造函数从其他数据结构创建字典:")
# 从键值对列表创建
key_value_pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(key_value_pairs)
print(f"   从键值对列表创建: {dict_from_pairs}")

# 1.5 使用setdefault()方法设置默认值（如果键不存在）
print("\n1.5 使用setdefault()方法设置默认值:")
user_preferences = {"theme": "dark"}
# 如果language键不存在，设置为"en"并返回
language = user_preferences.setdefault("language", "en")
print(f"   设置默认语言: {language}")
print(f"   更新后的preferences: {user_preferences}")

# 1.6 字典合并的最佳方式
print("\n1.6 字典合并的最佳方式:")
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}

# Python 3.9+ 推荐：使用|操作符合并
print("   # Python 3.9+推荐: merged = dict_a | dict_b")

# Python 3.5+ 推荐：使用解包操作符
merged = {**dict_a, **dict_b}
print(f"   Python 3.5+推荐: {merged}")

# 不推荐：修改原字典的方式
print("   # 不推荐：dict_a.update(dict_b)  # 这会修改dict_a")

# 2. 常见错误和陷阱
print("\n2. 常见错误和陷阱:")

# 2.1 尝试使用可变类型作为键
print("\n2.1 尝试使用可变类型作为键:")
print("   # 错误：列表是可变的，不能作为键")
print("   # invalid_dict = {[1, 2]: 'value'}  # TypeError: unhashable type: 'list'")

# 解决方案：使用元组（不可变）
valid_dict = {(1, 2): 'value'}
print(f"   正确：使用元组作为键: {valid_dict}")

# 2.2 修改字典在迭代过程中
print("\n2.2 修改字典在迭代过程中:")
print("   # 错误：在遍历字典时修改字典大小会引发错误")
print("   # my_dict = {1: 'a', 2: 'b', 3: 'c'}")
print("   # for key in my_dict:")
print("   #     if key == 2:")
print("   #         del my_dict[key]  # RuntimeError: dictionary changed size during iteration")

# 解决方案：迭代字典的副本
my_dict = {1: 'a', 2: 'b', 3: 'c'}
for key in list(my_dict.keys()):  # 创建键的列表副本
    if key == 2:
        del my_dict[key]
print(f"   解决方案：迭代键的副本，删除后: {my_dict}")

# 2.3 混淆字典的键和值
print("\n2.3 混淆字典的键和值:")
# 错误：尝试检查值是否存在于键中
product = {"name": "手机", "price": 5999, "brand": "Apple"}
print(f"   检查'手机'是否在product中: {'手机' in product}  # 这检查的是键，不是值")

# 正确：检查值是否存在
print(f"   正确检查'手机'是否是product的值: {'手机' in product.values()}")

# 2.4 浅拷贝vs深拷贝问题
print("\n2.4 浅拷贝vs深拷贝问题:")
import copy

# 创建嵌套字典
original = {"user": {"name": "张三", "age": 25}}

# 浅拷贝
shallow_copy = original.copy()
# 修改浅拷贝中的嵌套字典
shallow_copy["user"]["age"] = 26
print(f"   原始字典: {original}")  # 注意：原始字典也被修改了！
print(f"   浅拷贝: {shallow_copy}")

# 解决方案：使用深拷贝
original = {"user": {"name": "张三", "age": 25}}
deep_copy = copy.deepcopy(original)
deep_copy["user"]["age"] = 26
print(f"   使用深拷贝后，原始字典: {original}")
print(f"   使用深拷贝后，深拷贝: {deep_copy}")

# 2.5 键不存在时引发KeyError
print("\n2.5 键不存在时引发KeyError:")
config = {"debug": True, "port": 8080}
print("   # 错误：config['host']  # KeyError: 'host'")

# 解决方案1：使用get()方法
print(f"   解决方案1：使用get()方法: {config.get('host', 'localhost')}")

# 解决方案2：使用try-except
print("   解决方案2：使用try-except")
try:
    host = config["host"]
except KeyError:
    host = "localhost"
print(f"   host = {host}")

# 3. 性能注意事项
print("\n3. 性能注意事项:")

# 3.1 字典查找的时间复杂度
print("\n3.1 字典查找的时间复杂度:")
print("   字典查找操作的平均时间复杂度是O(1)，非常高效")
print("   对于频繁查找的场景，使用字典比列表更高效")

# 3.2 选择合适的键类型
print("\n3.2 选择合适的键类型:")
print("   - 优先使用不可变的、简单的类型作为键（字符串、数字）")
print("   - 避免使用复杂对象作为键，除非必要")

# 3.3 字典的内存使用
print("\n3.3 字典的内存使用:")
print("   字典比列表需要更多的内存，因为要存储键值对和哈希表结构")
print("   对于非常大的数据集，考虑是否真的需要使用字典")

# 4. 实用技巧
print("\n4. 实用技巧:")

# 4.1 使用字典模拟命名参数
print("\n4.1 使用字典模拟命名参数:")
def process_user(user_info):
    name = user_info.get("name", "未知")
    age = user_info.get("age", 0)
    return f"用户: {name}, 年龄: {age}"

user1 = {"name": "李四", "age": 30}
user2 = {"name": "王五"}  # 没有age
print(f"   处理user1: {process_user(user1)}")
print(f"   处理user2: {process_user(user2)}")

# 4.2 使用字典缓存计算结果
print("\n4.2 使用字典缓存计算结果:")
# 例如：计算斐波那契数列时缓存中间结果
fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    fib_cache[n] = result
    return result

print(f"   fibonacci(10) = {fibonacci(10)}")
print(f"   缓存内容: {fib_cache}")

# 4.3 使用字典进行配置管理
print("\n4.3 使用字典进行配置管理:")
default_config = {
    "debug": False,
    "port": 8000,
    "host": "127.0.0.1",
    "timeout": 30
}

# 用户配置可能只包含部分设置
user_config = {
    "port": 9000,
    "debug": True
}

# 合并配置，用户配置优先级更高
final_config = {**default_config, **user_config}
print(f"   默认配置: {default_config}")
print(f"   用户配置: {user_config}")
print(f"   最终配置: {final_config}")

print("\n" + "=" * 50)
print("恭喜！Python字典学习教程全部完成！")
print("=" * 50)
print("\n您现在已经掌握了Python字典的基本操作、方法、高级特性和最佳实践。")
print("继续练习，将这些知识应用到实际项目中，以加深理解和提高熟练度。")
print("\n祝您编程愉快！")