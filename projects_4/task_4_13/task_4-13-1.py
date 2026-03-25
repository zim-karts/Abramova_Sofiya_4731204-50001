a, b, c, d = map(int, input("Введите четыре числа: ").split())
if a <= b:
    if c <= d:
        if a <= c:
            print(a)
        else: 
            print(c)
    elif d <= c:
        if a <= d: 
            print(a)
        else: 
            print(d)
elif b < a: 
    if c <= d:
        if b <= c:
            print(b)
        else: 
            print(c)
    elif d <= c:
        if b <= d: 
            print(b)
        else: 
            print(d)