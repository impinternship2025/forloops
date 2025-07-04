#Given the list ages = [34, 21, 56, 19, 40], sort the list in ascending and then in descending order.


def sort_numbers(numbers):
    numbers.sort()
    print("Numbers sorted in ascending order:", numbers)

    numbers.sort(reverse=True)
    print("Numbers sorted in descending order:", numbers)

numbers = [34,21,56,19,40]


sort_numbers(numbers)
