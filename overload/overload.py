

from overloaddec import overload

@overload
def add(a: str, b: str):
    print("strs")
    return b + a


@overload
def add(a: int, b: int):
    print("ints")
    return a + b

@overload
def add(a: int, b: str):
    print("mul")
    return b * a


print(add(a=1, b=2))
print(add("1", "2"))
print(add(4, 'hello'))
print(add(1.0, 5))
