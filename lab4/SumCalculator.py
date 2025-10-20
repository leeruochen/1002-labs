r'''
Task Description: 
    In this task, we need to design one recursive function to calculate the SUM value
    of one input number. The SUM of x is defined as the summation of all the positive 
    numbers that are not bigger than X, such as 1+2+3…+X.

    So please design one recursive function sum_recursive(x) to return the SUM value of x. 
    In addition, please implement another function sum_iterative(x) to return the SUM 
    value of x     with the iterative manner (e.g. for loop).  Write the main program to 
    allow users to input one number to your program and call these two functions to see 
    whether they get the same output. 
    
    The example executions are shown as follows:

Note: 
    Your output should be in ONE line.

Running example: 
    C:\INF1002\Lab4\SumCalculator> python SumCalculator.py 3
    The SUM value calculated by recursive is 6 and by iterative is 6.
'''
import sys

# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

def sum_recursive(x):
    if x == 0:
        return 0
    return x + sum_recursive(x - 1)

def sum_iterative(x):
    sum = 0
    for i in range(x + 1):
        sum += i
    return sum

def SumCalculator():
    num = int(sys.argv[1])
    print(f"The SUM value calculated by recursive is {sum_recursive(num)} and by iterative is {sum_iterative(num)}.")


if __name__=='__main__':
     SumCalculator()