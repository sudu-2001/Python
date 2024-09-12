# custom exception is a way to create an exception where it will a class will inherit the except class and raise exception is done inside the if block


class AgeTooLowError(Exception):

    pass

def age_classify(age):

    if age < 0:

        raise ValueError("Age cannot be negative")
    
    elif age<18:

        raise AgeTooLowError("Age is too low")
    
    else:

        print("you are an adult")

try:

    age_classify(14)

except AgeTooLowError as e:

    print(f"AgeTooLowError: {e}")

except ValueError as e:

    print(f"exception : {e}")


