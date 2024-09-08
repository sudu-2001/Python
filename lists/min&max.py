numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

smallest=numbers[0]

largest=numbers[0]

for number in numbers:
    if number < smallest:
        smallest=number

    if number >largest:
        largest=number

print(f"the largest element is:{largest} \n the smallest number is {smallest}")
