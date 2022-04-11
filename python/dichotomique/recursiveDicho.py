def dicho(l,inf,sup,k):
    mil = (inf + sup)//2
    if sup < inf:
        return -1
    elif l[mil] == k :
        return mil
    elif l[mil] < k:
        dicho(l,inf,mil+1,k)
    else:
        dicho(l,mil-1,sup,k)
l=[1,2,3,4,5,6]
sup = len(l)-1
print(dicho(l,0,sup,3))
