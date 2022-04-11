def somme():
    """d'une maniere particuliere"""
    M = [[1,2],[4,6]]
    N = [[-1,3],[0,1]]
    C = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            C[i][j] = C[i][j] + M[i][j] + N[i][j]
    print(C)
somme()

def produit():
    M = [[1,1],[2,1]]
    N = [[3,0],[-1,1]]
    C = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c = M[i][k] * N[k][j]
                C[i][j] = C[i][j] + c
    print(C)

produit()