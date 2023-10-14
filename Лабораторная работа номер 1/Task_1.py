numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_of_missed = 0
sum_of_exist = 0
for i in range(len(numbers)):
    if (numbers[i] != None):
        sum_of_exist += numbers[i]
    else:
        index_of_missed = i
numbers[index_of_missed] = sum_of_exist / (len(numbers))
print("Измененный список:", numbers)
