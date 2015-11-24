import numpy as np

if __name__ == '__main__':

#    matrix =    ((0, 1, 1, 0, 0, 0, 0),   # A 
#                (1, 0, 1, 1, 0, 0, 0),   # B
#                (1, 1, 0, 0, 1, 0, 0),   # C
#                (0, 1, 0, 0, 1, 1, 0),   # D
#                (0, 0, 1, 1, 0, 0, 1),   # E
#                (0, 0, 0, 1, 0, 0, 0),   # F
#                (0, 0, 0, 0, 1, 0, 0))   # G

    print("Input Filename.")
    filename = str(input())

    matrix = np.loadtxt(filename, delimiter=',')

    # 隣接行列を隣接リストに変換
    adjacent = []
    for row in matrix:
        tmp = []
        for value in range(len(row)):
            if row[value] != 0:
                tmp.append(value)
        adjacent.append(tmp)

    print(adjacent)

    print("Input Outputfile name.")
    Outputfile = str(input())

    np.savetxt(Outputfile, adjacent, delimiter=',')


