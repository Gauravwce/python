"""a=100
print(a)
print("The number is",a)
print("The datatype of a is",type(a)"""

"""var1= 5 +8j
print(var1)
print(type(var1))"""

"""a=65
b=20
print("Addition is", a+b)
print("Subtraction is", a-b)
print("Multiplication is", a*b)
print("Division is", a/b)
print("Remainder is", a%b)
print("Floor Division is", a//b)"""

"""a=6
b=2

a=b
print(a)
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)
a//=b
print(a)"""

"""a=6
b=2

if a>10 and b<5:
    print("a is greater than 10 and b is less than 3")
if a>10 or b<5:
    print("either a is greater than 10 or b is less than 5")
print(not a>b)
print(not a<b)

a=65
b=20

if a==b:
    print("a and b are equal")
if a!=b:
    print("a is not equal to b")
if a>b:
    print("a is greater than b")
if a<b:
    print("a is less than b")
if a>=b:
    print("a is greater than equal to b")
if a<=b:
    print("a is less than equal to b")"""

"""
In Python, to write an empty class pass statement is used.
 pass is a special statement in Python that does nothing.
It only works as a dummy statement.
However, objects of an empty class can also be created.
"""

class MyClass:
    pass


m1=MyClass()
m2=MyClass()
print(m1 is m2)
print(m1 is not m2)

m2=m1
print(m1 is m2)
print(m1 is not m2)

# one more example

"""k=100
print(k)
print(id(k))
s=100
print(id(s))

print(k==s)
print(k is s)"""""

# with list
list1 = [1, 2, 3, 4, 5, 6, 7]
print(4 in list1)
print(4 not in list1)

# with dictionary
dict = {1:"first",2:"second"}
print(3 in dict)
print(2 in dict)

# with tuple
tup1 = ('physics', 'chemistry', 1997, 2000)
print('hello' in tup1)
print('chemistry' not in tup1)
print(1997 in tup1)








