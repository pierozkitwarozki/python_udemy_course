# Examples

my_list = [char for char in 'hello world']  # adds each character to the list
my_list2 = [num for num in range(0, 100)]  # adds each number in range from 0 to 99
my_list3 = [num * 3 for num in range(0, 100)]  # adds each number multiplied by 3 in range from 0 to 99
my_list4 = [num ** 2 for num in range(0, 100) if
            num % 2 == 0]  # adds each number (if even) powered by 2 in range from 0 to 99
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)
