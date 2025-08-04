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

def ter(event=None):
    root.quit()
root.bind("<q>",ter)

img1 = Image.open('/home/fedora1-41/prgm/storage/ic.png')
ico1 = ImageTk.PhotoImage(img1)
root.iconphoto(True,ico1)

label0 = tk.Label(text="label 0")
label0.pack()

label1 = tk.Label(root,text="str of label1",bg="red", fg="purple", font=("Helvetica", 20,"italic"))
label1.pack()

label2 = tk.Label(root,text="str of label2",bg="#101a3b", fg="#C9E042", font=("Helvetica", 20,"italic","bold","underline","overstrike"))
label2.pack()

my_custom_font = font.Font(family="Times New Roman", size=18, weight="bold", slant="italic", underline=True) #from tkintere import font

label3 = tk.Label(root, text="Custom Font Object", font=my_custom_font) 
label3.pack()

root.mainloop()