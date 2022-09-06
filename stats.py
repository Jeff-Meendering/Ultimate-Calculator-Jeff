from collections import Counter

# Calculate median
def Median(list):

    listLength = len(list)
    position = listLength // 2
    if listLength % 2:
        return sorted(list)[position]
    return sum(sorted(list)[position - 1:position + 1] / 2)


# Calculate mean
def Mean(list):

    return sum(list) / len(list)


# Calculate mode
def Mode(list):
    number = Counter(list)
    return [a for a, b in number.items() if b == number.most_common(1)[0](1)]

