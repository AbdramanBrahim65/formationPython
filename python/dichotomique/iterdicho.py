def dicho(l):

    k = int (input("Entrer un nombre : "))
    inf = 0
    sup = len(l)-1
    while( inf<=sup ):
        mil = (inf+sup)//2
        if l[mil] == k:
            return mil
        elif  l[mil] < k:
            inf = mil + 1
        else:
            sup = mil - 1
    if inf>sup :
        return -1
    
print(dicho(l=[1,2,3,4,5,6]))
