mi_set = set([1,2,3,4,5])

print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
s1.add(2)
s1.remove(3)
s1.discard(6)
s1.pop()#elimina aleatorio al ser un set ya que no esta indezadoi
s1.clear()#limpia el set
print(s1)
#print(s3)

