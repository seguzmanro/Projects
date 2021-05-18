import os
import random


with open("./proyecto_python_intermedio/files/database.txt", "r", encoding="utf-8") as file_:
    DATA = [line.removesuffix("\n") for line in file_]


def get_index(letter, word):
    rep = [index for index in range(len(word)) if word[index] == letter]
    return rep

def replace_in_blank(blank, index, letter):
    blank = list(blank)
    for i in index:
        blank[i] = letter
    blank = ''.join(blank)
    return blank

def sel_word():
    word = random.choice(DATA)
    word = word.upper()
    blank = "_" * len(word)
    return word, blank

def new_letter():
    letter = input("Por favor, ingresa una letra: ")
    letter = letter.upper()
    return letter

def actual(letter, word, blank):
    index = get_index(letter, word)
    if len(index) > 0:
        blank = replace_in_blank(blank, index, letter)
    return blank

if __name__ == '__main__':
    os.system("clear")
    word, blank = sel_word()
    tries = 0
    while "_" in blank:
        os.system("clear")
        print("¡Bienvenido al juego del ahorcado!\n")
        print(blank)
        print(f'Número de intentos: {tries}')
        tries += 1
        letter = new_letter()
        blank = actual(letter, word, blank)
    os.system("clear")
    print(f'{blank}\n¡Felicidades, has ganado!\nNúmero total de intenos: {tries}')
        
        
        