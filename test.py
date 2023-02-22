list = [1, 2, 3, 5, 6, 7, 8, 9, 10]

x = 1

while x < 5:
    print(x)
    for i in list:
        print(i)
        if i == 7:
            break
    print(f"While --> {x}")
    x += 1
    print("=" * 10)


