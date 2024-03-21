# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

##
##s1 = "hello how are you"
##s2 = "hello how is"

##s1 = s1.split(" ")
##s2 = s2.splite(" ")

##for val in s1:
##    if val not in s2:
##        print(val)
##for val in s2:
##    if val not in s1:
##        print(val)

# 3.)Wrire a code print the 8th fibanochi number
# 0,1,1,2,3,5,8

##n1 = 0
##n2 = 1
##ans = 0+1 ==>1
##
##n1 = 1
##n2 = 2
##ans = 1+2 ==>3
##
##n1 = 2
##n2 = 3
##ans = 2+3=5
##
## ! find the 8th fibanochi number
##num = 8
##n1 = 0
##n2 = 1
##
##for val in range(num):
##    ans = n1+n2
##    print(ans)
##    n1 = n2
##    n2 = ans

## ! constructors
# ? eg:2

##class profile:
##    def __init__(self):
##        print("hello world")
##
##obj = profile()
##obj.__init__()

# ? eg:3
# * unparameterised construcion
##class profile:
##    def __init__(self,id,name,age):
##        print(id,name,age)
##
##obj = profile(2,"ram",22)

# ? eg:4
##class c1:
##    name = "ram"
##    place= "n n kunta"
##
##    def m1(self):
##        print(self.name,self.place)
##
##object =c1()
##object.m1()

##class c1:
##    email = "ramlocal2511@gmail.com"
##    
##    def m1(self):
##        name = "ram"
##        place= "n n kunta"
##        print(name,place)
##        print(self.email)
##
##object =c1()
##object.m1()

# ? eg:5
##class c1:
##    def m1(self):
##        name = "ram"
##        age = 22
##        return name,age
##    def display(self):
##        # ! print(name,age)
##        # ! print(self,name,self.age)
##        print(self.m1())
##object = c1()
##object.display()

# ? eg:6
##class class1:
##    def __init__(self):
##        self.name = "ram"
##        self.email = "ramlocal2511@gmail.com"
##
##    def display(self):
##        print(self.name,self.email)
##
##c1 = class1()
##c1.display()

# ! ----> inheritance
# The process of utilising the methods and attributes of parent class
# throught the object of child class it is called as inheritance

#? 5 types of Inheritance
#Single Inheritance
#Multilevel Inheritance
# Multiple Inheritance
# Hybrid Inheritance
# Heirarichal inheritance

# *Single Inheritance
#? It has only one parent class and only one child class

# eg:1
##class parent:
##    def m1(self):
##        print("Iam parent class")
##
##class child:
##    def m2(self):
##        print("Iam child class")
##obj = parent()
##obj.m1()
##
##obj = child()
##obj.m1()

# eg:2

##class c1:
##    def _init__(self):
##        print("Iam constructor from parent class")
##class child1(c1):
##    pass
##obj = child1()

# ! eg:3
##class parent:
##    name = " ram"
##
##
##class child(parent):
##    name = "name1"
##    
##    def display(self):
##        print(self.name)
##
##d = child()
##d.display()

# ! mil
#! Multilevel inheritance
# ? Eg:1
##class voice:
##    def sound(self):
##        print("All the animals have their own voices")
##        
##class dog(voice):
##    def dog_voice(self):
##        print("bark")
##        
##class cat(dog):
##    def cat_voice(self):
##        print("Meow")
##        
##class parrot(cat):
##    def parrot_voice(self):
##        print("speak")
##
##all = prrot()
##all.dog_voice()
##all.cat_voice()
##all.sound()
##all.parrot_voice()
## ! eg:2
##class honda_city:
##    def honda_city_engine_specs (self, cc, Hp, torque, fuel type, num_of_piston):
##        print(cc, Hp, torque, fuel_type, num_of_piston)
##def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
##    print(color, weight, height, length, vehicle_type)
##class amaze:
##def amaze_engine_specs(self, cc, Hp, torque, fuel_type, num_of_piston):
##    print(cc, Hp, torque, fuel type, num_of_piston)
##def amaze_body_specs (self, color, weight, height, length, vehicle_type):
##    print(color, weight, height, length, vehicle_type
##
##honda = honda()
##honda.honda_city_engine_specs(1500,230,2979,"petrol",4)
##honda.civic_body_specs("white",2000,5.5,8,"hatchback")
##                      
### Multiple Inheritance
## #? It has multiple parent and 1 child
##class while_pertol:
##    def function_w(self):
##        print("used to Airplans")
##
##class Organic_petrol:
##    def function_o(self):
##        print("used for Bike, cars")
##class premium_petrol:
##    def function_p(self):
##        print("spots cars, bikes")
##class petrol(while_pertol, Organic_petrol, premium_petrol):
##    def defanition(self):
##        print("Petrols types")
##p=petrol()
##p.defanition()
##p.function_o()
##'''
##'''
### Eg:2
### MRO---> Method resolution Order
##class addition:
##    def add(self, a, b):
##        print(a+b)
##    def mul(self,a,b):
##        print(a%b)
##class subract:
##    def sub(self, a, b):
##        print(a-b)
##class multiply:
##    def mul(self, a, b):
##        print(a*b)
##class division(addition, subract, multiply):
##    def div(self, a, b):
##        print(a/b)
##
##       
##calc=division()
##calc.add(3,4)
##calc.mul(4,2)
##
### ! Heirarical inheritance
##
##LE - 326 K. RAMESH
##2:29 PM (1 minute ago)
##to me
##
##class honda (civic):
##    pass
##
##honda = honda()
##honda.honda_city_engine_specs(1500,230,2979,"petrol",4)
##honda.civic_body_specs("white",2000,5.5,8,"hatchback")
##                       
##       
##'''
##'''
### Multiple Inheritance
## #? It has multiple parent and 1 child
##class while_pertol:
##    def function_w(self):
##        print("used to Airplans")
##
##class Organic_petrol:
##    def function_o(self):
##        print("used for Bike, cars")
##class premium_petrol:
##    def function_p(self):
##        print("spots cars, bikes")
##class petrol(while_pertol, Organic_petrol, premium_petrol):
##    def defanition(self):
##        print("Petrols types")
##p=petrol()
##p.defanition()
##p.function_o()
##'''
##'''
### Eg:2
### MRO---> Method resolution Order
##class addition:
##    def add(self, a, b):
##        print(a+b)
##    def mul(self,a,b):
##        print(a%b)
##class subract:
##    def sub(self, a, b):
##        print(a-b)
##class multiply:
##    def mul(self, a, b):
##        print(a*b)
##class division(addition, subract, multiply):
##    def div(self, a, b):
##        print(a/b)
##
##       
##calc=division()
##calc.add(3,4)
##calc.mul(4,2)
# ! Heirarical inheritance

#! Hybrid inheritance
#? The combination of above 4 inheritance is called Hybrid inheritance
##class c1:
##    def m1(self):
##        print("Class1")
##class c2:
##    def m2(self):
##        print("class2")
##        
##class c3:
##    def m3(self):
##        print("Class 3")
##class c4:
##    def m4(self):
##        print("Class 4")
##        
##class c5:
##    def m5(self):

##→ Polymorphism
##
##?poly many, morph> form
##A function which has the ability to perform more than 1 functionality
##then it is considered to be as plioymorphism
##
##Ploymorphism in builtin functions
##len() which is used to find the length of list, tuple, dict etc..
##index()
##max()
##min()
##count()
##pop()

#* Ploymorphism in operators
#+
# print(8+8)
# print("k"+'1')
#print([1,2,3]+[5,6])


# print(6*7)
#11 (12,3,4,5,6)
# print(*11)
# def f1(*args)
#11 [1,2,3,4]
#print(11*10)

# Ploymorphism in classes
# We can achieve polymorphism in 2 ways
#1.) Method overloading it is not possible in python
#2.) Method overriding

#) Tasks
# Write the code for the belwo tasks using function
#1.) d1 {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'
#2.) Find then 67, is strong number or not

#3.) 11 [1,2,3,4,5,6]
#n=2 --> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]














