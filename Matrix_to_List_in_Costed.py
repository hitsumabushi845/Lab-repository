import numpy as np

if __name__ == '__main__':

    tmpmatrix =    ((0, 2, 1, 0, 0, 0, 0),   # A 
                (1, 0, 5, 1, 0, 0, 0),   # B
                (1, 1, 0, 0, 1, 0, 0),   # C
                (0, 1, 0, 0, 1, 1, 0),   # D
                (0, 0, 8, 1, 0, 0, 1),   # E
                (0, 0, 0, 1, 0, 0, 0),   # F
                (0, 0, 0, 0, 1, 0, 0))   # G

    print("Input Filename.")
    filename = str(input())

    if filename:
        matrix = np.loadtxt(filename, delimiter=',')
    else:
        matrix = tmpmatrix

    print(len(matrix[0]))
    # 隣接行列を隣接リストに変換
    adjacent = []
    for row in matrix:
        tmp = []
        for value in range(len(row)):
            if row[value] != 0:
                tmp.append((value, row[value]))
        adjacent.append(tmp)

    print(adjacent)
    print(len(adjacent))

    print("Input Outputfile name.")
    Outputfile = str(input())

    if Outputfile:
        np.savetxt(Outputfile, adjacent, delimiter=',')


