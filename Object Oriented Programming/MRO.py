class Letter():
    pass


class A(Letter):
    pass


class B(Letter):
    pass


class ABWord(A, B):
    pass


# mro method shows exactly how inheritance is being proceeded
# helps with implementing multi inheritance

print(ABWord.mro())
