import math
diag=float(input("Ievadi kvadrāta diagonāles gaumu (cm): "))
def laukums(x):
  mala_a= x/math.sqrt(2)
  laukums_kv=round(mala_a*mala_a,2)
  return laukums_kv
rezultats=laukums(diag)
print(f"Kvadrāta laukums ={rezultats} cm^2")