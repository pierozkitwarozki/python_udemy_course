# Comprehensions Exercise

some_letters = ['a', 'a', 'b', 'c', 'd', 'd', 'd', 'e', 'e', 'f', 'g', 'h', 'i', 'i']

duplicates = list({letter for letter in some_letters if some_letters.count(letter) > 1})

print(sorted(duplicates))

# Finds duplicates in some_letters list, adds them to duplicates set and converts it to the list
