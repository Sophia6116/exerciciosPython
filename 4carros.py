inicial=float (input("Digite o valor de fabrica do veículo: R$"))
imposto=inicial*0.45
comimposto=imposto+inicial
lucro=comimposto*0.12
final=lucro+comimposto

print ("Valor dos impostos: R$",imposto,"\nPreço do carro MAIS os impostos: R$",comimposto,"\nValor do lucro: R$",lucro,"\nValor final (impostos MAIS o lucro): R$",final)