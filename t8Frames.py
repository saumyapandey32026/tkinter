from tkinter import * 
root = Tk()

root.geometry("500x300")
root.minsize(300,100)
root.maxsize(600,400)
root.title("saumya's gui")

# Frames :- 
f1 = Frame(root, bg="royalblue" , borderwidth=7 , relief=SUNKEN , width=150)
f1.pack(side=LEFT , fill ="y")
f2 = Frame(root, bg="blue" , borderwidth=7 , relief=SUNKEN , width=150)
f2.pack(side="top" , fill ="x" , pady=20)


l = Label(f1 , text="frame1" , fg="black" , bg="white" , font=("Helvetica" , 5 , "bold"))
l.pack(pady=20)    # 🚀🚀 Frames shrink/grow according to children widgets ,qb yhan par itna hi text hai to frame shrink ho jayega usi ke brabar, bhale hi uski width 150 set ki hai aapne.    pack_propagate(False) - aur ye rha solution        
l = Label(f2 , text="welcome to subline text" , fg="black" , bg="white")
l.pack()    











root.mainloop()