peso= float (input("Digite o peso:"))
alt= float (input("Digite a sua altura:"))

imc= peso/(alt**2)

if imc<18.5:
    clas= "Abaixo do peso"
elif imc<=24.9:
    clas= "Peso normal"
elif imc<=29.9:
    clas= "Excesso de peso"
elif imc<=34.9:
    clas= "Obesidade grau I"
elif imc<=39.9:
    clas= "Obesidade grau II"
else:
    clas= "Obesidade grau III"
    
print (f"IMC: {imc:.2f}\nClassificação: {clas}")
    
    # Pesquisa: o "f" no inicio, ajuda a unir label e result dentro das chaves, e o ".2f" deica com dias casas decimais
    