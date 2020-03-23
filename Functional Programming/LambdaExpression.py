# lambda expression / anonymous function
# implementing multiply by 2 function using lambda expression
# and even numbers filtering
# and accumulating with reduce function
from functools import reduce
my_list = [1, 2, 3, 4, 5, 6]
print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 == 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list, 0))
