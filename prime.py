def is_prime(num):
    if num<=1:
     return False
    for i in range (2, int (num**0.5) + 1):
       if num % i == 0:
          return False
    return true

num1, num2 = map(int,input ("Enter two number :").split())

if is_prime(num1):
   print(f"{num1} is a prime")
else:
   print(f"{num1} is not prime") 

if is_prime(num1):
   print(f"{num2} is a prime")
else:
   print(f"{num2} is not prime") 
