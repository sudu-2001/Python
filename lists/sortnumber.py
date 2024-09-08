#using sort function

numbers = [3, 1, 4, 1, 5, 9]

dupli=[]

dupli=list(set(numbers))

dupli.sort(reverse=True)

print(dupli)

#using sorted method

sort=sorted(dupli,reverse=True)

print(dupli)

#using bubbel sort

n=len(numbers)

for i in range(n):

    for j in range(0,n-i-1):

        if numbers[j]>numbers[j+1]:

            numbers[j],numbers[j+1]=numbers[j],numbers[j+1]

            
