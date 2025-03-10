def great():
    print("Hello")

def greet(name):
    print(f"Hello, {name}")

greet("khushi")
def add(a: int, b:int) ->int :
    result = add(a+b)
    return result

def add_greet(name="Guest"):
    print(f"Hello, {name}")

greet("Bela")    

def add_numbers (*numbers):
    return sum(numbers)
print (add_numbers(1,2,3,4,5)) 

def print_info(**info):
    for key ,value in info.items() :
        print(f"{key} : {value}")

print_info(name="Ela", age=19, city="NYC")

square = lambda x: x** 2
print (square(5))

def factorial (n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)
    
def add(a: int, b:int) ->int :
    result = int(a) + int(b)
    return result 

result = add(5.5, 4.5)
print(result)
