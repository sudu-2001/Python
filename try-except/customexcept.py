def age_age(age):

    if age<0:

        raise ValueError("age cannot be negative")
    
    elif age<18:

        raise Exception("you under age")
    
    else:

        print("you are an adult")

try:

    age_age(-4)

except ValueError as e:

    print(f"the value occured: {e}")

except Exception as e:

    print(f"the occured value:{e}")