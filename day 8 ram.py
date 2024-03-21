## ! eg:3
##def profile(name,age,place):
##    print(name,age,place)
##profile("RAM",22,"N N KUNTA")


# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything

##3.) we cannot write any code below return statement
##
##def f1(a,b):
##    c=a*b
##    return c
##print(f1(6,8))
##obj=f1(6,8)
##obj1=f1(4,6)
##
##
##def gracemark(object):
##    print(object+4)
##gracemark(obj)
##gracemark(obj1)

# 123

##def palindrome(n):
##    print(n)
##    
##a = int(input("enter the value:"))
##palindrome(a)

# ? problem:1
# def palindrome(n):
#
#string str(n)
# rev = str(n) [::-1]
#if string==rev:
#print(n, "Palindrome")
#else:
#print("Not palindrome")
#aint(input("Enter the value: "))
#palindrome(a)

# ? Based on the declaration of parameter
# functions are divided into 5 catagories

# postal args
# keywords args
# defalt args
# variable length args
# keyword variable length args

# * Positional args
#Eg:1;
##def profile(name, phone, mark):
##    txt ="My name is {}. My phone number is {}. I got {} marks."
##    print(txt.format(name, phone, mark))

##    profile(9704984013, "mani", 92)

# * Keyword args
# ! Eg:1
#? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
## funtions
##def profile(name,phone,mark):
##    txt="My name is{}. My phone number{}. I got{} marks."
##    print(txt.format(name,phone,mark))
##profile(name="ramesh",mark=100,phone=767095664)

#  * todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))
##profile(name = "ram", mark=99, phone=9876543210)

#* Default args
# Eg:1;
##def profile(name, phone, place="nandyal"):
##    txt = "My name is {}.My phone number is {}.I am from{}."
##    print(txt.format(name, phone, place))
##
##profile("mani",7842684013,"nandyal")
##
##def profile(name, phone, place="n n kunta"):
##    if(place=="nandyal" or place!="n n kunta" or place != "kadapa"):
##       txt = "My name is {}.My phone number is {}.I am from{}."
##       print(txt.format(name, phone, place))
##    else:
##         print("not eligible" )
##profile("ram",7842684013,)

# ! Exception
##def profile(name, phone, place="Kadapa"): # error --> because default args should not follow
##                                          # positional paramdu ctryjr
##    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
##     txt="My name is{}. My phone number{}. I got{} marks{}."
##     print(txt.format(name,phone,place))
##    else:
##        print("You are not eligible to Signup")
##profile("ram",9876543210)

# * variable length params
# ! eg:1

#Variable length params

#! Eg:1
# To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param
##name = "ram", 'name2', 'name3'
##def profile(*name):
##    for val in name:
##        print("My name is", val)
##profile("ram", 'name2', 'name')

## ! eg:2
##def profile(*name age):
##    for val in name:
##        print("my name is",val,"my age is",age)
##profile(28,"ram",'name2','name3,28') #error --> age has no args

##def profile(*age, name):
##    for val in name:
##        print("my name is",val,"my age is",age)
##profile(28,"ram",'name2','name3') 

# * keyword variable length args
# kwargs --> which is used to provide the args in the form of key value pair.

### ! eg:1

##def price(**price_list):
##    print(price_list)
##
##price(shirt=1000,iphone=800000)
##
##n = 5
##{1:1,2:4,3:9,4:16,5:25}
##
##d1 = {"a":100,"b":200,"c":300}
##d2 = dict(a=100,b=200,c=300)

##n = int(input("enter the number"))
##d1 = {}
##for val in range(1,n+1):
##    d1[val] = val**2
##print(d1)

#def dict1(n):
#    d1 = {}
#    for val in range(1,n+1):
#        d1[val] = val**2
#    print(d1)
#dict1(5)

# !----> object orinted programming
##class
##objects
##inheritance
##polymorphism
##abstraction
##encapsulation

# ! class is a blue print of an object
# l1 = [1,2,3,4,5,6,7]

# ? eg:1
#class c1:
#    name1 = "ram"
#    print(name1)

# ? eg:2
#class person:
#    name = "ram"
#c = person()
#print(c.name)

# ? eg:3
# create of a method
# when the function is created with a class is called as method

##class person:
##    def display(person): # it is a method
##        print("hello welcome to classes")
##
##p = person()
##p.display()

#? eg:4
# ! method with parameter
##class person:
##    def display(person,name,age):
##        print(name,age)
##p = person()
##p.display("ramesh",22)

# ! eg:5
##class person:
##    fname = "ram" # attribute or staic variable
##    lname = "y"
##
##    def frist_name(self):
##        print(self.fname)
##
##    def full_name(self):
##        print(self.fname+" "+self.lname)
        
##p = person1()
##p.frist_name()
##p.full_name()

# ? eg:6
# constructors -->__init__()
# this is a spcial method which has the ability to execute itself without
#calling it manullay thorugh the process of instantiation
#class profile:
#    def __init__(self):
#        print("hey")
#p = profile()
#p.d1() # execution of construction through this process



































