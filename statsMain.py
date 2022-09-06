import stats

numberList = []

print("Please enter your list and type 'stop' when done")

while True:
    try:
        userInput = float(input())
        numberList.append(userInput)

    # breaks out of the loop while whenever any letter is typed
    except:
        break

print("Mean " + stats.Mean(numberList) + "\nMedian " + stats.Median(numberList) + "\nMode " + stats.Mode(numberList))
