#Assinging values to variables
#1.basic form
str="hello world"
print(str)

#2.tuple assignment
a,b=(10,20)
print("a=",a)
print("b=",b)

#3.list assignment (using []brackets)
x,y,z=[1,2,3]
print(x)
print(y)
print(z)

#4.sequence assignment
a,b,c,d="nani"
print(a)
print(b)
print(c)
print(d)

#5.extended sequence unpacking
p,*q="hello"
print(p)
print(q)

#6.multiple target assignment

a=b=c=100
print(a)
print(b)
print(c)

#Augmented assignment (updating the value)

""" a=10
a+=5
print(a) """

""" a=20
a-=22
print(a) """

a=5
a*=2
print(a)
