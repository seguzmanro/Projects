def create_dict(n):
    my_dict = {number: number **3 for number in range(n+1)}
    return my_dict

def dict_non_3_divisible(n):
    my_dict = {number: number**3 for number in range(n+1) if number % 3 != 0}
    return my_dict

def dict_sqrt(n):
    my_dict = {number: number**0.5 for number in range(n+1) if number**0.5 % 1 == 0}
    return my_dict

if __name__ == '__main__':
    print(dict_sqrt(1000))