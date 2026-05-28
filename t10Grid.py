from tkinter import *
root = Tk()

root.geometry("500x300")

# Tkinter me widgets arrange karne ke 3 main ways hote hain:

# | Layout Manager | Kaam                      |
# | -------------- | ------------------------- |
# | pack()     | stacking / simple layouts |
# | grid()      | rows-columns layout 😎    |
# | place()      | exact x-y positioning     |

# user = Label(root , text="username")
# user.grid(row=2, column=4)


# password = Label(root , text="password")
# password.grid(row=1)  # by default col. 0 

# .grid() vs .pack()

# pack()
# Simple stacking 😄
# Widget
# Widget
# Widget

# grid()
# Structured layout 😎
# Label    Entry
# Label    Entry
# Button

# 😎😎 Entry and Variable :-  (.pack() kiya yhan par)

# name = StringVar()

# e = Entry(root, textvariable=name)  # Entry ka kam input lene ka hota hai, jhan aap type karte ho
# e.pack()

# def show():
#     print(name.get())

# Button(root, text="Show", command=show).pack()

#😎😎 Variable classes in tkinter :-  
# BooleanVar , DoubleVar , InterVar , StringVar 


# 😎😎 Entry and Variable :-  (.grid() kiya yhan par)


# 🚀🚀 STEP 4. function define kiya :-
def getvals():
    print(uservalue.get())
    print(passvalue.get())
# pehle function bana
# phir button ne uska reference use kiya  
# matlab ye wala part button ke upar hona chahiye , i.e. fn. pahle define hona chahiye, par bhai step to ye 4 hi hoga , since jaruri nhi ki ham hmesha command use hi kare, agar nhi kiya to fn. ki jarurat hi nhi padegi, mera man mai button bas dikhane ke liye lgau, tumse kya , mujhe nhi krana koi fn. apni button se 😄😄


# 🚀🚀 STEP 1. 2 Labels bnaye :- 
user = Label(root , text="username")
password = Label(root , text="password")
user.grid(row=1, column=1)
password.grid(row=2 , column=1)  


# 🚀🚀 STEP 2. Entry box bnaya aur use .grid se stack kiya na ki .pack se  :-
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root , textvariable=uservalue)
passentry = Entry(root , textvariable=passvalue)

userentry.grid(row=1,column=2)
passentry.grid(row=2,column=2)


# 🚀🚀 STEP 3. Button bnaya :-

# Button(text="submit" ).grid()  
# bas itna hi karna enough hai ek button bnane ke liye,aur bhi attributes ham apni jarurat ke hisab se lga lenge. yhan .grid() use kiya , aur koi row col. val. nhi dali ,apne aap decide kar lega.

Button(text="submit", command=getvals).grid()  




root.mainloop()























