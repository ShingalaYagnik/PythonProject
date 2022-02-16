# __author__ = "Shingala Yagnik Maheshbhai"

import tkinter

app = tkinter.Tk()
app.title("Virtual Keyboard")

app.iconbitmap("D:\\PPs\\ProjectPython\\keyboard.ico")
app.geometry('1200x500-40-20')
# app.resizable(1080, 250)
app.resizable(0, 0)

appTitle = tkinter.Label(app, text="Virtual keyboard", font=("arial", 20, "bold"), bg="sky blue", fg="black", width=75,
                         relief=tkinter.RAISED)
appTitle.grid(row=0, columnspan=1250)

textBox = tkinter.Text(app, height=8, width=81, font=("arial", 20, "bold"), wrap=tkinter.WORD)
textBox.grid(row=1, columnspan=1250)

buttons = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', 'Back Space', '+',
           'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\\', '7', '8', '9',
           'Capslock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'Enter', '4', '5', '6',
           'Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift', '1', '2', '3',
           'Space'
           ]

#
# elif value == "Capslock":
# if value in "abcdefghijklmnopqrstuvwxyz":
#     value = value.lower()


# if value in "abcdefghijklmnopqrstuvwxyz":
#     value = value.upper()
# else:
#     if value in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         value = value.lower()




VarRow = 4
VarColumn = 0
CapsLockFlag = False
ShiftFlag = False


def select(value):
    global CapsLockFlag
    global ShiftFlag
    if value == "Capslock":
        CapsLockFlag = not CapsLockFlag
        ShiftFlag =False
    elif value == "Shift":
        ShiftFlag =True
    elif value == "Space":
        textBox.insert(tkinter.INSERT, ' ')
        ShiftFlag =False
    elif value=="Tab":
        textBox.insert(tkinter.INSERT, '    ')
        ShiftFlag =False
    elif value == "Enter":
        textBox.insert(tkinter.INSERT, '\n')
        ShiftFlag =False
    elif value == "Back Space":
        textBox.delete("end - 2c", tkinter.END)
        ShiftFlag =False
    else:
        if CapsLockFlag == True:
            value = value.upper()
        if ShiftFlag==True:
            if value in "abcdefghijklmnopqrstuvwxyz":
                value = value.upper()
            else:
                if value in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    value = value.lower()
            ShiftFlag =False

        textBox.insert(tkinter.INSERT, value)



for button in buttons:
    command = lambda x=button: select(x)
    if VarRow != 8:
        tkinter.Button(app, text=button, width=10, height=2, bg='black', fg='white', command=command).grid(row=VarRow,
                                                                                                           column=VarColumn)
    if VarRow == 8:
        tkinter.Button(app, text=button, width=40, height=2, bg='black', fg='white', command=command).grid(row=VarRow,
                                                                                                           columnspan=40,
                                                                                                           column=VarColumn)
    VarColumn += 1

    if VarColumn > 14:
        VarColumn = 0
        VarRow += 1

app.mainloop()
