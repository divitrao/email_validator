from validate_email import  validate_email
from  tkinter import *

root = Tk()

root.title('Email Validator')

def checkit(*args):
    email_add=str(ent.get())

    is_valid = str(validate_email(email_add))

    # print(is_valid)
    # print(type(is_valid))
    if is_valid == 'True':
        text.set('Valid Email id')

    else:
        text.set(' not a Valid Email id')






# frame = Frame(root,width=400,height=400)
lable1 = Label(root,text='Enter an Email id in the below box')

lable1.grid(row=0,columns=2)
ent = Entry(root,width=50,borderwidth=5)
ent.grid(row=1,column=0,columnspan=3)

button1= Button(text='Click here to validate',command=checkit)
button1.grid(row=4,column=2,columnspan=3)

text = StringVar()
lable2 = Label(root, textvariable=text)
lable2.grid(row=4, column=1)

for child in root.winfo_children(): child.grid_configure(padx=10, pady=5)
root.bind('<Return>',checkit)
root.mainloop()