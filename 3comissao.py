id=int (input("Digite o ID do vendedor: "))
codpeca=int (input("Digite o código da peça: "))
precouni=float (input("Digite o preço unitário da peça:R$"))
qtd=int (input("Digite a quantidade de peças: "))

precofinal= precouni*qtd
comissao= precofinal*0.05

print ("Código da peça:",codpeca,"\nPreço unitário:R$",precouni,"\nO portador do ID:",id,"recebrá uma comissão de:R$",comissao)
