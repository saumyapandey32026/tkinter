from tkinter import *
root = Tk()
root.geometry("500x800")
root.title("Saumya's GUI🚀")

# Important Label options :-
# text - adds the Text
# bd or bg - background
# fg - foreground
# font - sets the font
# 1st. font=("any font style, 5, bold")  yhan tuple bnakar de diya
# 2nd. font="comicsansms 19 italic"  yhan string form mr hai
# padx - x padding
# pady - y padding
# relief - border styling (SUNKEN , RAISED , GROOVE ,RIDGE)

make_label = Label(
    text="ram is a very good boy. Haven't you heard about him before? He is the most intelligent boy of our school. his father is in Indian Army and his mother is mathematics professor in IIT Kanpur.",

      bg="darkblue", 
      fg="white", 

      padx=100 , 
      pady=200 , 

      font="comicsansms 19 italic" , 

      borderwidth=20, 
      relief=SUNKEN ,

      wraplength=300
)             # likh to tum sab kuchh ek hi line me , se seprate karke ,par aisa professional hai.
make_label.pack()


# Important pack options : 
# 1st. anchor = nw , ne , sw , se
# 2nd. side = top, right, bottom, left  {by default top}
# 3rd. fill = X or Y  i.e. jaise-2 ham ise x,y me khichte jayenge wo label khichta chala jayega , aur yad rakho jab aap fill = X likha tab side top/bottom & fill = Y then side left/right.



make_label.pack(anchor="sw" , side=TOP , fill=X , padx=50, pady=50)    # agar tum northwest i.e. nw likh0 to by default upar hi rahta hai isliye side set karne ki jarurat nhi hai 






























root.mainloop()

















