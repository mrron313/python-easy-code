
numbers = [3, 0, 4, 1, 2]

for i in range(len(numbers)):
    min = i
    for j in range(i+1, len(numbers)):
        if numbers[min] > numbers[j]:
            min = j

    temp = numbers[i]
    numbers[i] = numbers[min]
    numbers[min] = temp

print(numbers)