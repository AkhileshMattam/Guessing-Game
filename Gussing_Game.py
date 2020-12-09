''' A GUI based Guessing Game were you can guess names of the folloing:
    1--> Animals
    2--> Birds
    3--> Flowers
    4--> Fishes
'''
# Libraries
from tkinter import *
import random
import datetime


# global variables
global jword, score, f2, c
score = c = 0


# List function
def listfun(event):
    global jword
    e1.delete(0, 20)
    lst1 = ['ELEPHANT', 'MONKEY', 'ZEBRA', 'TIGER', 'LION', 'YAK', 'CAMEL', 'DEER', 'HIPPOPOTAMUS', 'KANGAROO',
            'GORILLA', 'DONKEY', 'sheep', 'panda', 'horse', 'Buffalo', 'wolf', 'cow', 'pig', 'cat', 'goat', 'dog',
            'rabbit', 'rat', 'scorpion']
    lst2 = ['Sparrow', 'Eagle', 'crow', 'flamingo', 'parrot', 'peacock', 'hawk', 'kingfisher', 'swan', 'pigeon', 'duck',
            'ostrich', 'owl', 'penguin', 'woodpecker', 'robin', 'cock', 'hen']
    lst3 = ['sunflower', 'marigold', 'tulip', 'rose', 'hibiscus', 'lotus', 'jasmine', 'daisy', 'lavender', 'orchid',
            'bougainvillea', 'lily', 'daffodils', 'poppy']
    lst4 = ['piranha', 'whale', 'shark', 'tuna', 'salmon', 'stingray', 'tuna', 'dolphin', 'goldfish', 'starfish',
            'jellyfish', 'pufferfish', 'catfish', 'swordfish', 'eel', 'orcas']
    if st.get() == 'Animals':
        jword = random.choice(lst1)
        jumbfun(jword)
    if st.get() == 'Birds':
        jword = random.choice(lst2)
        jumbfun(jword)
    if st.get() == 'Flowers':
        jword = random.choice(lst3)
        jumbfun(jword)
    if st.get() == 'Fishes':
        jword = random.choice(lst4)
        jumbfun(jword)


# Jumble function
def jumbfun(val):
    out = ("".join(random.sample(val, len(val)))).lower()
    print(out)
    l1.config(text=out)


# Check function
def check():
    global jword
    global score
    eword = e1.get()
    eword = eword.upper()
    correct = '\U0001F603'+'\U0001F603'+'\nYou gussed correct'
    noentry = '\U0001F611'+'\U0001F611'+'\nYou didn\'t enter anything'
    wrong = '\U0001F61E'+'\U0001F61E'+'\nWrong guess..try again'
    if eword == jword.upper():
        l3.configure(text=correct, fg='black', bg='#B8FB3C')
        listfun(st.get())
        score += 1
        if score == 10:
            f1.destroy()
            resultframe()
        l5.config(text=score)
    elif eword == "":
        l3.configure(text=noentry, fg='#0310EA', bg='#FF2079')
    else:
        l3.configure(text=wrong, fg='black', bg='red')
        score -= 1
        l5.config(text=score)
    e1.delete(0, END)


# validate function
def valid(inp):
    if inp.isalpha():
        return True
    elif inp == '':
        return True
    else:
        return False


# OK function
def okfunc(event):
    check()


# next function
def nextfunc(event):
    listfun(st.get())


# HINT function
def hintfun():
    global jword, c
    c = c+1
    print(c)
    if c <= 5:
        l3.config(text=jword, bg='#28CF75')
    else:
        l3.config(text='No more hints', bg='#EBF875')


# frame 2
def resultframe():
    f2 = LabelFrame(am, bg='#80FF72')
    f2.pack(fill='both', expand=True)
    omin = datetime.datetime.now().minute
    osec = datetime.datetime.now().second
    print(omin, osec)
    fmin = abs(omin - imin)
    fsec = abs(osec - isec)
    mintxt = str(fmin)+' Minutes'
    sectxt = str(fsec)+' Seconds'
    congrats = '\U0001F38A'+'\U0001F38A'+'\U0001F38A'+'Congratulation'+'\U0001F38A'+'\U0001F38A'+'\U0001F38A'
    end = '\U0001F44D'+'\U0001F44F'+'\U0001F44F'+'\U0001F44F'+'\U0001F44F'+'\U0001F44F'+'\U0001F44D'
    Label(f2, text=congrats, font='Verdana 20', bg='#80FF72', fg='#EA55B1').pack(pady=20)
    Label(f2, text='Well Done!! \nYou Answered 10 Correct Names', font='Verdana 11 bold', bg='#80FF72', fg='#EF0888').pack(pady=8)
    Label(f2, text='You Took', font='Verdana 10 bold', bg='#48ADF1').pack(pady=20)
    lm = Label(f2, text=mintxt, font='Verdana 10 bold', bg='#48ADF1')
    lm.place(x=114, y=180)
    Label(f2, text=":", font='Verdana 10 bold', bg='#48ADF1').place(x=190, y=180)
    ls = Label(f2, text=sectxt, font='Verdana 10 bold', bg='#48ADF1')
    ls.place(x=200, y=180)
    Label(f2, text=end, font='Verdana 20 bold', bg='#80FF72', fg='orange').pack(pady=25)
    Label(f2, text='Rerun the program to play again', font='Verdana 10 bold', bg='#80FF72').pack(side=BOTTOM)


# GUI window
am = Tk()
am.geometry("400x330")
am.title("Gussing Game")
am.resizable(width=False, height=False)

# in time
imin = datetime.datetime.now().minute
isec = datetime.datetime.now().second
print(imin,isec)

# frame
f1 = LabelFrame(am, padx=10, pady=10, background='#FFCCCC')
f1.pack(fill='both', expand=True)

# optionmenu
mlst = ['Animals', 'Birds', 'Flowers', 'Fishes']
st = StringVar(am)
st.set('MENU')
op = OptionMenu(f1, st, *mlst, command=listfun)
op.config(bg='#B537F2', activebackground='#8A2BE2')
op.place(x=-10, y=-10)

# labels
l1 = Label(f1, text="WELCOME", font='Times 16 bold', bg='#00C2BA')
l1.pack(pady=15)
l2 = Label(f1, text="Guess the Name", font='Times 16 bold', bg='#FF822E')
l2.pack(pady=5)

# entry
e1 = Entry(f1, font='Verdana 20', width=30, bd=5)
e1.pack(pady=4)

# validate
v1 = am.register(valid)
e1.config(validate="key", validatecommand=(v1, '%P'))

# Buttons
b1 = Button(f1, text="OK", font='Verdana 10', bg='#B537F2', activebackground='#8A2BE2', command=check)
b1.place(x=0, y=160)
b2 = Button(f1, text="NEXT", font='Verdana 10', bg='#B537F2', activebackground='#8A2BE2', command=lambda: listfun(st.get()))
b2.place(x=330, y=160)
b3 = Button(f1, text="HINT", font='Verdana 10', bg='#B537F2', activebackground='#8A2BE2', command=hintfun)
b3.place(x=340, y=-8)

# Result label
l3 = Label(f1, text="-----result:-----", font='Verdana 16', bg='#FF1493')
l3.pack(side=BOTTOM)

# Score label
l4 = Label(f1, text='SCORE:', font='Verdana 10 bold', bg='#FEF900')
l4.place(x=146, y=180)
l5 = Label(f1, font="Verdana 10 bold", bg='#FEF900')
l5.place(x=200, y=180)

# keyboard
am.bind('<Return>', okfunc)
am.bind('<space>', nextfunc)

am.mainloop()