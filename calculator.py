from tkinter import *


#this is what you have to do first
root = Tk()
#Change the title
root.title("Simple Calculator")

#NOTE: get() returns the entry's current text as a string


#input box
e = Entry(root, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
	#takes what is currently in the box
	current = e.get()
	#delete whats in the box
	e.delete(0, END)
	#combines what was in the box with new number and puts back into input box
	e.insert(0, str(current) + str(number))


def button_clear():
	e.delete(0, END)


def button_add():
	#takes whatever is in the input box
	first_number = e.get()
	#put it in a global variable that can then be used in other functions / turns it into a legit integer
	global f_num
	f_num = int(first_number)
	#delete whats currently in the input box
	e.delete(0, END)

def button_equal():
	#takes whatever is in the input box
	second_number = e.get()
	#deletes whatever is in the input box
	e.delete(0, END)
	#adds the first number that is inside the global variable and adds it to the second number
	e.insert(0, f_num + int(second_number))

#define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)


#put the buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)




#GUI is always looping
root.mainloop()



# #creating label widget
# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="My name is Tom")
# #shoving it onto the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)




# root.geometry("200x150")
# frame = Frame(root)
# frame.pack()
 
# leftframe = Frame(root)
# leftframe.pack(side=LEFT)
 
# rightframe = Frame(root)
# rightframe.pack(side=RIGHT)
 
# label = Label(frame, text = "Hello world")
# label.pack()
 
# button1 = Button(leftframe, text = "Button1")
# button1.pack(padx = 3, pady = 3)
# button2 = Button(rightframe, text = "Button2")
# button2.pack(padx = 3, pady = 3)
# button3 = Button(leftframe, text = "Button3")
# button3.pack(padx = 3, pady = 3)
 
# root.title("Test")
# root.mainloop()