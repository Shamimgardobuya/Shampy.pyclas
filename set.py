 python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x=[1,2,3,4,5]#list
>>> y=[6,7,8]
>>> x.append(6)
>>> x
[1, 2, 3, 4, 5, 6]
>>> x.remove(5)
>>> x
[1, 2, 3, 4, 6]
>>> y=[1,2,3,4,5]
>>> y.append(6)
>>> y
[1, 2, 3, 4, 5, 6]
>>> y.append(7)
>>> y
[1, 2, 3, 4, 5, 6, 7]
>>> y.append(8)
>>> y
[1, 2, 3, 4, 5, 6, 7, 8]
>>> z=["a","b","c","d"]
>>> r=z+y
>>> r
['a', 'b', 'c', 'd', 1, 2, 3, 4, 5, 6, 7, 8]
>>> z.extend(y)
>>> z
['a', 'b', 'c', 'd', 1, 2, 3, 4, 5, 6, 7, 8]
>>> 
[1]+  Stopped                 python3
student@student-ThinkPad-X250:~$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x=[1,2,3,4,5]
>>> y=[6,7,8,9]
>>> x.extend(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> x.extend(y)
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> z=[11,12,13,14]
>>> w=x+z
>>> w
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
>>> w.insert(8)#insert a at index 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert expected 2 arguments, got 1
>>> w.insert(1,'a')
>>> w
[1, 'a', 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
>>> a=[30,20,60,10,100]
>>> a.sort()
>>> a
[10, 20, 30, 60, 100]
>>> a[-1:]
[100]
>>> a[-1::]
[100]
>>> a
[10, 20, 30, 60, 100]
>>> a.sort(reverse=True)
>>> a
[100, 60, 30, 20, 10]
>>> a.sort(reverse=False)
>>> a
[10, 20, 30, 60, 100]
>>> a.remove(60)
>>> a
[10, 20, 30, 100]
>>> a.pop(60)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
>>> #pop takes indices
>>> a.get(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'get'
>>> print(a[1])
20
>>> a[1]
20
>>> #how to access a value in a list
>>> fruits=["apple","mango","pineapple","grapes","banana"]
>>> for fruit in fruits:print(fruit.upper())
... 
APPLE
MANGO
PINEAPPLE
GRAPES
BANANA
>>> for fruit in fruits:print(fruit.lower())
... 
apple
mango
pineapple
grapes
banana
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'grapes', 'mango', 'pineapple']
>>> f=[10,20,30,40,50]
>>> for x  in f :print(x+10)
... 
20
30
40
50
60
>>> for fruit in fruits:print("Such an amazing "fruit)
  File "<stdin>", line 1
    for fruit in fruits:print("Such an amazing "fruit)
                                                ^
SyntaxError: invalid syntax
>>> 
>>> f=[10,20,30,40,50,60]
>>> for x  in f :print(x*3)
... 
30
60
90
120
150
180
>>> for x  in f :print(x**3)
... 
1000
8000
27000
64000
125000
216000
>>> m=[]
>>> m=(x*3 for x in f)
>>> m
<generator object <genexpr> at 0x7fb7cdd1fa50>
>>> m=[x*3 for x in f]
>>> m
[30, 60, 90, 120, 150, 180]
>>> #nice!in list comp,use square brackets  number_list = [ x for x in range(20) if x % 2 == 0],create empty list.
>>> x=[12,13,14,15]
>>> y=tuple(x)
>>> y
(12, 13, 14, 15)
>>> y.len()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'len'
>>> 
KeyboardInterrupt
>>> len(y)
4
>>> t=(1,2,3,4)
>>> z=t+y
>>> z
(1, 2, 3, 4, 12, 13, 14, 15)
>>> v=("a","s","d","f")
>>> t+v
(1, 2, 3, 4, 'a', 's', 'd', 'f')
>>> t*5
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> #checking 5 in t
>>> 5 in t
False
>>> #changing 
>>> for v in t:print(v)
... 
1
2
3
4
>>> 
[2]+  Stopped                 python3
student@student-ThinkPad-X250:~$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x={1,2,3,,5}
  File "<stdin>", line 1
    x={1,2,3,,5}
             ^
SyntaxError: invalid syntax
>>> x={1,2,3,,5}
  File "<stdin>", line 1
    x={1,2,3,,5}
             ^
SyntaxError: invalid syntax
>>> x={1,2,3,4,5}
>>> x.add(6)
>>> type(x)
<class 'set'>
>>> x.remove(6)
>>> x
{1, 2, 3, 4, 5}
>>> x.pop([5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop() takes no arguments (1 given)
>>> x.remove(8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 8
>>> x.discard(8)
>>> x
{1, 2, 3, 4, 5}
>>> #union brings everything              #intersection -same values in two sets,#difference checks for the elements,i don't have,x.difference(y)
>>> y={"a":1,"b":2,"c":3,"d":4}
>>> y.keys()
dict_keys(['a', 'b', 'c', 'd'])
>>> y.values()
dict_values([1, 2, 3, 4])
>>> "a" in y
True
>>> value(3) in y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'value' is not defined
>>> #checks for keys in 
>>> for value in y.values():print(value)
... 
1
2
3
4
>>> for value in y:print(value)
... 
a
b
c
d
>>> y["a"]
1
>>> y["e"]=10
>>> y
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 10}
>>> y["f"],["g"]


