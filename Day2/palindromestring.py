# name = "arora"
# start = 0
# end = name.length() - 1
# while(start < end):
#     if(name[start] == name[end]):
#         start = start + 1
#         end = end - 1

#-------------------------------------------------------------------------

# import math
# pi = 3.1415
# r = float(input("Enter radius of sphere: "))
# volume = (4/3)*math.pi*r**3
# print("Volume of sphere is : ",round(volume,3))
# print("Volume of sphere is : %.3f" %volume)

#----------------------------------------------------------------------

'''name = "Shriram"
age = 21
print("I am " + name + " and I am " + str(age) + " years old.")
print("I am %s and I am %d years old."%(name,age))
print("I am",name,"and I am",age,"years old.")
print(f"I am {name} and I am {age} years old.")
print("I am {} and I am {} years old.".format(name,age))'''

#------------------------------------------------------------------------
# mylist = [['Shriram','Kumawat']]

# IN python we implement a stack by using list data structures
#slicing 
#split

# def arithmatic(a,b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     return add,sub,mul
# result = arithmatic(7,9)
# print("Result : ",result)

#how to pass function as argument in lambda function 
# when we read large amount of data then we go for generator function
'''
1.kwargs
2.args
3.decorators
4.generators
5.lambda
6.map
7.reduce
8.zip
9.
'''

def func(*arg):
    for i in arg:
        print(i)

func('shriram','ankit','aditya')

def func(*)
