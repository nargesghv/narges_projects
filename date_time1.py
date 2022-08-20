import datetime
def date_log(func):
    def wrapper(*args,**kwargs):
        date=datetime.datetime.now()
        value=func(*args,**kwargs)
        with open("log.txt","a") as f:
            name=func.__name__
            f.write(f"name: {name} date: {date} returend: {value}args: {args} kwargs: {kwargs} \n")
        return value

    return wrapper


@date_log
def helloworld():
    print("Hello_World")

@date_log
def printtext(text):
    print(f"print: {text}")

@date_log
def nil():
    print('got it')

@date_log
def narges(a,b):
    return (a+b)
    


helloworld()
printtext("niloo")
print(narges(10,12))




        
