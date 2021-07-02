def square_numbers(n):
    squares = []
    for number in range(n+1):
        squares.append(number**2)
    return squares

def square_numbers_list_comprehension(n):
    squares_comprehension = [number**2 for number in range(n+1)]
    return squares_comprehension

def non_3_divisible(n):
    non_divisibles = [number**2 for number in range(n+1) if (number % 3 != 0)]
    return non_divisibles

def numbers():
    numbers = [number for number in range(1,99999) if (number % 4 == 0) and (number % 6 == 0) and (number % 9 == 0)]
    return numbers

if __name__ == '__main__':
    print(f'Multiples of 4, 6 and 9 from 1 to 99999:\n{numbers()}\n')
    print(f'Number of multiples of 4, 6 and 9 from 1 to 99999: {len(numbers())}')
    