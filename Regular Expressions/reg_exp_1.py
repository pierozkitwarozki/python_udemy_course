import re

test_line = 'Example text in pycharm. Coding in pycharm is pycharming'
pattern = re.compile('pycharm')
answer = pattern.search(test_line)
answer_b = pattern.findall(test_line)
answer_c = pattern.fullmatch(test_line)  # all string must be matched
answer_d = pattern.match(test_line)
print(answer)
print(answer.span())  # where it occurred
print(answer.start())
print(answer.end())
print(answer.group())
print(answer_b)
print(answer_c)
print(answer_d)
