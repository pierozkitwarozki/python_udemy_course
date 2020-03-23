# Set and Dictionary Comprehension

# Set Examples
my_list = {char for char in 'hello world'}  # adds each character to the list
my_list2 = {num for num in range(0, 100)}  # adds each number in range from 0 to 99
my_list3 = {num * 3 for num in range(0, 100)}  # adds each number multiplied by 3 in range from 0 to 99
my_list4 = {num ** 2 for num in range(0, 100) if
            num % 2 == 0}  # adds each number (if even) powered by 2 in range from 0 to 99
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# Dictionary Examples
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

my_dict2 = {key: value ** 2 for key, value in my_dict.items() if
            value % 2 == 0}  # adds each item (value powered by 2) if value is even
my_dict3 = {num: num * 2 for num in
            range(0, 10)}  # adds each item, where num in range 0-10 is the key and key multiplied by 2 is the value

print(my_dict2)
print(my_dict3)
