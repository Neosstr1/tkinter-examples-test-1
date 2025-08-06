import tkinter as tk 

#index: tutorial-0.1 creating a main window
#index: tutorial-0.2 adding geometry specifier and title 
#index: tutorial-0.3 arranging the position
#index: tutorial-0.4 using variable for size and position of root

root = tk.Tk()
root.title("Tkinter - Root")

ww = 300
wh = 200

sh = root.winfo_screenheight()
sw = root.winfo_screenwidth()

pw_w = sw/2 - ww/2 #pw_w is position of window; width
pw_h = sh/2 - wh/2 #pw_h is position of window; height

root.geometry(f"{ww}x{wh}+{int(pw_w)}+{int(pw_h)}") 
#used in formmated function 
#The variables have been changed from float to integer values 
# (i.e. +{int(pw_w)}+{int(pw_h)}).

root.mainloop()

'''     --WARNING--

1- pw_w and pw_h should be covered as integer value. 
    The division process(i.e. /2) turns pw_h and pw_w to float values.
    The geometry functions dont accept decimal(e.g. 4.67  60.0)

2- You might be writing winfo_screenheight() and winfo_screenwidth() incorrectly, 
    instead of winfo_screenmmheight() and winfo_screenmmwidth().
'''