"""Topic: Dict Methods """

''' Dictionary:  It is a data type in python.
It is represented by { : } , dict (dictionary) it is 
a combination of key-value pair.
The value can be accessed with the help of a key.
dict can have several data types in it , it can also
have one more dict inside it.
'''
'''Sub Topic'''

print(dir(dict))

['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


book={
1: "Python Programming",
2: 'Core Python Programming',
3: 'Advance Python Programming',
5.7: '7pm',
'p': 'Python'
}
print(book['p'])
print(book[10])              # KeyError

h={1:"",2: "Python", 3: 7, 4: 6.2,
5: [1,4], 6: (4,3), 7: {1,2},
8: {3: "world"}}
print(h[1],type(h[1]))
print(h[2],type(h[2]))
print(h,type(h))
print(h.keys())
print(h.values())
print(h.items())


h={1:"",2: "Python", 3: 7, 4: 6.2,
5: [1,4], 6: (4,3), 7: {1,2}, 8: {3: "world"}}
h.clear()
print(h)

a=[101,104,110,113,116,118]
print(dict.fromkeys(a,25))

h={1:"", 2: "Python", 3: 7, 4: 6.2,
5: [1,4], 6: (4,3), 7: {1,2},8: {3: "world"}}
print(h.get(4))                   # 6.2
print(h.get(76))                  # None
print(h[47])
h.pop(4)
print(h)
h.popitem()
print(h)

h={1:"", 2: "Python", 3: 7, 4: 6.2,
5: [1,4], 6: (4,3), 7: {1,2},8: {3: "world"}}
h.update({7: 'Core Python'})
print(h)
h.update({9: 'Adv Python'})
print(h)


h={1:"", 2: "Python", 3: 7, 4: 6.2,
5: [1,4], 6: (4,3), 7: {1,2},8: {3: "world"}}
h.setdefault(8,'DevOps')
print(h)
h.setdefault(10 , 'DevOps')
print(h)
