#for multiplication
'''
num=int(input("enter any number"))
for x in range(1,11):
    print(num,"*",x,"=",num*x)


#adding input in the empty list

list=[input("enter any elements of list")]
num=int(input("enter no of elements added"))
for i in range(num):
    list.append(input("enter new value"))
    print(list)'''



# program to display only even number among a list


list=[737445,566,7,78,654,33,344,45,56,7,8,8889,3,2,3,22]
even_num=[]
for num in list:
    if num%2==0:
        even_num.append(num)
print("list", list)
print("even list", even_num)
'''
#removing from list

list=[456,32,65,32,454,445,55,45,55,78]
print(list)
num=int(input("elements  rhat can be removed"))
for i in list:
    if i==num:
        list.remove(i)
print("new list",list)



