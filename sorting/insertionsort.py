
numbers = [3, 99, 0, 7, 5]

# j = 0, i = 1
# 2, 3, 5, 0, 1

# j = 0, i = 2
# j = 1, i = 2
# 2, 3, 5, 0, 1

# j = 0, i = 3
# 0, 3, 5, 2, 1
# j = 1, i = 3
# 0, 2, 5, 3, 1
# j = 2, i = 3
# 0, 2, 3, 5, 1

# j = 0, i = 4
# 1, 


for i in range(1, len(numbers)):
    for j in range(0, i):
        if numbers[j] > numbers[i]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp


print(numbers)
