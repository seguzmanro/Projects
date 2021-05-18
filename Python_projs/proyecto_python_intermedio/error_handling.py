def palindrome(string):
    string = string.lower()
    return string == string [::-1]

def divisors(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    return divisors

## Using try, raise and except:

# def run_palindrome():
#     while True:
#         try:
#             string = input("Ingresa una cadena de carácteres:\n")
#             if len(string) <= 2:
#                 raise ValueError("Por favor, ingresa cadenas de más de 2 caracteres")
#             print(palindrome(string))
#             break
#         except ValueError as ve:
#             print(ve)
#             print(False)

# def run_divisors():
#     while True:
#         try:
#             num = int(input("Ingresa un número:\n"))
#             if num < 0:
#                 raise ValueError("\nPor favor, ingresa solo números positivos")
#             print(divisors(num))
#             break
#         except ValueError:
#             print("\nPor favor, ingresa solo números positivos")

## Now using assert statements:
def run_palindrome():
    string = input("Ingresa una cadena de carácteres:\n")
    assert len(string) > 2, "Por favor, ingresa cadenas de más de 2 carácteres"
    print(palindrome(string))

def run_divisors():
    num = input("Ingresa un número:\n")
    assert num.isnumeric() and int(num) > 0, "Por favor ingresa solo números positivos"
    num = int(num)
    print(divisors(num))

if __name__ == '__main__':
    run_divisors()
    #run_palindrome()