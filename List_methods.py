"""Topic: List Methods"""
    
'''Sub-Topic'''

print(dir(list))             # To know display all string methods

['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

a=[]
print(type(a))

b=[1,20]
print(type(b))

c=[10,20,30]
print(c[26])          # IndexError: list index out of range
print(c[1]) 
print(c[2])
print(c[3])

a='hee'
print(type(a))
a[0]='s'

a='hee',
print(type(a))
a[0]='s'

b=['hello']
print(type(b))
print(b[0])
b[0]='bye'
print(b)

a=[4,5,6]
a[0]=70
print(a)

b=[1,2,3]
b[5]=10
print(b)

x=[1,2,3]
x.append(4)
print(x)

a=[10,20,30,40]
a.clear()
print(a)

y=[100,200,300,400]
y.remove(500)               # ValueError: x not in list
y.remove(200)
print(y)

c=[10,20,30,40,59]
c.pop()
print(c)

c=[10,20,30,40,59]
c.pop(2)
print(c)

v=[10,20]
n=[30,40,50,'hello']
v.extend(n)
print(v)

r=[1,5,7]
r.insert(0,3)
r.insert(1,3)
r.insert(10,3)
r.insert(2,'hi')
r.insert(2,(70,80))
print(r)

a=['hi',3,4,6,7,8,6]
print(a.count('hi'))
print(a.count('hey'))
print(a.count(6))


h=['python',5,8,'hi']
print(h.index('python'))
print(h.index(8))
print(h.index('v'))

x=[10,20,30,40]
x.reverse()
print(x)

z=[3,8,2,8,11,4]
z.sort()
print(z)

z=[3,8,2,8,11,4]
z.sort(reverse=False)
print(z)

z=[3,8,2,8,11,4]
z.sort(reverse=True)
print(z)
