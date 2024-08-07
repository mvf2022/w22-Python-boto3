#write a script that will take two numbers and display the sum of those numbers

try:
    n1=int(input("please enter the first number: "))
    n2=int(input("please enter the second number: "))    
except:
    print("please enter a valid number")
else:
    _sum=n1+n2
    print(_sum)