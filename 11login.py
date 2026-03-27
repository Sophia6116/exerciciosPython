# FONTE: https://docs.python.org/pt-br/3/library/random.html .

imput= str (input("Digite a senha: "))
tent= str
senha= "euteamo"
i= 0

while i<=3:
    if imput != senha:
        tent= str("Tente novamente:")
        i+=1
        break
    elif imput == senha or tent == senha:
        print("Acesso liberado")
    else:
        print("Conta bloqueada!!!!!!!!")
        
