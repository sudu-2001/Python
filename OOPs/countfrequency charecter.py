string="i like football"

charecter_frequency={}

for char in string:

    if char in charecter_frequency:

        charecter_frequency[char]+=1

    else:

        charecter_frequency[char]=1

for char,count in charecter_frequency.items():

    if count>0:

        print(f"the {char} count is {count}")