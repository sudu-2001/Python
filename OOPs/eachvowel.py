string="I like football"

vowels="aeiouAEIOU"

vowel_count={vowel:0 for vowel in vowels}

for char in string:
    if char in vowels:
        char.lower()
        vowel_count[char]+=1
print(vowel_count)
        
for vowel,count in vowel_count.items():
    if count>0:
        print(f"the {vowel} count is: {count}")

