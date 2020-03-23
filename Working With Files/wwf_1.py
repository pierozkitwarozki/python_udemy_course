my_file = open('test.txt')

print(my_file.read())
my_file.seek(0)  # places pointer back to the beginning
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.readline()) # reads first line, moves pointer to the next line
my_file.seek(0)
print(my_file.readlines())  # returns list, each element represents each line

my_file.close()
