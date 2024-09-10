string="i like football"

vowel="aeiouAEIOU"

result=""

for char in string:

    if char in vowel:

        result+="u"

    else:

        result+=char

print(result)