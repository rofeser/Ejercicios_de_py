x = 1
while (x < 10):
    print(x)
    x = x+1
    
#ciclo while

x = 1
while (x < 50):
    print(x)
    x = x+1
    
    
#ciclo for

x = 1
for x in range(1,10):
    print(x)
    
    
palabra = ("Ronaldjose Fernadez")
for letras in palabra:
    print(letras)
    
    

for i in range(0,50, 2):
    print(i)  
    
    
datos = ["dato1",["dato2"]],["dato3"]
for dato in datos:
    print(dato)
    
    
for i in range(50,0,-1):
    print(i)
    
#tuplas y listas con for

tupla = (1,2,3,4,5,)
tupla2 = ("aaa","bbb","ccc")
tupla3 = (1,"aaaa",True,1.2)
usuario = ("ronald","ronaldfernandez3000.com",20,"camcun")
for i in usuario:
    print(i)        
                  
#con listas

lista =[1,2,3,4]
lista [0]= 1000
print(lista)

lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
    print(i)  
    
#listas con metodos                   

lista = [1,2,3,4,5,6,7,]
for i in lista:
    print(i)
    
lista.append(100)
lista[6]="Hola mundo"
print(lista)  

listaA = [1,2,3,4,5,6,]
listaB = [10,100,1000]
listaA.extend(listaB)
print(listaA)  

lista = [1,2,3,4,5,6,7,8,]
print(lista)
del lista [6]
print(lista)
