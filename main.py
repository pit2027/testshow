def number():
    all_number = []

    def inner(x:int)->list:
        all_number.append(x)
        return all_number
    return inner

def counter():
    count = 0
    def inner(val):
        nonlocal count
        count+=val
        return count
    return inner


if __name__ == '__main__':
    f = number()
    c = counter()
    print(f(1))
    print(f(1))
    print(f(1))
    print(c(1))
    print(c(1))
    print(c(1))

