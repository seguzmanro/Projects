class library():
    def __init__(self):
        self.name = ' '
        self.books = []
    def add_book(self):
        self.x = book()
        self.x.capture()
        self.books.append(self.x)
    def order(self):
        print('Please choose an option:\n1. Order by reference\n2. Order by title name\n3. Order by author\n4. Order by quantity')
        opt = int(input())
        if opt == 1:
            tmp = [self.books[i].ref for i in range(len(self.books))]
            tmp.sort()
            for i in range(len(tmp)):
                for j in range(len(self.books)):
                    if tmp[i] == self.books[j].ref:
                        self.books[j].print_()
        elif opt == 2:
            tmp = [self.books[i].title for i in range(len(self.books))]
            tmp.sort()
            for i in range(len(tmp)):
                for j in range(len(self.books)):
                    if tmp[i] == self.books[j].title:
                        self.books[j].print_()
        elif opt == 3:
            tmp = [self.books[i].author for i in range(len(self.books))]
            tmp.sort()
            for i in range(len(tmp)):
                for j in range(len(self.books)):
                    if tmp[i] == self.books[j].author:
                        self.books[j].print_()
        elif opt == 4:
            tmp = [self.books[i].quant for i in range(len(self.books))]
            tmp.sort()
            for i in range(len(tmp)):
                for j in range(len(self.books)):
                    if tmp[i] == self.books[j].quant:
                        self.books[j].print_()
    def print_list(self):
        for i in range(len(self.books)):
            self.books[i].print_()


class book:
    def __init__(self):
        self.ref = 0
        self.quant = 0
        self.title = ' '
        self.author = ' '
    def capture(self):
        print('Book reference: ')
        self.ref = int(input())
        print('Enter quantity: ')
        self.quant = int(input())
        print('Book title: ')
        self.title = input()
        print('Book author: ')
        self.author = input()
    def print_(self):
        print('Book reference: ', self.ref)
        print('Available quantity: ', self.quant)
        print('Book title: ', self.title)
        print('Book author: ', self.author, '\n')


def menu1():
    print('n1. To build a new library\n2. To import an existing library\n0. Exit')
    opt = int(input))
    return opt

def menu2():
    print('Please name your new library:')
    new_lib = library()
    new_lib.name = input()
    print('Great!\nWhat would you like to do next?')
    print('1. To add a new book\n2. To look existing books inside the library\n3. To order the library\n0. Exit')
    opt2 = int(input())
    return opt2

def exit_():
    print('Thank you for using this app!')

if __name__ == '__main__':
    print('Hi! Welcome to your digital library.\n\nWhat would you like to do today?\n')
    opt = menu1()
    if opt == 1:
        opt2 = menu2()
        if opt2 == 1:
            number_books = int(input())
            for number in range(number_books):
                
            