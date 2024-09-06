string="took took"

process_string=string.replace(" ","").lower()

reversed_string=process_string[::-1]

if process_string==reversed_string:
    print("the given string is palindrome")

else:
    print("the string is not palindrome")