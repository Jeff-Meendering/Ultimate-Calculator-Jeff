#
numberList = []

print("Please enter your list and type 'stop' when done")

while True:
    try:
        userInput = float(input())
        if userInput == "stop":
            break
        numberList.append(userInput)
    except:
        print("Error invalid input. Please enter a valid number")
        continue

print(userInput)

