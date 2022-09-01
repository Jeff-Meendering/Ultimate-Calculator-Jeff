# binary to decimal
def binary_to_decimal(binary_number_input):
    binary = binary_number_input
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)

    return decimal


# decimal to binary conversion
def decimal_to_binary(decimal_number):
    return bin(decimal_number)


# decimal to hex
def decimal_to_hex(decimal_number):
    return hex(decimal_number)
