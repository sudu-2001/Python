def divide_numbers(a,b):

    try:
        
        result=a/b

    except ZeroDivisionError as e:

        print(f"you cant divide it by:{b}")

        print(f"exception:{e}")

    except TypeError as e:
        
        print(f"you cant divide a number with strings")

        print(f"except:{e}")

    else:

        print(f"the result of division of 2 numbers is:{result}")

    finally:

        print(f"the division of 2 numbers is completed")


divide_numbers(5,0)

divide_numbers(6,2)

divide_numbers(4,"two")

