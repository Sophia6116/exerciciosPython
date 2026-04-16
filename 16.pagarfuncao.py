def quanto_pagar(preco,quantidade):
    pagar= preco*quantidade
    return pagar
prc= float (input("Digite o preço unitário:"))
qtd= int (input("Digite a quantidade de produtos:"))
result= quanto_pagar(prc,qtd)
print (f"Preço final: {result:.2f}")