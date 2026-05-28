from tkinter import *
root = Tk()
root.geometry("500x700")

f1 = Frame(root , borderwidth=10 , relief=SUNKEN , bg="grey" , height=100 , width=500)
f1.pack(fill="x")

def hello():
    print("hello saumya pandey")

b1 = Button(f1 , bg="pink" , text="hello" , fg="black" , borderwidth=10 , relief=SUNKEN , command=hello)   #🚀command="hello" nhi, only hello, aur hello() bhi nhi since kewal function name likhna hai yhan ,fn. call nhi karna hai
b1.pack( side="left" , padx=20 , pady=4)  

def name():
    print("name is saumya pandey")

b2 = Button(f1 , bg="blue" , text="name" , fg="aqua" , borderwidth=10 , relief=SUNKEN , command=name)
b2.pack( side="left" , padx=20 , pady=4)  

b3 = Button(f1 , bg="green" , text="click me" , fg="black" , borderwidth=10 , relief=SUNKEN)
b3.pack( side="left"  , padx=20 , pady=4)  

b4 = Button(f1 , bg="royalblue" , text="click me" , fg="black" , borderwidth=10 , relief=SUNKEN)
b4.pack(  side="left" , padx=20 , pady=4) 

b5 = Button(f1 , bg="red" , text="click me" , fg="black" , borderwidth=10 , relief=SUNKEN)
b5.pack(side="left" , padx=20 , pady=4)  
# 🚀🚀 bina kisi side and all ke center me jayega button









root.mainloop()