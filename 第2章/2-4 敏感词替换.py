"""
敏感词过滤
思路：给定一个字符串，判断字符串中的文字是否在用户输入的数据中，如果存在使用*替换

"""
sensitive_character = '你好'  # 敏感词库
test_sentence = input('请输入一段话:')
for line in sensitive_character:  # 遍历输入的字符是存在敏感词库中
    if line in test_sentence:  # 判断是否包含敏感词
        test_sentence = test_sentence.replace(line, '*')
print(test_sentence)
# 你好，我是张三
