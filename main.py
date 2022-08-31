import basics

while True:
    choice = int(input("Choose from the following options:\n1 - addition\n2 - subtract\n3 - multiply\n4 - divide"))

    match choice:
        case 1:
            first_number = float(input("Enter your first number: "))
            second_number = float(input("Enter your second number: "))
            print(basics.addition(first_number, second_number))
            break
        case 2:
            first_number = float(input("Enter your first number: "))
            second_number = float(input("Enter your second number: "))
            print(basics.subtraction(first_number, second_number))
            break
        case 3:
            first_number = float(input("Enter your first number: "))
            second_number = float(input("Enter your second number: "))
            print(basics.multiply(first_number, second_number))
            break
        case 4:
            first_number = float(input("Enter your first number: "))
            second_number = float(input("Enter your second number: "))
            print(basics.divide(first_number, second_number))
            break
        case default:
            choice = int(input("please enter a valid number"))