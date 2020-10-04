from tkinter import font, ttk, Button, StringVar, Entry, Tk, Canvas, Menu, PhotoImage, Wm
from tkinter.constants import GROOVE, RIDGE, LEFT
from math import sqrt


def makeNumBut(text, x, y):
    but = Button(canvas, bg="skyblue", fg="black",
                 text=text, command=lambda entry=display, q=text: entry.set(entry.get() + q), font=('Castellar', 20, 'bold'), relief=GROOVE, bd=5)
    but.place(relx=x, rely=y, relheight=.12, relwidth=.19)


def makeOperBut(text, x, y):
    oBut = Button(canvas, bg="seagreen", fg="black",
                  text=text, command=lambda entry=display, q=text: entry.set(entry.get() + q), font=('Bookman Old Style', 18, 'bold'), relief=GROOVE, bd=5)
    oBut.place(relx=x, rely=y, relheight=.12, relwidth=.19)


def makeInput():
    # print(font.families())
    global entry
    global display
    display = StringVar()
    entry = Entry(canvas, fg="purple", bg="#fdfd66",
                  font=("Rockwell", 16), textvariable=display, relief=RIDGE, bd=10)
    entry.place(relx=.5, rely=0.03, relheight=0.1, relwidth=.95, anchor='n')


def ans():
    try:
        display.set(eval(display.get()))
    except Exception as e:
        print(e)
        display.set(
            "Boy I dont know where these people come from and try to use modern tech.")

def sqrtGet():
    try:
        myInt = display.get()
        toConvert = int(myInt)
        converted = sqrt(toConvert)
        display.set(converted)
    except Exception as e:
        print(e)
        display.set(
            "Boy I dont know where these people come from and try to use modern tech.")

def clear():
    try:
        display.set('')
    except Exception as e:
        print(e)


def changeTheme():
    chosenTheme = themeChoice.get()
    # print(chosenTheme)
    colorTuple = colorDict.get(chosenTheme)
    # print(colorTuple)
    bg_color, none = colorTuple[0], colorTuple[1]
    canvas.config(bg=bg_color)


app = Tk()
app.title("My Calc")
app.resizable(0, 0)
app.wm_iconbitmap("./res/icon.ico")
# icon = PhotoImage(file="./res/icon.ico")

# app.call('wm', 'iconphoto', app._w, icon)

canvas = Canvas(app, width=350, height=500, bg="darkgrey")
canvas.pack()

makeInput()

num1 = makeNumBut("1", .03, .15)
num2 = makeNumBut("2", .27, .15)
num3 = makeNumBut("3", .51, .15)
num4 = makeNumBut("4", .03, .30)
num5 = makeNumBut("5", .27, .30)
num6 = makeNumBut("6", .51, .30)
num7 = makeNumBut("7", .03, .45)
num8 = makeNumBut("8", .27, .45)
num9 = makeNumBut("9", .51, .45)
num0 = makeNumBut("0", .27, .60)

# numBut = [num0, num1, num2, num3, num4, num5, num6,num7, num8, num9]

add = makeOperBut("+", .75, .15)
sub = makeOperBut("-", .75, .30)
mul = makeOperBut("/", .75, .45)
div = makeOperBut("*", .75, .60)
dot = makeOperBut(".", .75, .75)
per = makeOperBut("%", .51, .75)
sqr = makeOperBut("**", .27, .75)

# operBut = [add, sub, mul, div, dot, per]

# on = Radiobutton(canvas, text="ON", command="",
#  bg="darkgrey", font=('Bookman Old Style', 18, 'bold'))
# on.place(relx=.03, rely=.75, relwidth=.2, relheight=.09)

# off = Radiobutton(canvas, text="OFF", command="",
#   bg="darkgrey", font=('Bookman Old Style', 18, 'bold'))
# off.place(relx=.27, rely=.75, relwidth=.22, relheight=.09)

sqrtBut = Button(canvas, bg="seagreen", fg="black", text="√",
               font=('@MS Gothic', 18), command=sqrtGet, relief=GROOVE, bd=5)
sqrtBut.place(relx=.03, rely=.75, relheight=.12, relwidth=.19)

equalsBut = Button(canvas, bg="orange", fg="black", text="=", font=(
    '@MS Gothic', 18, 'bold'), command=ans, relief=GROOVE, bd=5)
equalsBut.place(relx=.51, rely=.60, relheight=.12, relwidth=.19)

clearBut = Button(canvas, bg="orange", fg="black", text="AC", font=(
    '@MS Gothic', 18, 'bold'), command=clear, relief=GROOVE, bd=5)
clearBut.place(relx=.03, rely=.60, relheight=.12, relwidth=.19)

menu = Menu()
theme = Menu(menu, tearoff=False)
menu.add_cascade(label="Background", menu=theme)

darkIcon = PhotoImage(file="./res/dark.png")
defIcon = PhotoImage(file="./res/default.png")
blueIcon = PhotoImage(file="./res/blue.png")
lightIcon = PhotoImage(file="./res/light.png")
monokaiIcon = PhotoImage(file="./res/monokai.png")
redIcon = PhotoImage(file="./res/red.png")

themeChoice = StringVar()
colorIcons = (defIcon, darkIcon, lightIcon, monokaiIcon, blueIcon, redIcon)

colorDict = {
    'Default': ('darkgrey', ''),
    'Dark': ('#4a4a47', ''),
    'Light': ('#d4d4cf', ''),
    'Monokai': ('#e6bf43', ''),
    'Night Blue': ('#2448ab', ''),
    'Red': ('#ed594c', '')
}

# theme.add_command(label="Default", compound=LEFT, command="", image=defIcon)
# theme.add_command(label="Dark", compound=LEFT, command="", image=darkIcon)
# theme.add_command(label="Light", compound=LEFT, command="", image=lightIcon)
# theme.add_command(label="Monokai", compound=LEFT, command="", image=monokaiIcon)
# theme.add_command(label="Blue", compound=LEFT, command="", image=blueIcon)
# theme.add_command(label="Red", compound=LEFT, command="", image=redIcon)

count = 0
for i in colorDict:
    theme.add_radiobutton(
        label=i, image=colorIcons[count], variable=themeChoice, compound=LEFT, command=changeTheme)
    count += 1

app.config(menu=menu)

# app.bind("<Enter>", ans)
app.mainloop()
