#condicionales Anidadas o Combinadas

edad = int(input("Digite su edad:"))

if edad > 0 and edad < 100:
    print("edad es correcta")
    if edad >= 18:
        print("Es mayor de edad")
        
else:
    print("edad incorrecta")
            
# condicionales anidaddas

datoA = int(input("ingrese numero:"))
datoB = int(input("ingrese otro numero:"))
datoC = int(input("ingrese otro numero mas:"))

if datoA > datoB:
    if (datoA > datoC):
        print("El mayor es:",datoA)
    else:
        print("El mayor es:",datoC)
else:
    if (datoB > datoC):
        print("El mayor es:",datoB)
    else:
        print("El mayor es:",datoC)
        
#Condicionales con operador logico

datoA = int(input("Ingrese numero:"))
datoB = int(input("Ingrese otro numero:"))
datoC = int(input("Ingrese otro numero mas:"))

if (datoA > datoB) and (datoA > datoC) and (datoA == datoC):
    print("El mayor es:",datoA)
    
elif (datoA == datoB):
    print("son iguales",datoA,datoB,datoC)
        
else:
    print("hola")
    
# condicional 

datoA = int(input("digite un numero:"))
datoB = int(input("digite otro numero:"))
datoC = int(input("digite otro numero mas:"))

if (datoA>datoB)and  (datoA>datoC) and (datoB>datoC):
    print("El mayor:",datoA)
    if (datoC>datoB):
        print("el mayor es:",datoB)
    
elif (datoA==datoB)and  (datoA==datoC) and (datoB==datoC):
    print("son iguales:",datoA,datoB)
else:
    
    if (datoA<datoB)and (datoB==datoC):
        print("son igual:",datoB,datoC)
        print("el mayor es :",datoB)
        
    else:
        print("los dos son igual.",datoB,datoC)
   

                                       
    
            




       

        
    