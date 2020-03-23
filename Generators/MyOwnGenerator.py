class MyGenerator:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


gen = MyGenerator(0, 100)

for i in gen:
    if i % 4 == 0:
        print(i)
