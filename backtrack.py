import numpy as np



if __name__ == '__main__':
    
    print("Input A Coefficient File Name.")

    ACoefficientFileName = str(input())

    if ACoefficientFileName != '':
        data = np.loadtxt(ACoefficientFileName, delimiter=',')
        matrix = data + data.T
    else:
        matrix = np.array([[0,1,0],[1,1,0],[0,0,1]])

    print(matrix)
