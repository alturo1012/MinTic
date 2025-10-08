prom=0
i=0
n=int(input("ingrese el numero de notas"))
for i in range(n):
    n1=int(input(f"ingrese nota {i+1}: "))
    while n1>5 or n1 < 0:
        n1=int(input(f"ingrese nota {i+1}: "))
    prom=prom+n1
    #prom +=n1
prom= prom/n
if prom>=3:
    print(f"Aprovado y su nota es: {prom}")
else:
    print(f"Reprovado y su nota es: {prom}")