def summa(a,b):
  a=int(a)
  sar=[a]
  x=len(b)-1
  for i in range(x):
    sar.append(a%(10**x))
    x-=1
  return(sum(sar))