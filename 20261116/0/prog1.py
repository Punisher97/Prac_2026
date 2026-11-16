class A:
    def __init__(self, a=0):
        self.a = a

    def __str__(self):
        return "A"

    def __add__(self, other):
        return self.a + other.a


class B(A):
    def __str__(self):
        return super().__str__() + ":B"


class C(B):
    def __str__(self):
        return super().__str__() + ":C"


ClassFromType = type("CLASS", (), {
    "A": 123,
    "fun": lambda self: self.A * 2,
    "__str__": lambda self: f"<{self.A}>",
    "__init__": lambda self, A: setattr(self, "A", A),
})


class Regular:
    __value = 123


Dynamic = type("Dynamic", (), {"__value": 123})


class Child(ClassFromType):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f"Child: {super().__str__()}"



def init_type_child(self, value):
    super(TypeChild, self).__init__(value)


TypeChild = type("TypeChild", (ClassFromType,), {"__init__": init_type_child})


if __name__ == "__main__":
    print(A())
    print(B())
    print(C())
    # print("Обычный class:", Regular._Regular__value)
    # print("super() в class:", Child(5))
    # print("super() в методе для type():", TypeChild(7))
