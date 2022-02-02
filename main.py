n=12
s1=[1]
s2=[7]
s3=[]
count=-1
for i in range(n):
  s3.append(s1[-1]+s2[-1])
  s1.pop(0)
  s1.append(s2)
  s2.pop(0)
  s2.append(s3)
  count+=1
  if n!=count:
    s3.pop(0)
  else:
    break
print(s3)












"""
teksts="pazeme"
print(teksts[2]) #atgriež simbolu ar indeksu 2  	z
print(teksts[:2]) #atgriež līdz simbolam ar indeksu 2 (neieskaitot) 	pa
print(teksts[2:]) #atgriež no simbola ar indeksu 2 līdz vārda beigām zeme
print(teksts[:-2]) #atgriež virkni bez pēdējiem diviem simboliem 	paze
print(teksts[-2]) #atgriež otro simbolu no beigām
"""