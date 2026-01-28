#Sets (collection of welldefined objects)
#use curly brackets for that
#set ma replace nhi kar sakhte ak dafa jo index assign hoo jaye (5 ke jagha 8 nhi kar sakhte)
# s={1,5,44,8,9,4}
# print(s)
# s.add(3)
# print(s)
#for multi value add
# s.update([3,7,8,9,80])
# print(s)
# s.remove(4)
# print(s)
# s.discard(4)#value remove he hoti hai aghr avlue na hoo to error nhi aaye gya
# print(s)
#clear all element
# s.pop()
# print(s)
# s.clear()
# print(s)
# a=s.copy()
# print(a)

# name={"Sidra","Malika","Rizwan","Naseem","Iram"}
# print(name)

# n={"Sidra",89,True,5.90,"Moon"}#order mantain nhi hoo gya everytime change hoo gyi value
# print(n)
# sidra=set({})
# print(type(sidra))
# for value in n:
#     print(value)

# s1={3,89,90,56,3,45,26}
# s2={1000,76,1,3,45,2}
# print(s1.union(s2))#join kar dye gya dono ko
# print(s1.intersection(s2))#common dye gya 
# print(s1.symmetric_difference(s2))#jo common nhi aaye vo wali print hoo gyi
# print(s1.symmetric_difference_update(s2))
# print(s1.isdisjoint(s2))#aghr common na hoo dono ma phir true hoo gya 
# print(s1.issuperset(s2))#sare element first am majhood hoo
# print(s2.issubset(s1))

#Dictionaries (mapping hoti hai )
# dic={
#     "Sidra":"Human being",
#     "Pencil":"Object",
#     2:"Number",
# }
# print(dic[2])
# print(dic)
# print(dic.get("Pencil"))
# print(dic.keys())
# print(dic.values())

ep1={1:90,4:89,5:67}
ep2={34:100,56:78}
ep1.update(ep2)
print(ep1)
print(ep2)
print(type(ep1))
ep1.pop(34)
print(ep1)
ep1.popitem()#last value ko remove kar data hain
print(ep1)
ep3=ep1.copy()
print(ep3)
del ep1[4]
print(ep1)
ep1.clear()
print(ep1)