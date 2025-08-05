import tkinter as tk
from PIL import Image,ImageTk


#launching standart tkinter window tk.tutorial-0
#adjusting position of root windows tk.tutorial-1
#binding keys tk.totorial-2
#setting up app photos totorial-3.2

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


root.mainloop()
