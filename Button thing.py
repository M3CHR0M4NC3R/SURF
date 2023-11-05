import tkinter as tk 
#import file
#import SURF


#Window
window = tk.Tk()
window.geometry('900x600')
window.title("S.U.R.F")


def Button_click():
    title.config(text = "Button Clicked")
    #run the SURF command with the entry.get() as an argument, slap that bitch together like a string
    #yessur
    print(entry.get())

#Title and Format
title = tk.Label(window, text = "Welcome to The Simple Unintrusive Reorganized Files", font = 'Calibri 24 bold' )
title.pack()


#Inputs
input = tk.Frame(window)
entry = tk.Entry(input)
Button = tk.Button(input, text = "That Was Easy", command = Button_click)
entry.pack(side = 'left', padx = 10)
Button.pack(side = 'left')
input.pack(pady = 30)

#Output Label 
Output = tk.Label(window, text = "OutPut")

Output.pack()

window.mainloop()