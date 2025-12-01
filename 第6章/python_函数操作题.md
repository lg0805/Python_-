# Python 函数知识点操作题 (高职版)

## 前言

大家好！

作为你们的Python老师，我深知“光说不练假把式”的道理。函数是Python编程的核心，掌握好函数，你的编程能力将迈上一个新台阶。

为了帮助大家更好地理解和运用函数相关的每一个知识点，我设计了这套操作题。请大家务必亲手敲一遍代码，运行一下，看看结果是否和预期一致。遇到问题，先独立思考，再参考答案。

开始我们的练习之旅吧！

---

### 1. 知识点：函数的定义与调用

**知识点简述**：学习如何使用 `def` 关键字定义一个最简单的函数，并调用它。

**操作题**：
- **题目**：创建一个名为 `say_hello` 的函数。
- **要求**：
    1. 函数不需要接收任何参数。
    2. 函数的功能是在控制台打印字符串 "你好，欢迎学习Python函数！"。
    3. 定义函数后，调用它。
- **示例输出**：
  ```
  你好，欢迎学习Python函数！
  ```
- **参考答案**：
  ```python
  # 1. 定义函数
  def say_hello():
      print("你好，欢迎学习Python函数！")

  # 2. 调用函数
  say_hello()
  ```

---

### 2. 知识点：位置参数

**知识点简述**：函数可以接收外部传入的数据，这种在定义函数时就确定好顺序和数量的参数，称为位置参数。

**操作题**：
- **题目**：创建一个名为 `calculate_area` 的函数，用于计算长方形的面积。
- **要求**：
    1. 函数接收两个位置参数：`length` (长) 和 `width` (宽)。
    2. 函数内部计算面积（长 * 宽），并打印结果，格式为 "长方形的面积是: [计算出的面积]"。
    3. 调用函数，并传入长为10，宽为5。
- **示例输入与输出**：
  - 输入 (调用时)：`calculate_area(10, 5)`
  - 输出 (控制台)：`长方形的面积是: 50`
- **参考答案**：
  ```python
  def calculate_area(length, width):
      area = length * width
      print(f"长方形的面积是: {area}")

  # 调用函数并传入位置参数
  calculate_area(10, 5)
  ```

---

### 3. 知识点：关键字参数

**知识点简述**：调用函数时，可以通过“关键字=值”的形式传入参数，这种方式可以忽略参数的顺序。

**操作题**：
- **题目**：创建一个名为 `show_user_info` 的函数，用于显示用户信息。
- **要求**：
    1. 函数接收三个参数：`name`, `age`, `city`。
    2. 函数内部打印用户信息，格式为 "姓名: [name], 年龄: [age], 城市: [city]"。
    3. 使用关键字参数的方式调用函数，传入姓名为"张三"，年龄20，城市"北京"，并且调用时故意打乱顺序。
- **示例输入与输出**：
  - 输入 (调用时)：`show_user_info(age=20, city="北京", name="张三")`
  - 输出 (控制台)：`姓名: 张三, 年龄: 20, 城市: 北京`
- **参考答案**：
  ```python
  def show_user_info(name, age, city):
      print(f"姓名: {name}, 年龄: {age}, 城市: {city}")

  # 使用关键字参数调用，顺序可以不一致
  show_user_info(age=20, city="北京", name="张三")
  ```

---

### 4. 知识点：默认参数

**知识点简述**：在定义函数时，可以为参数指定一个默认值。如果在调用时不传入该参数，则使用默认值。

**操作题**：
- **题目**：创建一个名为 `power` 的函数，计算一个数的N次方。
- **要求**：
    1. 函数接收两个参数：`base_num` (底数) 和 `exponent` (指数)。
    2. 参数 `exponent` 的默认值为 2。
    3. 函数打印计算结果。
    4. 调用两次函数：一次只传入底数10；另一次传入底数2，指数5。
- **示例输出**：
  ```
  10 的 2 次方是: 100
  2 的 5 次方是: 32
  ```
- **参考答案**：
  ```python
  def power(base_num, exponent=2):
      result = base_num ** exponent
      print(f"{base_num} 的 {exponent} 次方是: {result}")

  # 调用1：只传入base_num，exponent使用默认值2
  power(10)

  # 调用2：两个参数都传入
  power(2, 5)
  ```

---

### 5. 知识点：可变参数 `*args`

**知识点简述**：当不确定要传入多少个位置参数时，可以使用 `*args`。它会将所有多余的位置参数打包成一个元组(tuple)。

**操作题**：
- **题目**：创建一个名为 `sum_all` 的函数，可以计算任意个数的和。
- **要求**：
    1. 函数使用 `*args` 接收所有传入的数字。
    2. 函数计算所有数字的总和并打印。
    3. 调用函数，传入 1, 2, 3, 4, 5。
- **示例输入与输出**：
  - 输入 (调用时)：`sum_all(1, 2, 3, 4, 5)`
  - 输出 (控制台)：`所有数字的总和是: 15`
- **参考答案**：
  ```python
  def sum_all(*args):
      print(f"收到的参数元组: {args}")
      total = sum(args)
      print(f"所有数字的总和是: {total}")

  sum_all(1, 2, 3, 4, 5)
  ```

---

### 6. 知识点：关键字可变参数 `**kwargs`

**知识点简述**：当不确定要传入多少个关键字参数时，可以使用 `**kwargs`。它会将所有多余的关键字参数打包成一个字典(dict)。

**操作题**：
- **题目**：创建一个名为 `show_extra_info` 的函数，可以接收并显示任意额外的用户信息。
- **要求**：
    1. 函数接收一个位置参数 `name`。
    2. 函数同时使用 `**kwargs` 接收任意数量的关键字参数。
    3. 函数先打印姓名，然后遍历并打印所有额外信息。
    4. 调用函数，传入姓名"李四"，并额外传入 `gender="男"`, `hobby="篮球"`。
- **示例输出**：
  ```
  用户 李四 的额外信息如下:
    - gender: 男
    - hobby: 篮球
  ```
- **参考答案**：
  ```python
  def show_extra_info(name, **kwargs):
      print(f"收到的关键字参数字典: {kwargs}")
      print(f"用户 {name} 的额外信息如下:")
      for key, value in kwargs.items():
          print(f"  - {key}: {value}")

  show_extra_info("李四", gender="男", hobby="篮球")
  ```

---

### 7. 知识点：函数返回值 `return`

**知识点简述**：函数可以使用 `return` 关键字将处理结果返回给调用者，而不仅仅是打印。

**操作题**：
- **题目**：创建一个名为 `celsius_to_fahrenheit` 的函数，将摄氏度转换为华氏度。
- **要求**：
    1. 函数接收一个参数 `celsius` (摄氏度)。
    2. 函数根据公式 `华氏度 = (摄氏度 * 9/5) + 32` 进行计算。
    3. 使用 `return` 关键字返回计算出的华氏度值。
    4. 调用函数，传入25，并用一个变量接收返回值，最后打印该变量。
- **示例输出**：
  ```
  25摄氏度等于77.0华氏度
  ```
- **参考答案**：
  ```python
  def celsius_to_fahrenheit(celsius):
      fahrenheit = (celsius * 9/5) + 32
      return fahrenheit

  # 调用函数并接收返回值
  result = celsius_to_fahrenheit(25)
  print(f"25摄氏度等于{result}华氏度")
  ```

---

### 8. 知识点：返回多个值

**知识点简述**：Python函数可以在一条 `return` 语句中返回多个值，这些值会被自动打包成一个元组。

**操作题**：
- **题目**：创建一个名为 `analyze_list` 的函数，分析一个数字列表。
- **要求**：
    1. 函数接收一个列表 `num_list`。
    2. 函数需要找出列表中的最大值、最小值和总和。
    3. 一次性返回这三个值。
    4. 调用函数，传入列表 `[8, 2, 10, 5, 7]`，并使用三个变量分别接收返回的三个值，最后打印它们。
- **示例输出**：
  ```
  最大值: 10, 最小值: 2, 总和: 32
  ```
- **参考答案**：
  ```python
  def analyze_list(num_list):
      max_val = max(num_list)
      min_val = min(num_list)
      sum_val = sum(num_list)
      return max_val, min_val, sum_val

  # 调用函数并解包返回值
  my_list = [8, 2, 10, 5, 7]
  max_result, min_result, sum_result = analyze_list(my_list)

  print(f"最大值: {max_result}, 最小值: {min_result}, 总和: {sum_result}")
  ```

---

### 9. 知识点：变量作用域与 `global` 关键字

**知识点简述**：函数内部定义的变量是局部变量，只在函数内有效。如果想在函数内部修改全局变量，需要使用 `global` 关键字声明。

**操作题**：
- **题目**：模拟一个计数器功能。
- **要求**：
    1. 在函数外部定义一个全局变量 `count`，初始值为0。
    2. 创建一个名为 `increment` 的函数。
    3. 函数 `increment` 每次被调用时，都将全局变量 `count` 的值加1。
    4. 调用 `increment` 函数三次，每次调用后都打印全局变量 `count` 的值，观察其变化。
- **示例输出**：
  ```
  当前计数值: 1
  当前计数值: 2
  当前计数值: 3
  ```
- **参考答案**：
  ```python
  # 全局变量
  count = 0

  def increment():
      # 声明要修改的是全局变量 count
      global count
      count += 1

  print("开始计数...")
  increment()
  print(f"当前计数值: {count}")
  increment()
  print(f"当前计数值: {count}")
  increment()
  print(f"当前计数值: {count}")
  ```

---

### 10. 知识点：函数文档字符串 (DocString)

**知识点简述**：在函数定义的第一行下方，使用三对引号 `"""..."""` 编写的字符串，是函数的“说明书”，用于解释函数的功能、参数和返回值。

**操作题**：
- **题目**：为第7题中的 `celsius_to_fahrenheit` 函数添加一个规范的文档字符串。
- **要求**：
    1. 找到 `celsius_to_fahrenheit` 函数的定义。
    2. 在 `def` 语句下方添加文档字符串。
    3. 文档字符串应包含：函数的一句话功能描述、参数说明 (`Args`)、返回值说明 (`Returns`)。
    4. 使用 `help()` 函数或 `__doc__` 属性查看你编写的文档。
- **示例输出** (使用 `help()`):
  ```
  Help on function celsius_to_fahrenheit in module __main__:

  celsius_to_fahrenheit(celsius)
      将摄氏度转换为华氏度。
    
      Args:
          celsius (float or int): 输入的摄氏温度值。
    
      Returns:
          float: 计算出的华氏温度值。
  ```
- **参考答案**：
  ```python
  def celsius_to_fahrenheit(celsius):
      """将摄氏度转换为华氏度。

      Args:
          celsius (float or int): 输入的摄氏温度值。

      Returns:
          float: 计算出的华氏温度值。
      """
      fahrenheit = (celsius * 9/5) + 32
      return fahrenheit

  # 使用 help() 查看文档
  help(celsius_to_fahrenheit)

  # 或者打印 __doc__ 属性
  # print(celsius_to_fahrenheit.__doc__)
  ```

---

### 11. 知识点：匿名函数 `lambda`

**知识点简述**：`lambda` 是一种简单、临时的单行小函数，通常用在需要一个函数作为参数的场合。

**操作题**：
- **题目**：对一个包含元组的列表进行排序。
- **要求**：
    1. 有一个列表 `students = [('张三', 20), ('李四', 18), ('王五', 22)]`，元组中分别是姓名和年龄。
    2. 使用 `sorted()` 函数对列表进行排序，但排序的依据是学生的年龄（元组的第二个元素）。
    3. 在 `sorted()` 函数的 `key` 参数中，使用 `lambda` 函数来实现按年龄排序的逻辑。
    4. 打印排序后的列表。
- **示例输出**：
  ```
  [('李四', 18), ('张三', 20), ('王五', 22)]
  ```
- **参考答案**：
  ```python
  students = [('张三', 20), ('李四', 18), ('王五', 22)]

  # key参数接收一个函数，该函数指定了排序的依据
  # lambda student: student[1] 表示对于列表中的每个元素(student)，都返回其索引为1的值(年龄)作为排序键
  sorted_students = sorted(students, key=lambda student: student[1])

  print(sorted_students)
  ```

---

### 12. 知识点：函数作为参数 (高阶函数)

**知识点简述**：在Python中，函数本身也是一种对象，可以像普通变量一样被当作参数传递给另一个函数。

**操作题**：
- **题目**：创建一个通用的计算器函数。
- **要求**：
    1. 定义两个简单的计算函数：`add(a, b)` 返回a+b，`subtract(a, b)` 返回a-b。
    2. 定义一个名为 `calculator` 的高阶函数，它接收三个参数：`num1`, `num2`, 和一个名为 `op_func` 的函数。
    3. `calculator` 函数内部调用 `op_func` 函数，并将 `num1`, `num2` 作为参数传给它，然后返回计算结果。
    4. 调用 `calculator` 两次：一次传入 `add` 函数，一次传入 `subtract` 函数，并打印结果。
- **示例输出**：
  ```
  10 + 5 = 15
  10 - 5 = 5
  ```
- **参考答案**：
  ```python
  def add(a, b):
      return a + b

  def subtract(a, b):
      return a - b

  def calculator(num1, num2, op_func):
      # op_func 在这里是一个占位符，实际调用时会被替换成 add 或 subtract 函数
      result = op_func(num1, num2)
      return result

  # 将 add 函数作为参数传递
  add_result = calculator(10, 5, add)
  print(f"10 + 5 = {add_result}")

  # 将 subtract 函数作为参数传递
  subtract_result = calculator(10, 5, subtract)
  print(f"10 - 5 = {subtract_result}")
  ```

---

### 13. 知识点：递归函数

**知识点简述**：递归函数是一种在函数内部调用自己的函数。它必须包含一个基本情况（终止条件）和一个递归情况。

**操作题**：
- **题目**：使用递归函数计算一个数的阶乘。
- **要求**：
    1. 创建一个名为 `factorial` 的函数。
    2. 函数接收一个参数 `n`。
    3. **基本情况**：如果 `n` 等于1，函数返回1。
    4. **递归情况**：如果 `n` 大于1，函数返回 `n` 乘以 `factorial(n-1)` 的结果。
    5. 调用函数计算5的阶乘，并打印结果。
- **示例输出**：
  ```
  5 的阶乘是: 120
  ```
- **参考答案**：
  ```python
  def factorial(n):
      # 基本情况（终止条件）
      if n == 1:
          return 1
      # 递归情况
      else:
          return n * factorial(n - 1)

  result = factorial(5)
  print(f"5 的阶乘是: {result}")

  # 递归过程拆解：
  # factorial(5) = 5 * factorial(4)
  # factorial(4) = 4 * factorial(3)
  # factorial(3) = 3 * factorial(2)
  # factorial(2) = 2 * factorial(1)
  # factorial(1) = 1
  # 回代：2*1 -> 3*2 -> 4*6 -> 5*24 = 120
  ```
