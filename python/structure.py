# structure conditionnelle

a=int(input("Entrez un nombre : "))
b=int(input("Entrez un nombre : "))

if(a  == b):
    print("a est egal b")
elif( a == 0):
    print(" a est egal 0")
else:
    print("b est egal 0")
def smal():
    return a if a==b else a==0 or b==0
print(smal())

