from tkinter import ttk, Tk

def button_clicked():
    print(my_name.get())

root = Tk()

my_name = ttk.Entry(root)
my_name.pack()

ttk.Button(root, text="SOLA", command=button_clicked).pack()

root.mainloop()