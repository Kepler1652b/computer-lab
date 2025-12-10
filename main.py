from datetime import datetime, timedelta
import random

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


def blind_date(list_of_boys:list,list_of_girls:list):
    offset = 5
    start_time = datetime.now() + timedelta(offset)
    while list_of_boys:
        boy_random_index = random.randint(0,len(list_of_boys)-1)
        boy = list_of_boys[boy_random_index]
        list_of_boys.pop(boy_random_index)

        girl_random_index = random.randint(0,len(list_of_girls)-1)
        girl = list_of_girls[girl_random_index]
        list_of_girls.pop(girl_random_index)
        
        bd = (boy,girl,start_time.date())
        print(bd)


def swap(a,b):
    a,b =b,a
    return (a,b)



def main():
    # count = 0
    # number = 2

    # while count < 100:
    #     if is_prime(number):
    #         print(number)
    #         count += 1
    #     number += 1
    boys = ["amir",'sam','shahram']
    girls = ['mina','mobina','fatemeh','z']
    blind_date(boys,girls)


main()