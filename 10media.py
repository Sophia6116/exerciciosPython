n1= float(input("Nota 1:"))
n2= float(input("Nota 2:"))
n3= float(input("Nota 3:"))

media= (n1+n2+n3)/3

if media<5:
    conc= "C"
elif media>=5 and media<8:
    conc= "B"
else:
    conc= "A"
print(f"Média: {media:.2f}\nConceito: {conc}")