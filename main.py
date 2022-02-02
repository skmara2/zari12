x1=int(input("Ievadi pirmo skaitli: "))
x2=int(input("Ievadi otro skaitli: "))
element=int(input("Ievadi kuru elementu pēc kārtas vēlies izvadīt: "))

def risinajums(a,b,e):
  sar=[x1,x2]
  for i in range(1, e-1):
    m=sar[i-1]+sar[i]
    n=m%10
    sar.append(n)
  atb=sar[e-1]
  return atb
atbilde=risinajums(x1,x2,element)
print(atbilde)