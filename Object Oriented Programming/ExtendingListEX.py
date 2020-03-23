class SuperList(list):
    def __len__(self):  # changing dunder method len
        return 100


super_list = SuperList()

print(len(super_list))
