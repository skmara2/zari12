def virkne(b,c,d):
 sar=[b,c]
 for i in range(2,d):
   sk=(sar[i-1]+sar[i-2])%10
   sar.append(sk)
 print(sar[-1])