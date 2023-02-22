def get_int(text):
    while True:
        num = input(text)
        if num.isnumeric():
            return int(num)

