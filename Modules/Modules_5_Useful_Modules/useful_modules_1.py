from collections import defaultdict, Counter

# Counter - counts each element in an argument - example below

my_list = [1, 2, 3, 4, 5, 6, 7, 7, 7, 6, 4, 1]
sentence = 'blah blah blah my name is Slim Shady'
print(Counter(my_list))
print(Counter(sentence))

# default dict - fills dict in non-existing indexes with some default value

my_dict = defaultdict(lambda: 0, {'a': 1, 'b': 2})

print(my_dict['c'])

