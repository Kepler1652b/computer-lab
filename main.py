def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def biggest_number(list_of_numbers):
    biggest = list_of_numbers[0]
    for number in list_of_numbers:
        if number>biggest:
            biggest=number
    return biggest

def main():
    count = 0
    number = 2

    while count < 100:
        if is_prime(number):
            print(number)
            count += 1
        number += 1



