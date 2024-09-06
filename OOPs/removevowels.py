string="i like football"
vowels="aeiouAEIOU"

result_string=" "

consonent_string=" "

for char in string:
    if char in vowels:
        result_string+=char
    else:
        consonent_string+=char

print(result_string)
print(consonent_string)