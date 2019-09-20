print("hello world")
#this is comment
'''this is multiline
comment'''
'''a=7
print(a, end="   done")
b=10
print(type(a))
print(type(b))
b="hello"
print(type(b))
#string manipulation-different methods
#print(b[1:3])
#print(b[:])
print(b[3:5])
print(b[2:-1])
#print(b[2:-4]) index shoul not trespass the starting value
a=input("a=")

b=input("b=")
print(type(a), type(b))
a=input("a=")
b=input("b=")
a=int(a)
b=int(b)
print(type(a), type(b))
'''
#creating lists-we can put a ny type of values into it
list1=[1,2,"hello" ,2.5]
print(type(list1))
print(list1[0])
print(list1[1:5])
print(list1[:3])
print(list1[:])
#to change the value ina list
list1[2]="sawa"
print(list1[:])
#length of the list
print(len(list1))
list1.append("bhoot")
print(list1[:])
print(len(list1))
list1.insert(0,"lalala")
print(list1[:])
print(len(list1))
list1.remove("bhoot")
print(list1[:])
print(len(list1))
list1.remove(1)
print(list1[:])
print(len(list1))
list1.clear()
print(list1[:])
print(len(list1))
del(list1)



#creating tuples- immutable
t1=(1,2,34,5)
print(len(t1))
#t1.remove(t1[1])
print(t1)



#creatin' dictionary
d1={ 'two':2 ,'one':[1,2,3], 'three':3}
print(d1)
print(d1['one'])
d1['four']=[4,5,6]
print(d1)
d1.pop('two')
d1.pop('three')
print(d1)


