import tkinter as tk 

#index: tutorial-0.1 creating a main windows
#index: tutorial-0.2 adding geometry specifier and title 
#index: tutorial-0.3 arranging the position

root = tk.Tk()
root.geometry("300x200+400+150") 
#width x height + position_for_width + position_for_height 
root.title("Title area") 

root.mainloop()

'''     --WARNİNG--
1- when you decide to assign a possition for root window
    you can't assign just one direction
    (e.g. not like this "300+200+400")
    you should assign for both direction
    (e.g. "300x200+400+150")

'''