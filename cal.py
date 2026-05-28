from tkinter import *    

saumya_root = Tk()              # ctrl+click on Tk() you can see....

# 🔍 gui logic here : 
# 🔍 GUI app ka flow usually aisa hota hai : 
# root = Tk()

# # settings
# root.geometry()
# root.title()

# # widgets
# Label()
# Button()

# # show/run app
# root.mainloop()

#  "width x height"  (small x hai ye)
saumya_root.geometry("800x1000")

#   width , height
saumya_root.minsize(100 , 200)

#   width , height
saumya_root.maxsize(2000 , 3500)

# ab labels jinse user interact nhi karta , label(text), images ,.....
ab_label = Label(text= "Saumya's 1st gui app" , bg="black" , fg="yellow")
ab_label.pack()

# ab_image = PhotoImage(file="my photo.jpeg")           #jpeg tkinter support nhi karta isliye - pip install pollow, ek module install python ka, and write : from PIL import Image, ImageTk ,  PIL matlab : python imaging library

# ab_image = Image.open("my photo.jpeg")
# sec_img = ImageTk.PhotoImage(ab_image)
# now_label_it = Label(image=sec_image)
# now_label_it.pack()

ab_image = PhotoImage(file="image.png")          
now_label_it = Label(image=ab_image)
now_label_it.pack()

















saumya_root.mainloop()







