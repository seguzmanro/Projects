def palindrome_func(string):
    return string == string[::-1]

print(palindrome_func('ana'))


palindrome = lambda string: string == string[::-1]
print(palindrome('ana'))

## High order functions: map, filter and reduce
numbers = [1,4,5,6,9,13,19,21]
odd = [i for i in numbers if i % 2 != 0]
odd_2 = list(filter(lambda x: x%2 != 0, numbers))

numbers_2 = [1,2,3,4,5]
squares = [i**2 for i in numbers_2]
squares_2 = list(map(lambda x: x**2, numbers_2))

from functools import reduce
numbers_3 = [2,2,2,2,2]
multiply = 1
for i in numbers_3:
    multiply = multiply * i
multiply_2 = reduce(lambda a, b: a*b, numbers_3)
