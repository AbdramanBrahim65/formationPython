def recherche_sequentielle(l,k):
    for i in range(len(l)-1):
        if l[i] == k:
            return i
    if i >= len(i):
        return -1
    
print(recherche_sequentielle([1,2,3,4,5,6,7],5))