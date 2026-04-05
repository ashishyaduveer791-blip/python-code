from tkinter import*
root = Tk()
# # ceate  a label widget
# mylabe1 = Label(root, text = "hello world!")
# mylabe2 = Label(root, text = "ashish!")
# # showing t onto the secreen
# mylabe1.grid(roe = 0,column=0)
# mylabe2.grid(row = 1,column= 5)
# root .mainloop()

# Button creation


# myButton  = Button(root,text="Click Me !",state=DISABLED)
# CHANGE TTHE  SIZE
e =Entry(root,width =50,bg="pink")
e.pack()
e.get()
def myClick():
    
    mylabel =  Label(root,text="heloo " +e.get())
    mylabel.pack()
myButton = Button(root,text="Enter you Name", command=myClick,fg="white",bg="black")
myButton.pack()


# myButton.pack()
root.mainloop()


# Build a sample calcukter

