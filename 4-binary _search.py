def main():
    sequence = input("Sequence: ")
    element = int(input("Element: "))
    result = binary_search(sorted(list(sequence)), element)
    if result == element:
        print("Exist")
    else:
        print("Not exist")


def binary_search(sequence, element):
    start = 0
    end = len(sequence)
    
    # here we're looping through the sequence, hoping to see that the element is existed in it
    while start <= end:
        middle_point = (start + int(end)) // 2
        num = int(sequence[middle_point])

        if element == num:
            return num
        # if the element is less than the num the first part of the sequence will be dicarded
        if element <= num:
            end = middle_point - 1
        # if the element is greater than the num the second part of the sequence will be dicarded
        else:
            start = middle_point + 1

    return None


main()
