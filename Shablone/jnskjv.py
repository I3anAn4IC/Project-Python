# from tkinter import *
# from tkinter import messagebox
# Tk().wm_withdraw() #to hide the main window
# messagebox.showinfo('Continue', 'OK')


from tkinter import *


window = Tk()
window.geometry('500x300+460+240')
lbl = Label(window, text="Привет")
lbl.grid(column=0, row=0)


window.mainloop()
