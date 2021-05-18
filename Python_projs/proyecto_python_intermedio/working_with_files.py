def read():
    with open('./files/numbers.txt', 'r', encoding = "utf-8") as f:
        numbers = [int(line) for line in f]
    print(numbers)
    

def write():
    names = ["Facundo", "Sara", "Sebastián", "Carol", "Camila"]
    with open('./files/names.txt', 'w', encoding = "utf-8") as f2:
        for name in names:
            f2.write(name)
            f2.write("\n")

def run():
    read()
    write()


if __name__ == '__main__' :
    run()