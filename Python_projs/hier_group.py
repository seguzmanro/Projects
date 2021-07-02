'''
This program is just a demonstration of the hierarchical grouping algorithm through euclidean distance.
The program generates 10 random coordinates and then searches for the minor distance between any two points.
Next it groups this pair in a set and replaces the points with its midpoint, starting again. 
The end result is a string with the labels of the 10 points (a-j) grouped by parentheses.
It also plots the points with its corresponding labels. 
'''

import random
import math
import uuid
import matplotlib.pyplot as plt


class coord:
    def __init__(self, x, y, coord_label):
        self.x = x
        self.y = y    
        self.coord_label = coord_label


class arbol:
    def __init__(self, coord_1, coord_2=None, node_label=None):
        self.coord_1 = coord_1.coord_label
        if coord_2 != None and node_label == None:
            self.coord_2 = coord_2.coord_label
            self.coord_label = coord_1.coord_label + coord_2.coord_label
            self.node_label = coord_1.coord_label + coord_2.coord_label 
        elif coord_2 == None and node_label == None:
            self.coord_label = coord_1.coord_label
            self.node_label = coord_1.coord_label
        elif coord_2 != None and node_label != None:
            self.coord_2 = coord_2.coord_label
            self.coord_label = coord_1.coord_label + coord_2.coord_label
            self.node_label = node_label
        elif coord_2 == None and node_label != None:
            self.coord_label = coord_1.coord_label
            self.node_label = node_label


def arbol_de_arboles(arbol_1, arbol_2):
    return arbol(arbol_1, arbol_2, node_label = '(' + arbol_1.node_label + ')' + arbol_2.node_label)


def get_coord(vector_coords, coord_label):
    for i in vector_coords:
        if i.coord_label == coord_label:
            return i


def gen_coords(coord_label):
    coord.x = random.randint(0,10)
    coord.y = random.randint(0,10)
    coord_label = coord_label
    return coord(coord.x,coord.y, coord_label)


def obt_dist_euc(coord_1, coord_2):
    return math.sqrt((coord_1.x - coord_2.x)**2 + (coord_1.y - coord_2.y)**2)


def obt_coord_medio(coord_1, coord_2):
    return coord((coord_1.x + coord_2.x) / 2, (coord_1.y + coord_2.y) / 2, coord_label='(' + coord_1.coord_label + coord_2.coord_label + ')')


def plot_points(vector_coords):
    x=[]
    y=[]
    labels=[]
    for coord in vector_coords:
        x.append(coord.x)
        y.append(coord.y)
        labels.append(coord.coord_label)
    plt.figure()
    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Random Coordinates')
    for i, label in enumerate(labels):
        plt.annotate(label, (x[i], y[i]))
    plt.show()


def agrup_jerarq(vector_coords):
    vector_coords_2=[]
    for coord in vector_coords:
        vector_coords_2.append(coord)
    while len(vector_coords) > 1:
        distancias = {}
        for i in range(len(vector_coords)):
            for j in range(len(vector_coords)):
                distancia = obt_dist_euc(vector_coords[i], vector_coords[j])
                if distancia == 0:
                    pass
                else:
                    distancias[(i,j)] = distancia
        distancias = dict(sorted(distancias.items(), key=lambda kv:kv[1]))
        label_1 = vector_coords[min(distancias.items(), key=lambda kv:kv[1])[0][0]].coord_label
        label_2 = vector_coords[min(distancias.items(), key=lambda kv:kv[1])[0][1]].coord_label
        vector_coords.append(obt_coord_medio(vector_coords[min(distancias.items(), key=lambda kv:kv[1])[0][0]], vector_coords[min(distancias.items(), key=lambda kv:kv[1])[0][1]]))
        tree_a = arbol(vector_coords[min(distancias.items(), key=lambda kv:kv[1])[0][0]], vector_coords[min(distancias.items(), key=lambda kv:kv[1])[0][1]])
        vector_coords.remove(get_coord(vector_coords, label_1))
        vector_coords.remove(get_coord(vector_coords, label_2))
    return tree_a


if __name__ == '__main__':
    vector_coords = [gen_coords(i) for i in ['a','b','c','d','e','f','g','h','i','j']]
    plot_points(vector_coords)
    print(agrup_jerarq(vector_coords).node_label)
