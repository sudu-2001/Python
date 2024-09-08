# using index built in method

numbers = [10, 20, 30, 40, 50]

print(numbers.index(30))

#using for loop

target=30

index=-1

for i in range(len(numbers)):

    if numbers[i]==target:

        index=i

        print(index)