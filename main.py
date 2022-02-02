viens=int(input("Ievadi pirmo skaitli: "))
divi=int(input("Ievadi otro skaitli: "))
skaits=int(input("Kuru skaitli vēlies uzzināt: "))
visi=[viens,divi]
for i in range(0,skaits-2):
    nak=visi[i]+visi[i+1]
    nak=nak%10
    visi.append(nak)
print(visi[skaits-1])


skaitlis=str(input("Ievadi skaitli: "))
summa=int(skaitlis)
for i in range(0,len(skaitlis)):
    jauns=skaitlis[1:]
    summa=int(jauns)
    skaitlis=skaitlis[1:]
print(summa)

#nestrādā un es nezinu kāpēc