import tkinter as tk


root = tk.Tk()

root.title('Project Steam Dashboard')
root.minsize(700, 700)

root.configure()
root.geometry(str(root.winfo_screenwidth() - 100) + 'x' + str(root.winfo_screenheight() - 100))
root.mainloop()
