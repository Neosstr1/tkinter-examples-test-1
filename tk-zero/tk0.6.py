import tkinter as tk 

#index: tutorial-0.1 creating a main window
#index: tutorial-0.2 adding geometry specifier and title 
#index: tutorial-0.3 arranging the position
#index: tutorial-0.4 using variable for size and position of root
#index: tutorial-0.5 configuration of window's backgroud
#index: tutorial-0.6 adding iconphoto --WARNING-- tested just on linux, not yet for WINs and MACs

root = tk.Tk()
root.title("Tkinter - Root")
root.configure(bg="lightblue") 
root.configure(bg="#89F1E0") 

img1 = tk.PhotoImage(file='the/path/where/you/downloaded/this/tkinter-example-test-1/image1.png')
#We are creting an object for using photo

root.iconphoto(True,img1)
#setting up the image for the object root

ww = 300;wh = 200

sh = root.winfo_screenheight()
sw = root.winfo_screenwidth()

pw_w = sw/2 - ww/2
pw_h = sh/2 - wh/2

root.geometry(f"{ww}x{wh}+{int(pw_w)}+{int(pw_h)}")

root.mainloop()

'''
--- CONGRATULATIONS ---  d(>_• )

If you've reached this point, congratulations, praise youself because you deserve this

You've been learned:

*Creating a top level window, 
*Adjusting size, position, backgraound and title of that window

*And also assigning iconphoto along this lesson


Right now, for the next lesson or tutorial file,
you will learn binding keys in a couple of file
and you will change the iconphotos via those keys

Go tk.t folder from main folder, and don't skip to INTRO.md file.
'''



