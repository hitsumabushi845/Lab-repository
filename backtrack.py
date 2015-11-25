import numpy as np



if __name__ == '__main__':
    
    print("Input A Coefficient File Name.")

    ACoefficientFileName = str(input())

    data = loadtxt(ACoefficientFileName, delimiter=',')

    matrix = data + data.T

    print(matrix)
