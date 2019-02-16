#program for clculator
'''
val1 = int(input("enter the first value\n"))
val2 = int(input("enter the second value"))
print("MENU \n1.option +\n2.option -\n3.option *\n4.option /\n5.option % \n 6.option quit")
ch=input("enter your choice")
while True:
 if ch=='1':
    print("This is addition")
    print("The sum is",val1+val2)
    val1 = int(input("enter the first value\n"))
    val2 = int(input("enter the second value"))
    print("MENU \n1.option +\n2.option -\n3.option *\n4.option /\n5.option % \n 6.option quit")
    ch = input("enter your choice")

 elif ch=='2':
    print("This is subtraction")
    print("The difference is",val1-val2)
    val1 = int(input("enter the first value\n"))
    val2 = int(input("enter the second value"))
    print("MENU \n1.option +\n2.option -\n3.option *\n4.option /\n5.option % \n 6.option quit")
    ch = input("enter your choice")

 elif ch=='3':
    print("This is multiplication")
    print("The multiplication is",val1*val2)
    val1 = int(input("enter the first value\n"))
    val2 = int(input("enter the second value"))
    print("MENU \n1.option +\n2.option -\n3.option *\n4.option /\n5.option % \n 6.option quit")
    ch = input("enter your choice")

 elif ch=='4':
    print("This is division")
    print("The division is ",val1/val2)
    val1 = int(input("enter the first value\n"))
    val2 = int(input("enter the second value"))
    print("MENU \n1.option +\n2.option -\n3.option *\n4.option /\n5.option % \n 6.option quit")
    ch = input("enter your choice")
 elif ch=='5':
     print("this is remainder\nthe remainder is",val1%val2)
     val1 = int(input("enter the first value\n"))
     val2 = int(input("enter the second value"))
     print("MENU \n1.option +\n2.option -\n3.option *\n4.option /\n5.option % \n 6.option quit")
     ch = input("enter your choice")
  if ch==6:
    print("quiting")
    break

#to find out that it is leap year or not
year=int(input("enter year"))
if year%4==0:
    print("it is leap year")
else:
    print("not a leap year")'''


#program for entering name ,tel and age
name=input("Enter your name")
while True:
 if name.isalpha()==True:
    break
 else:
    print("Incorrect name")
    name = input("Enter your name")
tel = input("Enter your telephone number")
while True:
 if tel.isdigit()==True:
    break
 else:
    print("your telephone number is incorrect")
    tel = input("Enter your telephone number")
age = int(input("enter your age"))
while True:
 if age>18:
      break
 else:
    print("your age is not sufficient")
    age = int(input("enter your age"))
print("Nice to meet you",name,"\nyour age is",age,"\nyour telephone number is",tel)








