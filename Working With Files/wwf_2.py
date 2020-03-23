# another way to work with files
# better way

with open('test.txt',
          mode='a') as my_file:  # 'r' - read (default), 'w' - write (treats file like empty),
    # 'r+' - both (overwrites), 'a' - appends
    my_file.write('Hi from pyCharm - (append)')
