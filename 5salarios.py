nome=str (input("Digite o nome: "))
inicial=float (input("Digite o salário: "))
if inicial<=1000:
    aumento=inicial*(20/100)
    final=inicial+aumento
elif inicial>=1000.01 and inicial<= 5000:    
    aumento=inicial*(10/100)
    final=inicial+aumento
else:
    aumento=inicial*(5/100)
    final= inicial+aumento

print("O novo salário do(a) jogador(a)",nome,"será: R$",final)