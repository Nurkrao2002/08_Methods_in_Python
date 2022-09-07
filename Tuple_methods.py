"""Topic: Tuple_methods"""

'''Sub_Topics'''

print(dir(tuple))

['count', 'index']


x=(1)
print(x,type(x))

x=(1,)
print(x,type(x))

pr=('apple','reliance','asus','dell','samsung')
pr[1]="Motorolla"

n="Hello" ,  "World"
print(n,type(n)) 
print(n[0])

v=(1,4.2,'hello',[2,3],('H','D'),None,True)
print(v,type(v)) 

v=(1,4.2,'hello',[2,3],('H','D'))
v[0]=21

v=(1,4.2,'hello',[2,7],('H','D'))
print(v.count(4.2))
print(v.index([2,7]))


print(dir(tuple))