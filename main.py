import math
""""# 2.Uzdevums
Ciparu virknē a1,a2,a3,.... katrs elements sākot no trešā ir vienāds ar iepriekšējo divu virknes elementu summas pēdējo ciparu.<br>
Uzrakstiet programmu, kas dotiem a1,a2 un n atrod virknes n elementu.<br>
<br>
Testa dati:<br>
ievaddati: 1,7,12<br>
izvaddati: 8
"""

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


