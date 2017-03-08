# 08.3.2017
# Tkinter Introduction


import tkinter

# start up a little empty window
root = tkinter.Tk()

# make text appear in the window with a label
# bg = background color
# fg = foreground color
hi_there = tkinter.Label(
    root,
    text="Hi there!",
    bg="red",
    fg="white"
)
hi_there.pack(fill=tkinter.BOTH, expand=True)

my_name = tkinter.Label(
    root,
    text="My name is Tim"
)
my_name.pack()

# runs forever
root.mainloop()
