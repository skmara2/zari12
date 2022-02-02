import math
import random

a1=int(input("Ievadi virknes 1. skaitli: ")) #1
a2=int(input("Ievadi virknes 2. skaitli: ")) #7
ntais=int(input("Ievadi n elementu: ")) #12

def virkne(a,b,n):
  sk=[a,b]
  for i in range(1, n-1):
    p=sk[i-1]+sk[i]
    o=p%10
    sk.append(o)
  rez=sk[n-1]
  return rez
rezultats=virkne(a1,a2,ntais)
print(rezultats)
