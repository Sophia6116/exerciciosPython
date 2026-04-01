# 13 - Desenvolva um programa que permita cadastrar usuários (nome e idade). O programa deve:
# Continuar pedindo dados até que o usuário digite "encerrar"
# Exibir ao final:
# Quantidade de usuários cadastrados
# Quantos são maiores de idade (≥ 18 anos
usuarios=0
maior_idade=0
while True:
    nome=(input("Digite o nome:"))
    if nome == "encerrar":
         break
    idade= int (input("Digite a idade:"))  
    usuarios+=1
    if idade>=18:
        maior_idade+=1
print (f"Foram cadastrados {usuarios} usuários\n{maior_idade} são maiores de idade")
