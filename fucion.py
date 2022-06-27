
    

n=8
for i in range (n):
    print(i,"hola")
    
letras=str(input(":"))
for caracter in letras:
       if caracter in "abchdefgijklmnñopqrstuvwyxz":
              print(caracter,)             
    
def s(a,b):
   return a+b

def r(a,b):
   return a-b
 
def m(a,b):
   return a*b
  
def d(a,b):
    return a/b
 
while True:
   print("Menu principal")
   print("1 sumar")
   print("2 restar")
   print("3 multiplicar")
   print("4 dividir")
   opc = input("Ingrese una opcion:")
   n1 = float(input(":"))
   n2 = float(input(":"))
   if opc == "1":
         print("La suma es: ",s(n1,n2))
   
   elif opc == "2":
         print("La resta es: ",r(n1,n2))
         
   elif opc == "3":
         print("La multiplicacion:",m(n1,n2))
         
   elif opc == "4":
         print("La divicion es:",d(n1,n2))
   else:
          print("Opcion invalidas")
                    

 
   

   
   
   
      
   
    
     
    
        
        

    

