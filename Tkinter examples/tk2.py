import tkinter as tk

#launching standart tkinter window tk.tutorial-0
#adjusting position of root windows tk.tutorial-1
#binding keys tk.tutorial-2

root = tk.Tk()
root.title("Root")
s_witdh = int(root.winfo_screenwidth()/2 - 150)
s_hight = int(root.winfo_screenheight()/2 - 100)
root.geometry(f"300x200+{s_witdh}+{s_hight}")

def ter(event=None):
    root.quit()

root.bind("<q>",ter)

root.mainloop()