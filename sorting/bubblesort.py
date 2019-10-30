
numbers = [5, 4, 1, 3, 2]
i = 0 
flag = 0

for i in range(len(numbers)):
    flag = 0
    for j in range(len(numbers) - 1):  
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
            flag = 1

    if flag == 0:
        break

print(numbers)