a = 0
b = 1
c = 2
d = [0, 1, 2]
e = ["pera", "uva", "manzana"]
f = [2.5, 3, 4.5]

print(e)  

e.insert(4, 'melon')  
print(e)

e.append("mango")  
print(e)

print(a, b, c, d, e, f)  

e[1]="coco"
print(e)

#print(len(e))
#for elemmento in (e):
    #print(elemmento)

matriz=(["uva","pera","manzana","mango","melon"],[200,300,500,1000,600])
print(matriz[0][0],matriz[0][1])