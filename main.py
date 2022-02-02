a1=1
a2=7
n=12
for i in range(n):
  skaitlis=a1+a2
  cipars=a2+skaitlis
  a1=skaitlis
  a2=cipars
  pedejais=(a1+a2)%10
  print(pedejais)

skaitlis=7231493
for i in range(7):
  if i==1:
    virkne=skaitlis%1000000 #problēm aradīsies, ja skaitli nebūs tieši 7 cipari
    summa=skaitlis+virkne
  elif i==2:
    virkne=skaitlis%100000
    summa+=virkne
  elif i==3:
    virkne=skaitlis%10000
    summa+=virkne
  elif i==4:
    virkne=skaitlis%1000
    summa+=virkne
  elif i==5:
    virkne=skaitlis%100
    summa+=virkne
  elif i==6:
    virkne=skaitlis%10
    summa+=virkne
print(summa)

