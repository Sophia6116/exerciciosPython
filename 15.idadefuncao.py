def  maior_idade (idade):
    if idade>=18:
        return "maior de idade"
    else:
        return "menor de idade"    
idd= int (input("Digite a idade:"))
result=maior_idade(idd)
print(f"Você é {result}")