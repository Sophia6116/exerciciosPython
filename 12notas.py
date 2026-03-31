# 12 - Crie um programa que solicite notas de alunos até que seja digitado -1.
# Ao final, exiba  Média das notas, Maior nota e Menor nota
soma=0
i=0   
while True:
    nota= float (input("Digite a nota (ou -1 para terminar):"))
    if nota == -1:
            break
    if i == 0:
        maior=nota
        menor=nota
    else:
        if nota>maior:
           maior=nota
        if nota<menor:
           menor=nota
    soma= nota+soma
    i+=1
    
    if i>0:
        media = soma / i  
print(f"Média: {media:.2f}\nMaior nota: {maior}\nMenor nota: {menor}")

# manos e manas, como mostra a maior e menor nota tirada? (Trabalho pra Sophia do futuro)
    
