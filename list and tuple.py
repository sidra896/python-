#List (Different type ka data store hoo sakhta hai )
# marks=[23,89,90,100]
# print(marks)
# print(type(marks))

# name=["naseem","rizwan","iram","sidra","malika"]
# print(name)

# list=[20,"Sidra",90,"Semi",True]
# print(list)
# print(list[0])
# print(list[4])
# print(list[-1])#len(list)-1kar dye gye 5-1=4
# print(list[-3])#5-3=2
# print(type(list))

# fruits=["Mango","Orange","Banana","Apple","Cheery"]
# print(fruits)
# for f in fruits:
#     print(f)
# print(len(fruits))

#list Constructor() list() ek built-in constructor hai jo kisi iterable (jaise tuple, string, set) ko list me convert kar deta hai.
# myfruits=list(("Mango","Orange","Banana","Apple","Cheery"))
# print(myfruits)
# print(type(myfruits))

# fruit=("Mango","Orange","Banana","Apple","Cheery")
# print(fruit)
# print(type(fruit))
# f=print(list(fruit))#aghr ase kare gye phir type none hoo gyi beacuse print none return karta hain
# print(type(f))

#Check karna hoo list ma yeh hai yeh nhi 
# list=[20,"Sidra",90,"Semi",True]
# if 8 in list:
#     print("Yes")
# else:
#      print ("No")
#yeh ase bi kar sakhte hai user se input lee kar 
# list=[20,"Sidra",90,"Semi",True,54,"hello","love you"]
# item=input("enter the you want to check ").strip().lower()
# if item in [str(x).strip().lower() for x in list ]:#str se data type change hoo jy gye 
#     print("Yes")
# else:
#      print ("No")
# print(list[:])
# print(list[1:-2])
# print(list[: :2])

# name="sidra"
# print(list(name))
# print(tuple(name))
# print(set(name))

# list=[i*i for i in range(10) if i%2==0]
# print(list)

# numbers = []  # Empty list

# while True:
#     n = input("Enter a number (or 'q' to quit): ")
#     if n.lower() == 'q':  # User can type 'q' to stop
#         break
#     if n.isdigit():
#         numbers.append(int(n))  # Convert to int
#     else:
#         print("Please enter a valid number")

# # List comprehension to get squares of even numbers
# squares = [i*i for i in numbers if i%2==0]

# print("Squares of even numbers:", squares)

# list=[20,"Sidra",90,"Semi",True,54,"hello","love you"]
# list[1]="Shazadi"
# print(list)
# list.append(8)
# print(list)
# list.insert(2,45)


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)
# thislist.sort()
# print(thislist)


# list=[90,56,4,87,43,67,100,1,90,4,6,7,4,12,47]
# print(list)
# list.sort()
# print(list)
# list.reverse()
# print(list)
# print(list.index(43))
# print(list.count(4))
# print(list.copy())

# num=[23,89,78,5,0,3,23,8]
# print(num)
# n=[90,8,333]
# num.extend(n)#num ko open karo or jo n ma hai us ko num ma pass kar doo
# print(num)
# #ak or tarah se bi merge kar sakhte hai
# print(num+n)


# numbers=[]
# while True:
#     n=input("Enter a number,(or q for stop)")
#     if n.lower()=="q":
#         break
#     if n.isdigit():
#         numbers.append(int(n))
#     else:
#         print("Enter a valid number")
# print(numbers)
# numbers.sort()
# print("the sorted list is",numbers)

#Tuple(A tuple is a collection which is ordered and unchangeable.)
# tup=(1,4,3,4,5,7)
# print(type(tup),tup)

#Aghr hum sirf ak value dye gye to class int hoo gyi 
# tup=(2)  #yeh tupe he show hoo phir hume (2,)ase likhna hoo gya 
# print(type(tup))

# my_tuple = list((10, 20, 30, "Sidra", True))
# print(my_tuple)

n=(3,9,78,45,12,56,34,9)
print(n[3])
print(n[3:7])
print(n[-3])
print(n[1:len(n):2])
print(n.count(9))
print(n.index(45))