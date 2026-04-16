def para_somar(n1,n2):
    soma=n1+n2
    return soma
num1=float (input("Digite o primeiro número:"))
num2= float(input("Digite o segundo número:"))
result=para_somar (num1,num2)
print(f"A soma dos dois números é: {result:.2f}")