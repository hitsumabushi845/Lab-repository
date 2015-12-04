import numpy as np
import math

#軌道のアルファベットをリストで管理
orbits = ['s', 'p', 'd', 'f', 'g', 'h', 'i', 'j', 'k']

#イオンの持つ電子数，最大の主量子数を決める
print("H like(1)/He like(2)")
electrons = int(input())
print("What is Upper Quantum Number n ?")
upperQuantumNumber = int(input())

if electrons == 2:
    #電子数が偶数の場合の処理(Jは整数値をとる)   
    print("Here is He like")

    allStateNumber = 1 + (sum(np.arange(2, upperQuantumNumber+1, 1))*2) + (sum(np.arange(1, upperQuantumNumber, 1))*2)

    aCoefficients = np.zeros((allStateNumber,allStateNumber))

    tmplist = []
    headerstr = ""
    for n in np.arange(1, upperQuantumNumber+1, 1):
        for l in range(n):
            tmpstr = "1s"+str(n)+orbits[l]
            if l == 0:
                tmplist.append(tmpstr+" singlet S 0")
                headerstr += tmpstr + " singlet S 0, "
                if n != 1:
                    tmplist.append(tmpstr+" triplet S 1")
                    headerstr += tmpstr + " triplet S 1, "
            else:
                tmplist.append(tmpstr + " singlet " + orbits[l].upper() + "1")
                tmplist.append(tmpstr + " triplet " + orbits[l].upper() + str(l-1))
                tmplist.append(tmpstr + " triplet " + orbits[l].upper() + str(l))
                tmplist.append(tmpstr + " triplet " + orbits[l].upper() + str(l+1))
                headerstr += tmpstr + " singlet " + orbits[l].upper() + "1, "
                headerstr += tmpstr + " triplet " + orbits[l].upper() + str(l-1) + ", "
                headerstr += tmpstr + " triplet " + orbits[l].upper() + str(l) + ", "
                headerstr += tmpstr + " triplet " + orbits[l].upper() + str(l+1) + ", "
    print(tmplist)
    #print(len(tmplist))
    #print(allStateNumber)

    i = 0
    for stateA in tmplist:
        for j in range(i+1):
            if i != j:
                print("A Coefficient " + stateA + " to " + tmplist[j])
                tmp = input()
                if tmp:
                    aCoefficients[j][i] = float(tmp)
                else:
                    aCoefficients[j][i] = 0.0
                #aCoefficients[i][j] = i * j
        i+=1

    headerstr = headerstr.rstrip(', ')
    print(headerstr)
    print("input aCoefficients File Name")
    output_file = input()
    if output_file:
        np.savetxt(output_file, aCoefficients, header = headerstr, delimiter=',')
        print("Saved.")
    else:
        print("Done.")

elif electrons == 1:
    print("Here is H like")
    #電子数が奇数の場合の処理(Jは半整数値をとる)
    #全状態の数を決める．Jの違いでで重複する状態も数える
    allStateNumber = sum(np.arange(1, upperQuantumNumber+1,1)) + sum(np.arange(1, upperQuantumNumber,1))
    #print(allStateNumber)
    #全状態の数からなる正方行列を確保する．全て浮動小数点数の0.0で初期化している．
    aCoefficients = np.zeros((allStateNumber,allStateNumber))

    #リストに状態を入れていく(A係数入力時にどのような遷移かわかるようにするため)
    tmplist = []
    headerstr = ""
    for n in np.arange(1,upperQuantumNumber+1,1):
        #print(n)
        for l in range(n):
            #print(l)
            #print(str(n) + orbits[l])
            j = l*2
            if orbits[l] == 's':
                tmplist.append(str(n)+orbits[l])
                headerstr += str(n)+orbits[l]+', '
            else:
                tmplist.append(str(n)+orbits[l]+' ' + str(j-1) + '/2')
                tmplist.append(str(n)+orbits[l]+' ' + str(j+1) + '/2')
                headerstr += str(n)+orbits[l]+' '+str(j-1)+'/2'+', '
                headerstr += str(n)+orbits[l]+' '+str(j+1)+'/2'+', '


    print(tmplist)

    #順番にA係数を正方行列に格納していく．
    i = 0
    for stateA in tmplist:
        for j in range(i+1):
            if i != j:
                print("A Coefficient " + stateA + " to " + tmplist[j])
                tmp = input()
                if tmp:
                    aCoefficients[j][i] = float(tmp)
                else:
                    aCoefficients[j][i] = 0.0
                #aCoefficients[i][j] = i * j
        i+=1
    
    #print(aCoefficients)
    headerstr = headerstr.rstrip(', ')
    print(headerstr)
    print("input aCoefficients File Name")
    output_file = input()
    if output_file:
        np.savetxt(output_file, aCoefficients, header = headerstr, delimiter=',')
        print("Saved.")
    else:
        print("Done.")
   
elif electrons == 0:
    print("Here is Test mode.")
    
    allStateNumber = sum(np.arange(1,upperQuantumNumber+1,1))
    aCoefficients = np.zeros((allStateNumber,allStateNumber))

    #リストに状態を入れていく(A係数入力時にどのような遷移かわかるようにするため)
    tmplist = []
    headerstr = ""
    for n in np.arange(1,upperQuantumNumber+1,1):
        #print(n)
        for l in range(n):
            #print(l)
            #print(str(n) + orbits[l])
            tmplist.append(str(n)+orbits[l])
            headerstr += str(n)+orbits[l]+', '

    print(tmplist)

    #順番にA係数を正方行列に格納していく．
    i = 0
    for stateA in tmplist:
        for j in range(i+1):
            if i != j:
                print("A Coefficient " + stateA + " to " + tmplist[j])
                tmp = input()
                if tmp:
                    aCoefficients[j][i] = float(tmp)
                else:
                    aCoefficients[j][i] = 0.0
                #aCoefficients[i][j] = i * j
        i+=1
    
    #print(aCoefficients)
    headerstr = headerstr.rstrip(', ')
    print(headerstr)
    print("input aCoefficients File Name")
    output_file = input()
    if output_file:
        np.savetxt(output_file, aCoefficients, header = headerstr, delimiter=',')
        print("Saved.")
    else:
        print("Done.")
else:
    print("Please Type 1 or 2.")


