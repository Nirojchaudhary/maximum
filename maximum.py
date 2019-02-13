'''
#program for taking 5 marks input from the user and then find the sum
print("enter the marks obtained")
mark1=int(input("sub1"))
mark2=int(input("sub2"))
mark3=int(input("sub3"))
mark4=int(input("sub4"))
mark5=int(input("sub5"))
sum=mark1+mark2+mark3+mark4+mark5
print("sum=",sum)




#program for counting the desired string
string="hello i hope you are having a nice day"
print(string)
str=input("what u want to count")
print("total number of string =",string.count(str))



#finding min and max from the list
list=[666,23,4445,32,54,65,767,88,9,1,77]
print("the maximun number of the list is=",max(list))
print("the minimum number of the list is=",min(list))
'''

st=input("what string you want to write")
print(st.upper())
st=st.replace(st,input("replacing string"))
print(st.upper())