#write me a code to calculate fibonnacci series using recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  
    
n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer")        
else:    
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))     

#Output
#Enter the number of terms: 10
#Fibonacci sequence:


#write documentation and comments for this
#code
#The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
#The Fibonacci sequence is defined by the recurrence relation:

