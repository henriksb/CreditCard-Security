from itertools import product
import sys

def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0

def find_missing_digits(partial_card_number):
    total = 0
    missing_indices = [i for i, x in enumerate(partial_card_number) if x == '*']
    for replacement in product('0123456789', repeat=len(missing_indices)):
        test_number = list(partial_card_number)
        for index, digit in zip(missing_indices, replacement):
            test_number[index] = digit
        test_number_str = ''.join(test_number)
        if luhn_check(int(test_number_str)):
            total += 1
            print(test_number_str)

    print("Total number of combinations: " + str(total))

partial_card_number = sys.argv[1] 
find_missing_digits(partial_card_number)
