import tkinter as tk 

#index: tutorial-0.1 creating a main window
#index: tutorial-0.2 adding geometry specifier and title 
#index: tutorial-0.3 arranging the position
#index: tutorial-0.4 using variable for size and position of root
#index: tutorial-0.5 configuration of window's backgroud

root = tk.Tk()
root.title("Tkinter - Root")
root.configure(bg="lightblue") #you can use both names or colour codes
root.configure(bg="#89F1E0") #:D I tried to make this lightblue, too 
#--WARNING--: those codeS should be exactly 6 number of digit
#(i.e. #RRGGBB) 
# don't use something like #00112233 or #00112


ww = 300;wh = 200

sh = root.winfo_screenheight()
sw = root.winfo_screenwidth()

pw_w = sw/2 - ww/2
pw_h = sh/2 - wh/2

root.geometry(f"{ww}x{wh}+{int(pw_w)}+{int(pw_h)}")






root.mainloop()

