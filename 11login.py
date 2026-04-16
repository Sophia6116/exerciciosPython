senha= "senha123"
i=1
while i<=3:
    imput= str(input("Digite a senha:"))
    if imput == senha:
        print ("Acesso concebido")
        break
    else:
        i+=1
        print ("Incorreto")
if i>3:            
   print ("Conta bloqueada")
    

 




        
