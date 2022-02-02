import math
""""# 2.Uzdevums
Ciparu virknē a1,a2,a3,.... katrs elements sākot no trešā ir vienāds ar iepriekšējo divu virknes elementu summas pēdējo ciparu.<br>
Uzrakstiet programmu, kas dotiem a1,a2 un n atrod virknes n elementu.<br>
<br>
Testa dati:<br>
ievaddati: 1,7,12<br>
izvaddati: 8


a1=int(input("Ievadi pirmo skaitli: "))
a2=int(input("Ievadi otro skaitli: "))
a3=int(input("Ievadi elementu c: "))
def cipari(a,b,c):
  li=[1,7]
  for i in range(1,c-1):
    l=li[i-1]+li[i]
    v=l%10
    li.append(v)
  a3 = li[c-1]
  return a3
a3 = cipari(a1,a2,a3)
print(a3)

#3.uzdevums
Uz papīra lapas tika uzrakstīts naturāls skaitlis, kura visi cipari bija lielāki par 0. Skaitlim bija ne vairāk kā 100 cipari. <br>
Pēc tam zem šī skaitļa stabiņā tika uzrakstīti skaitļi, kā redzams paraugā šeit: <br>
https://clevercode.lv/task/show/summa2 <br>

Beigās visi skaitļi tika saskaitīti. <br>
Piemērs, ievaddati 7231493, izvaddati 7496561."""


naturāls = 7231493
def stabins(s):
  li=[]
  summ=0
  stronk=str(s)
  for x in stronk:
    if  len(stronk)>100 or int(x)<=0:
     return 0
    else:
      pagarinaajums=True
  
  if pagarinaajums==True:
   for x in range(len(stronk),0,-1):
      a=naturāls%10**x
      li.append(a)
      print(a)
   for x in li:
      summ+=x
  return summ

iznakums=stabins(naturāls)
print(iznakums)