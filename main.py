import math
"""
1.uzd 
diag=float(input("Ievadi kvadrāta diagonāles gaumu (cm): "))
def laukums(x):
  mala_a= x/math.sqrt(2)
  laukums_kv=round(mala_a*mala_a,2)
  return laukums_kv
rezultats=laukums(diag)
print(f"Kvadrāta laukums ={rezultats} cm^2")



2.uzd

a1=int(input("Ievadi 1.skaitli: "))
a2=int(input("Ievadi 2.skaitli: "))

elements=int(input("Ievadi n elementu: "))

def virkne(x,y,n):
  li=[x,y]
  for i in range(1,n-1):
    g=li[i-1]+li[i]
    h=g%10
    li.append(h)
  rez = li[n-1]
  return rez
rezultats = virkne(a1,a2,elements)
print(rezultats)



3.uzd


skaitlis = 7231493
def funkcija(x):
  li=[]
  summa=0
  strings=str(x)
  for i in strings:
    if int(i)<=0 or len(strings)>100:
     return 0
    else:
      turp=True
    


  if turp==True:
   for i in range(len(strings),0,-1):
      d=skaitlis%10**i
      li.append(d)
      print(d)
   for i in li:
      summa+=i
  return summa

rez=funkcija(skaitlis)
print(rez)
"""
