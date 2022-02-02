
def virkne(a,b,c):
  sar=[a,b]
  for i in range(2,c):
    sar.append((sar[i-1]+sar[i-2])%10)
  return(sar[-1])
