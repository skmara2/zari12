def summa(x,y):
  x=int(x)
  sar=[x]
  len(y)=int(len(y))
  for i in range(len(y)):
    sar.append(x%(10**(len(y))))
    len(y)-=1
    print(sum(sar))
