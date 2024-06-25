"""
PYTHON ALGORITHMS - THE FIZZBUZZ PROBLEM

Write a program that prints the numbers 1 to 100. 

+ For multiples of three print Fizz instead of the number
+ For the multiples of five print Buzz
+ For multiples of both three and five print FizzBuzz

In order to solve this problem, you need a way to check if a number is a multiple of 3, 5, both or neither.
Modulo (%) returns the remainder. The problem can be solved by checking if each number is divisible by both 3&5, 3, 5 or neither
"""

for num in range(1, 101): 
    
    # Check if there are any remainders for
    # 3 and 5 first, because the following elif statements would break this logic
    # i.e. if 15 / 5 comes first, then it would be satisfied and move on
    if (num % 3 == 0 and num % 5 == 0):
        print('FizzBuzz')

    elif num % 5 == 0: 
        print('Buzz')
        
    elif num % 3 == 0:
        print('Fizz')
    
    else: 
        print(num)
