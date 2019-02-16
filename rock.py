from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("600x600")
root.title("python graphics")
root.config(background='black')
root.resizable()
title=Label(root,text="Form",font=("Times New Roman",45),fg='red',background='black') #label eidget
title.grid(row=0,column=1)
title1=Label(root,text="Enter name",font=("",26),fg='green',background='black')
title1.grid(row=1,column=0)
name=Entry(root,width=20,font=("",26))
name.grid(row=1,column=1,padx=5,pady=(10,0),columnspan=5)
title2=Label(root,text="Enter your age",font=("",26),fg='green',background='black')
title2.grid(row=2,column=0)
#entry
age=Entry(root,width=20,font=("",26))
age.grid(row=2,column=1,padx=20,pady=(20,0),columnspan=5)
title3=Label(root,text="Enter Gender",font=("",26),fg='green',background='black')
title3.grid(row=3,column=0)

#radiobutton
gender=StringVar()
male=Radiobutton(root,text='Male',value='Male',variable=gender,font=("",20),fg='red',background='black')
male.grid(row=3,column=2)
Female=Radiobutton(root,text='FeMale',value='FeMale',variable=gender,font=("",20),fg='red',background='black')
Female.grid(row=3,column=1)
she=Radiobutton(root,text='others',value='others',font=("",20),variable=gender,fg='red',background='black')
she.grid(row=3,column=3)

#combo box
stream=ttk.Combobox(root,state='readonly',font=("",20),background='black',foreground='cyan')
stream.set("select your course")
stream['values']=["BBS","BIM","BCA","BSC.CSIT"]
stream.grid(row=4,column=2)
#function
def click():
    '''print("Nmae:",name.get())
    print("Age:",age.get())
    print("Gender:",gender.get())
    print("course:",stream.get())'''
    top=Toplevel(root)
    info=Label(top,text=name.get())
    info.grid(row=0,column=2)
    out=Label(top,text=age.get())
    out.grid(row=1,column=2)
    out1= Label(top, text=gender.get())
    out1.grid(row=2, column=2)
    out3= Label(top, text=stream.get())
    out3.grid(row=3, column=2)

#submit
submit=Button(root,text="SUBMIT",font=("",20),fg='red',background='black',command=click)
submit.grid(row=5,column=2,padx=20,pady=20)
root.mainloop()