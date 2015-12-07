import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def show_graph(G):
    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=6)
    nx.draw_networkx_labels(G, pos,font_size=20, font_family='sans-selif')

    plt.show()

if __name__ == '__main__':

    #軌道のアルファベットをリストで管理
    orbits = ['s', 'p', 'd', 'f', 'g', 'h', 'i', 'j', 'k']

    #空の有向グラフ構造を生成
    graph = nx.DiGraph()

    #イオンの持つ電子数，最大の主量子数を決める
    print("H like(1)/He like(2)")
    electrons = int(input())
    print("What is Upper Quantum Number n ?")
    upperQuantumNumber = int(input())

    if electrons == 2:
        #電子数が偶数の場合の処理(Jは整数値をとる)   
        print("Here is He like")

        allStateNumber = 1 + (sum(np.arange(2, upperQuantumNumber+1, 1))*2) + (sum(np.arange(1, upperQuantumNumber, 1))*2)

        tmplist = []
        headerstr = ""
        for n in np.arange(1, upperQuantumNumber+1, 1):
            for l in range(n):
                tmpstr = "1s"+str(n)+orbits[l]
                if l == 0:
                    tmplist.append(tmpstr+" singlet S 0")
                    graph.add_node(tmpstr+" singlet S 0")
                    if n != 1:
                        tmplist.append(tmpstr+" triplet S 1")
                        graph.add_node(tmpstr+" triplet S 1")
                else:
                    tmplist.append(tmpstr + " singlet " + orbits[l].upper() + "1")
                    tmplist.append(tmpstr + " triplet " + orbits[l].upper() + str(l-1))
                    tmplist.append(tmpstr + " triplet " + orbits[l].upper() + str(l))
                    tmplist.append(tmpstr + " triplet " + orbits[l].upper() + str(l+1))
                    graph.add_node(tmpstr + " singlet " + orbits[l].upper() + "1")
                    graph.add_node(tmpstr + " triplet " + orbits[l].upper() + str(l-1))
                    graph.add_node(tmpstr + " triplet " + orbits[l].upper() + str(l))
                    graph.add_node(tmpstr + " triplet " + orbits[l].upper() + str(l+1))
        print(tmplist)

        i = 0
        for stateA in tmplist:
            for j in range(i+1):
                if i != j:
                    print("A Coefficient " + stateA + " to " + tmplist[j])
                    tmp = input()
                    if tmp:
                        graph.add_edge(stateA,tmplist[j], weight = float(tmp))
                    
            i+=1

        print('Show graph?(y/n)')
        sg = input()
        if sg == 'y':
            show_graph(graph)

        print("input aCoefficients File Name")
        output_file = input()
        if output_file:
            nx.write_weighted_edgelist(graph, output_file)
            print("Saved.")
        else:
            print("Done.")

    elif electrons == 1:
        print("Here is H like")
        #電子数が奇数の場合の処理(Jは半整数値をとる)
        #全状態の数を決める．Jの違いでで重複する状態も数える
        allStateNumber = sum(np.arange(1, upperQuantumNumber+1,1)) + sum(np.arange(1, upperQuantumNumber,1))

        #リストとグラフに状態を入れていく(リストは状態の順番を把握するため)
        tmplist = []
        for n in np.arange(1,upperQuantumNumber+1,1):
            for l in range(n):
                j = l*2
                if orbits[l] == 's':
                    tmplist.append(str(n)+orbits[l])
                    graph.add_node(str(n)+orbits[l])
                else:
                    tmplist.append(str(n)+orbits[l]+' ' + str(j-1) + '/2')
                    tmplist.append(str(n)+orbits[l]+' ' + str(j+1) + '/2')
                    graph.add_node(str(n)+orbits[l]+' ' + str(j-1) + '/2')
                    graph.add_node(str(n)+orbits[l]+' ' + str(j+1) + '/2')


        print(tmplist)

        #順番にA係数をグラフに格納していく．
        i = 0
        for stateA in tmplist:
            for j in range(i+1):
                if i != j:
                    print("A Coefficient " + stateA + " to " + tmplist[j])
                    tmp = input()
                    if tmp:
                        graph.add_edge(stateA,tmplist[j], weight=float(tmp))
            i+=1

        #ここでyを入力すればグラフを描画する
        print('Show graph?(y/n)')
        sg = input()
        if sg == 'y':
            show_graph(graph)

        #エッジリストの出力(入力がない場合はリストを出力しない)
        print("input aCoefficients File Name")
        output_file = input()
        if output_file:
            nx.write_weighted_edgelist(graph, output_file)
            print("Saved.")
        else:
            print("Done.")

    elif electrons == 0:
        print("Here is Test mode.")

        allStateNumber = sum(np.arange(1,upperQuantumNumber+1,1))

        #リストに状態を入れていく(A係数入力時にどのような遷移かわかるようにするため)
        tmplist = []
        for n in np.arange(1,upperQuantumNumber+1,1):
            #print(n)
            for l in range(n):
                tmplist.append(str(n)+orbits[l])
                graph.add_node(str(n)+orbits[l])

        print(tmplist)

        #順番にA係数を正方行列に格納していく．
        i = 0
        for stateA in tmplist:
            for j in range(i+1):
                if i != j:
                    print("A Coefficient " + stateA + " to " + tmplist[j])
                    tmp = input()
                    if tmp:
                        graph.add_edge(stateA,tmplist[j],weight=float(tmp))
            i+=1


        print('Show graph?(y/n)')
        sg = input()
        if sg == 'y':
            show_graph(graph)

    else:
        print("Please Type 1 or 2.")
