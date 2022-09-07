"""Topic: set data type
set is represented by { } with element inside it
but we cannot represented an empty set.
if we keep an empty set { } it will treated as dictionary (dict) 
set can contain several data types in it but
we cannot have a list and one more set inside it.
set cannot have one more set inside it.
set is mutable , modifications can be made.
i.e we can add and remove from set
but frozenset is immutable . we cannot add and remove elements in it.
set is unordered.
"""

'''Sub Topic'''

print(dir(set))

['add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']


e={}
print(e,type(e)) # {} <class 'dict'>

v={1,2.6,"Hello",("hi",2),{4}}
print(v,type(v)) # <class 'set'>

n={10,20,30}
print(n[1])


a={1,2,3}
b='hello',1,2,3
a={'hi','rav'}
b='ravi'
a.add(b) 
print(a) 

b={1,5,7}
b.clear()
print(b) # set()

a={1,2,3}; b={4,3,3,6}; c={10,15,20}; d={1,4,7}
print(a.intersection(b)) 
print(a.intersection(c)) 
print(a.intersection(d)) 
print(b.intersection(d)) 


a={1,2,3,'hello'}
b={4,3,5,'hey'}
print(a.union(b))
print(b.union(a))

a={1,2,3}
b={4,3,5}
c={4,3,7}
a.update(b) # {1,2,3,4,5}
a.update(c) # {1,2,3,4,5,7}
print(a) 

a={5,10,20,25,30}
b={10,21,5}
print(a.difference(b)) 
print(b.difference(a)) 
print(a-b)
print(b-a)

z={55,56,57,73,45,23}
z.discard(44)
print(z)
z.discard(73)
print(z)

v={26,7,11,4,23}
v.pop()
print(v)

A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}
print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))
print('Are B and C disjoint?', B.isdisjoint(C))

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}
print(A.issubset(B))
print(B.issubset(A))
print(A.issubset(C))
print(C.issubset(B))



print(len(['add', 'clear', 'copy', 'difference',
 'difference_update', 'discard', 'intersection', 
 'intersection_update', 'isdisjoint', 'issubset', 
 'issuperset', 'pop', 'remove', 'symmetric_difference', 
'symmetric_difference_update', 'union', 'update']))

"""remove """

a={8,9,10,12,14}
a.remove(150)
print(a)

"""" issuperset """

a={8,9,10,12,14}
b={10,14}
print(a.issuperset(b))

a={8,9,10,12,14}
b={8,9,10}
print(a.issuperset(b))
print(b.issuperset(a))
