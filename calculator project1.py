from tkinter import *
from tkinter import ttk
def click(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def clear():
    global operator
    operator=""
    text_input.set("")
def equal():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""


root=Tk()
root.title("Calculator")
root.config(background='black')
operator=""
text_input=StringVar()
display=Entry(root,font=("bold",26,),textvariable=text_input,bd=30,bg='green')
display.grid(columnspan=4)
one=Button(root,text="1",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click(1))
one.grid(row=1,column=0)
two=Button(root,text="2",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click(2))
two.grid(row=1,column=1)
three=Button(root,text="3",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click(3))
three.grid(row=1,column=2)
div=Button(root,text="/",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click("/"))
div.grid(row=4,column=1)
four=Button(root,text="4",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click(4))
four.grid(row=2,column=0)
five=Button(root,text="5",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click(5))
five.grid(row=2,column=1)
six=Button(root,text="6",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click(6))
six.grid(row=2,column=2)
mul=Button(root,text="*",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click("*"))
mul.grid(row=2,column=3)
seven=Button(root,text="7",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click(7))
seven.grid(row=3,column=0)
eight=Button(root,text="8",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click(8))
eight.grid(row=3,column=1)
nine=Button(root,text="9",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click(9))
nine.grid(row=3,column=2)
sub=Button(root,text="-",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click("-"))
sub.grid(row=3,column=3)
zero=Button(root,text="0",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click(0))
zero.grid(row=4,column=0)
space=Button(root,text="C",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=clear)
space.grid(row=1,column=3)
equals=Button(root,text="=",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=equal)
equals.grid(row=4,column=3)
add=Button(root,text="+",font=("bold",20),fg='red',bd=8,padx=16,background='grey',command=lambda:click("+"))
add.grid(row=4,column=2)


root.mainloop()
