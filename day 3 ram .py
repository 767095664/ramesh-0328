# eg 3

#length = float(input("enter the lendth of rectangula"))
#breath = float(input("enter the breath of rectangular"))
#if length==breath:
#     print("its a square")
#else:
#      print("tits not square")

# eg 4

#n = int(input("enter the number "))
#if n%5==0 and n%7==0:
#    print("yes")
#else:
#    print("no")

#eg 5

#price = int(input("enter the price"))
#amount = 0
#if price>=500000:
#    discount = 500000*(6/100)
#    value = price+discount
#    amount=value*(15/100)
#    print(value+amount)
#else:
#    tax = price*(5/100)
#    total = price+tax
#print("the anroad cost of bike is: ",total)

#if elif
#eg:1
#a = 7
#b = 9
#c = 3
#if a>b and a>c:
#    print("a is greter")
#elif b>a and b>c:
#    print("b is greater")
#else:
#    print("c is greater")

#mark = int(input("enter marks: "))
#if mark>=80 and mark<=100:
#    print("a")
#elif mark>=60 and mark<80:
#    print("b")
#elif mark >=40 and mark<50:
#    print("c")
#else:
#    print("fail")

# ! --> short hand if else
# eg: 1
#a = 9
#b = 60
#if a>b:
#     print("a")
#else:
#    print("b")

#? --> using short hand if else
# * rules
# 1.) statement inside the if conditio have to be present at frist
# 2.) elif cannot be used in short hand if else
# 3.) always if have to end with

# print("a") if a>b else print ("b")

# ! code to check the give char is vowel or consonent
# char = input("enter the char")
 
 # if char=="a" or char  ==>'e' or char =='i' or char =='o' or char =='u'
 #    print("is a vowel")
 #else :
 #    print("its consonent")

 # ? or

#str1 = "aeiouaeiou"
#if char in str1:
#    print("vowel")
#else:
#     print("consonet")

# ! ---> elif ladder ueing short hand if else
#eg:1
# ? find greatest among 3 variable using short hand if else
#a = 8
# b = 5
# c = 9

#print("a is grater ") if a>b and a>c else print("b is grater")
#if b>a and b.c else print("c is greater
#Looping

# Looping can be implemented using
# for loop
# while loop


#--->for loop
# for loopis used to iteration, if we know the number of times the loop have to run
# It is used to iterate the iterables eg(string, list, tuple, etc...,)


#todo--> Syntax for loop
#for syntax in 
#for(i=0;i<10;i++){
#  print("hello");


 # ! for syntax in python
 #for userdefined_variables in range(start, end, step):default setup value is 1
   #  statement
  #   statement
 #    statement

 #Eg:1
 
#To print the values from 1 to 100 using for loop

#for i in range(0,10): (n ,n-1)
#       print(i)
#       print("hello")

# ? eg:2

#for val in range(1,15,3):
 #     print(val)



#for val in range(10, 0, -1):
#   print(val)
   
#for val in range(10, 0, -2):
#   print(val)
   
#for val in range(10, 0, 1):
#   print(val)

# ? eg:4
# ! print the output of 7th multiplication table from 21 to 43
#for val in range(1,10+1,):
#--> method: 2
#    print('7','*',value,'=',value*7)
#    ans="7 * {} = {}"
#    print(ans.format(val, val*7))

# ?eg:5
# break --> used to teerminate the loop

#for val in range(1,1000):
 #   print(val)
  #  if val ==5000:
  #      break

# ? eg:7
#for val in range (1,100):
#    if val ==50:
#        print(val)
#        break

# ! continue
#eg:1
#for val in range (1,100):
#    if val ==70:
#       continue
 #   print(val)

# ! PRACTISE problem
# ? print the even number between 20 to 40
#for val in range(20,40):
#    print("the even number between 20 to 40 ")

#----> while ioop
# while is used when we do not know the number of times the loop have to run
# ? to iterate the non iterable element while loop is used

# todo syntax

#initialisation
# while condition
#   statement
#   incre or decre

#! eg: 1
# to interate number from 1 to 10#i = 0
#while i<11:
#    print(i)

# for loop practise
# write a program to display sum of odd number and even
# number that fall between
# 12 and 37(inciuding both numbers)

#n = 12
#while n<37:
#    print(n)


















































  
