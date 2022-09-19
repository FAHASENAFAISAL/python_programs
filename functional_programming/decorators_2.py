# afunction can any number of decorators -->no limit
#greater than 18 vaccinated otherwise create an error
def agevalidate(func):
    def wrapper(a,b):
        if b>=18:
            return func(a,b)
        else:
            raise Exception("not eligible")
    return wrapper
@agevalidate
def vaccine(name,age):
    return "successfully vaccinated"
print(vaccine("anu",17))