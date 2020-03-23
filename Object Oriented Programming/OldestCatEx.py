class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat_1 = Cat('pussy1', 2)
cat_2 = Cat('pussy2', 3)
cat_3 = Cat('pussy3', 4)


def find_oldest(my_list):
    return max(my_list)


def show_oldest(oldest_cat):
    print(f'The oldest cat is {oldest_cat} years old')
    return True


show_oldest(find_oldest([cat_1.age, cat_2.age, cat_3.age]))
