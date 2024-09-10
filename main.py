from packages.mathoperator import add,sub,mul
from packages.stringoper import upper,lower
from packages.fileoper.fileoper import read_file,write_file

result1=add(5,4)

print(f"addition:{result1}")

result2=sub(7,5)

print(f"substraction:{result2}")

result3=mul(2,3)

print(f"multiplication:{result3}")

result4=upper("hello")

print(result4)

result5=lower("demo")

print(result5)

filepath='name.txt'

result6=read_file(filepath)

print(result6)

result7=write_file(filepath,"hello world")

print(result7)
