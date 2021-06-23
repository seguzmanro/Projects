# def min_sq(list_):
#     '''
#     Returns the slope and intercept of a linear regression from a data set.
#     Input: a list of paired values (x,y)
#     Output: two float numbers corresponding to the slope and the intercept of the linear equation, respectively.
#     '''
#     x = [i[0] for i in list_]
#     x_mean = sum(x)/len(x)
#     y = [i[1] for i in list_]
#     y_mean = sum(y)/len(y)
#     values1 = []
#     values2 = []
#     for i in range(len(list_)):
#         values1.append((x[i]-x_mean)*(y[i]-y_mean))
#         values2.append((x[i]-x_mean)**2)
#     slope = sum(values1)/sum(values2)
#     intercept = y_mean - slope*x_mean
#     return slope, intercept


# if __name__ == '__main__':
#     data = [(1,2),(2,3),(3,5),(4,6),(5,5)]
#     print(f'The approximate linear equation from the data is:\nY = {min_sq(data)[1]} + {min_sq(data)[0]}X')

import numpy as np
import matplotlib.pyplot as plt

def estimate_b0_b1(x, y):
    n = np.size(x)
    #obtener promedios de X e Y:
    m_x, m_y = np.mean(x), np.mean(y)
    #calcular sumatoria de XY y de XX
    sumatoria_xy = np.sum((x-m_x)*(y-m_y))
    sumatoria_xx = np.sum((x-m_x)**2)
    #coeficientes de regresión:
    b_1 = sumatoria_xy/sumatoria_xx
    b_0 = m_y - b_1*m_x
    return b_0, b_1

#Función de graficado:
def plot_regression(x,y,b):
    plt.scatter(x, y, color = 'g', marker = 'o', s = 30)
    y_pred = b[0] + b[1]*x
    plt.plot(x, y_pred, color = 'b')

    #etiquetado: 
    plt.xlabel('x-Independiente')
    plt.ylabel('y-Dependiente')

    plt.show()

#Codigo main:
def main():
    x = np.array([1,2,3,4,5])
    y = np.array([2,3,5,6,5])
    b = estimate_b0_b1(x, y)
    print(f'Los valores de b0 = {b[0]}, b1 = {b[1]}')
    plot_regression(x, y, b)

if __name__ == '__main__':
    main()