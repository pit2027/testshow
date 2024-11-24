def number():
    all_number = []

    def inner(x:int)->list:
        all_number.append(x)
        return all_number
    return inner

if __name__ == '__main__':
    f = number()
    print(f(1))
    print(f(1))
    print(f(1))

