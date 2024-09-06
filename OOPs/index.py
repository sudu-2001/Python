string="i like footbal"

word="football"

try:
    finded=string.index(word)
    print(f"the {word} is ther in the string")

except ValueError:
    print(f"the {word} is not found")