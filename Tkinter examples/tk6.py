import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk

#launching standart tkinter window tk.tutorial-0
#adjusting position of root windows tk.tutorial-1
#binding keys tk.tutorial-2
#setting up app photos tutorial-3
#adding label widget and costumizing it tutorial-4
#defining a function for button and adding button tutorial-5

root = tk.Tk()
root.title("Root")
s_witdh = int(root.winfo_screenwidth()/2 - 250)
s_hight = int(root.winfo_screenheight()/2 - 150)
root.geometry(f"500x300+{s_witdh}+{s_hight}")

img1 = Image.open('/home/fedora1-41/prgm/storage/ic.png')
ico1 = ImageTk.PhotoImage(img1)
root.iconphoto(True,ico1)

label0 = tk.Label(text="label 0")
label0.pack()

button1 = tk.Button(root, text="Button 1", command=print("hi"))
button1.pack()


root.mainloop()