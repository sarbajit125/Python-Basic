# The Collatz Sequence

def Collatz(number):
    try:
        if number%2 == 0:
            print(number//2)
            return(number//2)
        print(3*number+1)
        return(3*number+1)
    except TypeError:
        print("Input in wrong format")
try:
    x=int(input("Enter the number "))
except ValueError:
    print("please enter integer")
while True:
    try:z=Collatz(x)
    except NameError: 
        print("Pogram terminated due to NameError")
        break
    x=z
    if z == 1:
        break
 
   

    
