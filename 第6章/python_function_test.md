# Python 函数知识测试题

## 一、选择题（每题5分，共30分）

### 1. 下列关于函数定义的说法，正确的是：
A. 函数名可以使用数字开头  
B. 函数定义必须使用 `def` 关键字  
C. 函数可以没有 `return` 语句，但必须有参数  
D. 一个函数只能有一个 `return` 语句  

**答案：B**

---

### 2. 以下代码的输出结果是什么？
```python
def func(x, y=5):
    return x + y

print(func(3))
```
A. 3  
B. 5  
C. 8  
D. 报错  

**答案：C**

---

### 3. 关于函数参数传递，下列说法错误的是：
A. Python 中参数传递采用"引用传递"方式  
B. 不可变对象（如整数、字符串）作为参数时，函数内修改不影响原变量  
C. 可变对象（如列表、字典）作为参数时，函数内修改会影响原对象  
D. 函数参数可以有默认值  

**答案：A**（Python 采用的是"对象引用传递"，但对于不可变对象表现类似值传递）

---

### 4. 以下哪个是正确的函数调用方式？
```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
```
A. `greet()`  
B. `greet("Alice")`  
C. `greet(message="Hi")`  
D. `greet("Bob", name="Alice")`  

**答案：B**

---

### 5. 下列代码的输出是什么？
```python
def modify_list(lst):
    lst.append(4)
    return lst

my_list = [1, 2, 3]
new_list = modify_list(my_list)
print(len(my_list))
```
A. 3  
B. 4  
C. 报错  
D. None  

**答案：B**

---

### 6. 关于 `return` 语句，下列说法正确的是：
A. `return` 语句必须返回一个值  
B. 函数执行到 `return` 语句后会立即结束  
C. 一个函数只能有一个 `return` 语句  
D. 没有 `return` 语句的函数返回值为 0  

**答案：B**

---

## 二、程序填空题（每空5分，共30分）

### 1. 完成以下函数，计算两个数的最大值
```python
def max_value(a, b):
    if ________(1)________:
        return a
    else:
        return ________(2)________
```
**答案：**
- (1) `a > b` 或 `a >= b`
- (2) `b`

---

### 2. 完成以下函数，计算列表中所有元素的和
```python
def sum_list(numbers):
    total = ________(3)________
    for num in numbers:
        ________(4)________
    return total
```
**答案：**
- (3) `0`
- (4) `total += num` 或 `total = total + num`

---

### 3. 完成以下函数，判断一个数是否为偶数
```python
def is_even(n):
    return ________(5)________
```
**答案：**
- (5) `n % 2 == 0`

---

### 4. 完成以下函数，使用默认参数
```python
def power(base, ________(6)________):
    return base ** exponent

print(power(2, 3))  # 输出 8
print(power(5))     # 输出 25
```
**答案：**
- (6) `exponent=2`

---

## 三、程序设计题（每题20分，共40分）

### 1. 编写函数：计算阶乘
**题目要求：**
编写一个函数 `factorial(n)`，计算并返回 n 的阶乘（n!）。
- 如果 n 为 0 或 1，返回 1
- 如果 n 为负数，返回 None
- 例如：`factorial(5)` 应返回 120

**参考答案：**
```python
def factorial(n):
    """计算 n 的阶乘"""
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# 测试
print(factorial(5))   # 输出: 120
print(factorial(0))   # 输出: 1
print(factorial(-3))  # 输出: None
```

**评分标准：**
- 正确处理边界条件（n=0, n=1, n<0）：6分
- 正确实现阶乘计算逻辑：10分
- 代码规范性和可读性：4分

---

### 2. 编写函数：查找列表中的最大值和最小值
**题目要求：**
编写一个函数 `find_min_max(numbers)`，接收一个数字列表作为参数，返回一个包含最小值和最大值的元组 `(min_value, max_value)`。
- 如果列表为空，返回 `(None, None)`
- 例如：`find_min_max([3, 1, 4, 1, 5, 9])` 应返回 `(1, 9)`

**参考答案：**
```python
def find_min_max(numbers):
    """查找列表中的最小值和最大值"""
    if not numbers:  # 列表为空
        return (None, None)
    
    min_value = numbers[0]
    max_value = numbers[0]
    
    for num in numbers:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    
    return (min_value, max_value)

# 测试
print(find_min_max([3, 1, 4, 1, 5, 9]))  # 输出: (1, 9)
print(find_min_max([7]))                 # 输出: (7, 7)
print(find_min_max([]))                  # 输出: (None, None)
```

**评分标准：**
- 正确处理空列表情况：5分
- 正确找到最小值：6分
- 正确找到最大值：6分
- 正确返回元组格式：3分

---

## 附加题（选做，10分）

### 编写函数：判断素数
**题目要求：**
编写一个函数 `is_prime(n)`，判断一个正整数 n 是否为素数。
- 素数是指大于 1 且只能被 1 和自身整除的数
- 返回 `True` 或 `False`
- 例如：`is_prime(7)` 返回 `True`，`is_prime(8)` 返回 `False`

**参考答案：**
```python
def is_prime(n):
    """判断 n 是否为素数"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 只需检查到 sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# 测试
print(is_prime(7))   # 输出: True
print(is_prime(8))   # 输出: False
print(is_prime(2))   # 输出: True
print(is_prime(1))   # 输出: False
```

**评分标准：**
- 正确处理边界情况（n<=1, n=2）：3分
- 正确实现素数判断逻辑：5分
- 代码优化（如只检查到√n）：2分

---

## 知识点覆盖

本套试题涵盖以下知识点：
1. ✅ 函数的定义和调用
2. ✅ 函数参数（位置参数、默认参数）
3. ✅ 返回值（return 语句）
4. ✅ 参数传递机制（可变对象与不可变对象）
5. ✅ 函数的应用（循环、条件判断结合）
6. ✅ 边界条件处理
7. ✅ 代码规范性

**总分：100分（附加题不计入总分）**
**考试时间：60分钟**
