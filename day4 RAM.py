# --> while loop

#eg:1
#i = 20
#while i<31:
#    if i ==27:
#        break
#    print(i)
#    i+=1


#:2
#    i = 20
#    while i<31:
#        print(i)
#         i+=1

#        if i==27:
#            break

#eg:3

#i= 20
#while i<31:
#    print(i)
#    if i==27:
#        break
#    i+=1

#eg: 4
#i = 20
#while i<31:
#    if i==27:
#        print(i)
#        break
#    i+=1

#--> continue

#i = 20
#while i<31:
#    if i==27:
#        continue
 #   print(i)
 #   i=i=1

# eg:5

#i = 20
#while i<31:
#    i=i+1
#    if i==27:
#        continue
#    print(i)

#eg: 6
# while to iterate from 12 to 22
# find the sum of all numbers
#i = 12
#sum=0
#while i<=22:
#    sum=sum+i
#    i=i+1
#    print(sum)

#eg:7
# find the average of value from 20 to 25

#i = 20
#sum = 0
#count=0
#while i<=25:
#    sum = sum+i
#    count+=1
#   i+=1
#print(sum/count)

# !-------> nested for loop
# eg : 1

#for row in range(1,3+1):
#   for col in range(1,4+1):
#    print(row,col)

#eg:2
# * * * *
# * * * *
# * * * *
# * * * *

#for row in range(4):
#   for col in range(4):
#    print(row,col)

#for row in range(4):
#   for col in range(4):
#    print("*,%,#,*,),@,%",)

#for row in range(4):
#   for col in range(4):
#    print("*,&",end=" ")

#rows = int(input("enter the row")
#cols = int(input("enter the cols")

#for row in rang(rows):
#    for col in range(cols):
#           print("*",end=" ")
#    print()

#sum = 0
#for row in range(5):
#    for col in range(5):
#        sum= sum+1
#        print(row, end=" ")
#    print()

#for row in range(0,6):
#    for col in range(0,row):
#        print("*", end=" ")
#    print()

#for row in range(0,6):
#    for col in range(0,row):
#       print("*", end=" ")
#    print()


#for row in range(0,6):
#    for col in range(row,6):
#        print("*", end=" ")
#    print()


# for row in range(5):
#    for col in range(5):
#        if col==0 or col==15-1 or row ==0 or row ==5-1:
#          print("*", end=" ")
#    else:
#        print(" ", end=" ")
#    print()

#for row in range(0, 5):
#    for col in range (0, 6):
#        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()

# ----> data type
# primary

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary


# ---> list


#1.) if the collection of elements are sorounded by square brackets, it is considered
# to be list

#! eg:1
# 11 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]

#charactristics of list

#1.) list have to be sorrrounded by []
#2.) It is mutable (the elements in the list are changable)
#3.) Every element inside list is indexed
#4.) The elements inside list will be ordered format
#5.) It can hold duplicate values
#6.) Its heterogenous

# to access the element in list
#l1 = [1,4,1,7,89,7,75,"p","i"]
#print(l1)

#----> Indexing

# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value
# We have 2 types of indexing
# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side

# ---->Positive indexing

# list 1 = [1,4,1,7,89.7,7.5,"p","i"]
#print(lst1[0])
#print(lst1[4])
#print(lst1[20])

# ---->Negative indexing

#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1[-1])
#print(lst1[-5])

# ? -----> slicing
#lst1 = [1,4,1,7,89.7,7.5, "p","i"]
# lst1[start_index:end_index:step]

#print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[3:6])
#print(lst1[:5])
#print(lst1[3:])
#print(lst1[:])

#print(lst1[0:7:1]) # lst1[:7] --> both are same
#print(lst1[0:7:2])

# trail = int(input())

#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1[-1:4])
#print(lst1[-4:-1]) --> []
#print(lst1[-7:-1:2])
#print(lst1[-7:-1])

#! to insert to add element inside list

# append()--> used to add element at last position of list
# 11 = [9, 8, 0, 6]
# 11.append("car")
#print(l1)








































