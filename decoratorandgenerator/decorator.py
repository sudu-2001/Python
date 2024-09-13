import time

def log_decorator(func):

    def wrapper(*args,**kwargs):

        start_time=time.time()

        print(f"exection of {func.__name__} is started")

        result=func(*args,**kwargs)

        endtime=time.time()

        print(f"programme {func.__name__} is stopped")

        print(f"Executed time:{endtime-start_time} seconds")

        return result
    
    return wrapper

@log_decorator
def sum_time(a,b):

    time.sleep()

    return a+b

print(sum_time(5,9))