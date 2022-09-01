# binary to decimal

def binary_to_decimal(binary_number_input):
    binary = binary_number_input
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)

    return decimal


def decimal_to_binary(decimal_number):
    return bin(decimal_number)

