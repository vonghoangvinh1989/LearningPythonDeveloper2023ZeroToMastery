# MRO - Method Resolution Order
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())
D.__str__
