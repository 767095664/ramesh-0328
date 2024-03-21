#s1 = input("enter string")
#print(type(s1))         
#print(s1.replace('h','H','d',))
#fst = s1[0].upper()
#lst = s1[-1].upper()
#print(fst+s1[1:len(s1)-1]+lst)

#n = 128
#i = 0
#while n!=0:
#    rem = n%10
#    print(rem)
#    n = n/10
#for i in str(n):
#     print(i)
#temp = n
#tr1 = ""
#while n!=0:
#    rem = n%10
#    check= temp % rem
#    if check==0:
#        print("yes")
#    else:
#        print("n0")
#        n = 0

#n = 220
#temp = n
#f1 = 0
#while n!=0:
#    rem = n%10
#    if rem == 0:
#f1=1   
#break
#check= temp % rem
#if check!=0:
#f1 = 1
#n = n//10

#l1 = [8,9,0,7]
#l2 = [3,4,5,6]
#l3 = []
#print(l1[0]+l2[0],l1[1]+l2[1])
#for val in range(len(l1)):
#    ans = (l1[val]+l2[val])
#    l3.append(ans)
#    print(l3)
#    print(l1[val]+l2[val])

# !----> set
#? charctristics of set
#1.) set can be created using {}
#2.) the elements inside set are not indexed
#3.) does not allow duplicate values
#4.) it unordered
#5.) heterogenous
#6.) mutable or changable

# Eg:1
#s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
#print(s1)

#eg:2
#s2 = {5,8,98,[9,0]}
#print(s2) ---> error

#Eg:3,
# min(), max(), len()

# Eg:4,
# ? to add element inside set
#s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
#print(s1)

# update()
##s1.update(9, 0)
##print(s1)

#To deleat element inside set

#s1 = {8, 78, 67, 'u'}

#pop() # to deleat one element randomly
##s1.pop()
##print(s1)

#remove()
#s1.remove(78)
#print(s1)

#discard()
##s1.discard(67)
##print(s1)

# clear()
# l1 = {}
# print(type(l1)) ----> datatype is dict

#S1 = set() # to create empty set
#print(type(s1))

#s1 = {8,9,0}
#s1.clear()
#print(s1)

#del s1
#print(s1)

#  *---> JOIN the sets

#s1 = {9,0,8}
#s2 = {9,90,"card"'t',56}
# union() --> to ombine 2 sets
#s3 = s1.union(s2)
#print(s3)

#* intersection() ---> to get common element inside set
#s1 = {4,5,6}
#s2 = {4,5,7,8}
#print(s1.intersection(s2))

#s1 = {4,5,6}
#s2 = {5,6,7,8}
#print(s1.difference(s2))
#print(s2.difference(s1))
#print(s1.symmetric_difference(s2))

# isdisjoit(), issubset(), issuperset()

#s1 = {8,9,0}
#s2 = {6,7,8,9,0}

#print(s1.issubset(s2))
#print(s2.issuperset(s1))

#s1 = {1,2,3,4,5}
#s2 = {3,2,7,8,9}

# n1 = {1,2,3} --> s1

#for val in s1:
#    if val in s2:
#        str1 = "its joint set"
#print(str1)

# ? o/p --> its a joinset


# ! ------> dictionary

# eg:1
#d1 = {1:100,'a':200,4.5:"hello"}
#print(d1)
#print(len(d1))
# ? char of dictionary
#1) have to be surrounded by {)
#2) It have to be in the form of key, value pair
#3) It is mutable
#4) duplicate keys are not allowed, duplicate values are allowed
#5) It is unindexed
#6) It is ordered
#7) Key does not allow mutable datatypes, values allow mutable 

#d1 = {1:100,2:200,3:300,4:400}
# * to access element in dictionary

#print(d1)
#or
# to access the values,have to use key
#print(d1[1]) # o/p--> 100

##some common functions
#len(), min, max()
#print(min(d1))
#print(max(d1))

# ? To find min, max based on values. T
#print(min(d1.values()))
#print(max(d1.values()))

# ? dictionary based functions
# to add element(key and value pair) in dict
#d1 = {1:100,2:200,3:300,4:400}
#d1[5] = 500
#print(d1)

# ? to replace a value in
#d1 = {1:100, 2:200, 3:300,4:400}
#d1[2]="mango"
#print(d1)
#delete element from dictionary

#d1 = {1:100, 2:200, 3:300, 4:400}
#popitem()
#d1.popitem()
#print(d1)


#pop
#d1.pop(2) #2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 ditionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple","b":"ball","c":"cat"}
#d1.update(d2)
#print(d1)

# get() --> used to get the value from a key
#d1 = {1:100, 2:200, 3:300, 4:400}
# print(d1[90])
#print(d1.get(90))

# to print aii keys()
#print(d1.keys())
#print(type(d1.keys()))

# to print all the values
# print(d1.values())

# * iterating dictionary
#for val in d1.values():
#    print(val)

# to get both key and values
#for key, val in d1.items():
#    print(key, val)

#mech_name = ["name","name2","name3"]
#mech_age = [33,55,67]
#mech_mark = [89,90,60]
#mech_email = ["name2@gmail.com","name3@gmail"]

#mech = {
#    "student1":{
#        "name":"name1"
#        "age":24,
#        "mark":89,
#  },
#   "student2":{
#        "name":"name2"
#        "age":24,
#        "mark":89,
#  },
#   "student3":{
#        "name":"name3"
#        "age":24,
#        "mark":89,

#! Problem:1

#n= input()
#1.) Swap elements in String list
# The original list is: ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps: ['efg', 'is', 'bGst', 'for', 'eGGks']

#n = int(input("enter num of times:"))
#for val in range(n):
#    value = eval(input("enter the value"))
#    print(n)

#n = int(input("Enter num of times: " ))
#integer=[]
#float_value = []
#string=[]

#for val in range(n):
#    value = eval(input("Enter the values: "))
#    if type (value)==int:
#        integer.append(value)
#   elif type (value) == float:
#        float_value.append(value)
#   elif type(value) == str:
#        string.append(value)
#    else:
#        print("Pls provide data in int, float, string")
#print(integer)
#print (float_value)
#print(string)


# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}

# Return a set of elements present in Set A or B, but not both
#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}

#for val in set1:
#    if val  in set2:
#      str1= {"20,70,10,60"}
#print(str1)

# ! ---> problem 3
#l1 = [1,2,3,4] # key
#l2 = ["a","b","c","d"] # value
#d1[l1[0]] =l2[0]
#print(d1)


























