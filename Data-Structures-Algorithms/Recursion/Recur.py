# problem_statement_1: Sum Range of all number upto n
def sum_range(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    return num + sum_range(num-1)

print(sum_range(3))    # output: 6

# problem_statement_2: factorial of a number
def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)

print(factorial(5))    # output: 120