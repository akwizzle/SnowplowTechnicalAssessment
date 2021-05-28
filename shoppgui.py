from tkinter import *
from tkinter import scrolledtext
import spTracker as sp

HEIGHT = 700
WIDTH = 500
selected_item='NONE'
basket = []
total = 0
tracker = sp.spTracker()

def invoice():
    global basket
    global total
    report = ''
    for i in basket:
        report += '\n' + i[0] + '\t\t£' + str(i[1])
    report += '\n\nTOTAL:\t\t£'+ str(total) 
    return report

def basketview():
    shopframe.place_forget()
    baconbutton.place_forget()
    breadbutton.place_forget()
    cheesebutton.place_forget()
    chocolatebutton.place_forget()
    eggsbutton.place_forget()
    winebutton.place_forget()
    lollipopbutton.place_forget()
    popcornbutton.place_forget()
    tacobutton.place_forget()
    
    basketcontents.delete(1.0, END)
    basketcontents.insert(INSERT, invoice())
    basketframe.place(relx=0, rely=0.1, relwidth=1, relheight=0.7)
    basketcontents.place(relx=0, rely=0, relwidth=1, relheight=1)
    
def shopview():
    basketframe.place_forget()
    basketcontents.place_forget()

    shopframe.place(relx=0, rely=0.1, relwidth=1, relheight=0.7)
    baconbutton.place(relx=0, rely=0, relwidth=0.33, relheight=0.33)
    breadbutton.place(relx=0.33, rely=0, relwidth=0.33, relheight=0.33)
    cheesebutton.place(relx=0.66, rely=0, relwidth=0.33, relheight=0.33)
    chocolatebutton.place(relx=0, rely=0.33, relwidth=0.33, relheight=0.33)
    eggsbutton.place(relx=0.33, rely=0.33, relwidth=0.33, relheight=0.33)
    winebutton.place(relx=0.66, rely=0.33, relwidth=0.33, relheight=0.33)
    lollipopbutton.place(relx=0, rely=0.66, relwidth=0.33, relheight=0.33)
    popcornbutton.place(relx=0.33, rely=0.66, relwidth=0.33, relheight=0.33)
    tacobutton.place(relx=0.66, rely=0.66, relwidth=0.33, relheight=0.33)

def select(iteminfo):
    global selected_item
    selected_item = iteminfo
    selected.delete(1.0, END)
    selected.insert(INSERT, iteminfo[0]+'\t\t£'+str(iteminfo[1]))

def add():
    global basket
    global selected_item
    global total
    global tracker
    
    basket += [selected_item]
    tracker.add_to_cart(selected_item[2],selected_item[0],selected_item[1])
    total += selected_item[1]

    basketcontents.delete(1.0, END)
    basketcontents.insert(INSERT, invoice())

def buy():
    global basket
    global total
    global tracker

    tracker.bought_items(basket,total)
    tracker.all_items_bought(basket)
    
    basket = []
    total = 0

    basketcontents.delete(1.0, END)
    basketcontents.insert(INSERT, invoice())

def clear():
    global basket
    global total
    global tracker

    tracker.clear_cart(basket)
    basket = []
    total = 0

    basketcontents.delete(1.0, END)
    basketcontents.insert(INSERT, invoice())
    
root = Tk()
root.title("Shopp")

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

baconicon = PhotoImage(file = r"Icon_bacon.png").subsample(2,2)
breadicon = PhotoImage(file = r"Icon_bread.png").subsample(2,2)
cheeseicon = PhotoImage(file = r"Icon_cheese.png").subsample(2,2)
chocolateicon = PhotoImage(file = r"Icon_chocolate.png").subsample(2,2)
eggsicon = PhotoImage(file = r"Icon_eggs.png").subsample(2,2)
wineicon = PhotoImage(file = r"Icon_glass of wine.png").subsample(2,2)
lollipopicon = PhotoImage(file = r"Icon_lollipop.png").subsample(2,2)
popcornicon = PhotoImage(file = r"Icon_popcorn.png").subsample(2,2)
tacoicon = PhotoImage(file = r"Icon_taco.png").subsample(2,2)

#Creating and placing the header
headerframe = Frame(root, bg='black', bd=5)
shopbutton = Button(headerframe, text='Shop', font=40, command=lambda:shopview())
basketbutton = Button(headerframe, text='Basket', font=40, command=lambda:basketview())
headerframe.place(relx=0, rely=0, relwidth=1, relheight=0.1)
shopbutton.place(relx=0, rely=0, relwidth=0.25, relheight=1)
basketbutton.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

#Creating and placing the shopp
shopframe = Frame(root, bg='grey', bd=5)
baconbutton = Button(shopframe, image=baconicon, command=lambda: select(('Bacon',2.5,'001')))
breadbutton = Button(shopframe, image=breadicon, command=lambda: select(('Bread',1,'002')))
cheesebutton = Button(shopframe, image=cheeseicon, command=lambda: select(('Cheese',3,'003')))
chocolatebutton = Button(shopframe, image=chocolateicon, command=lambda: select(('Chocolate',4,'004')))
eggsbutton = Button(shopframe, image=eggsicon, command=lambda: select(('Eggs',2,'005')))
winebutton = Button(shopframe, image=wineicon, command=lambda: select(('Wine',7,'006')))
lollipopbutton = Button(shopframe, image=lollipopicon, command=lambda: select(('Lollipop',0.5,'007')))
popcornbutton = Button(shopframe, image=popcornicon, command=lambda: select(('Popcorn',5,'008')))
tacobutton = Button(shopframe, image=tacoicon, command=lambda: select(('Taco',3.5,'009')))

shopframe.place(relx=0, rely=0.1, relwidth=1, relheight=0.7)
baconbutton.place(relx=0, rely=0, relwidth=0.33, relheight=0.33)
breadbutton.place(relx=0.33, rely=0, relwidth=0.33, relheight=0.33)
cheesebutton.place(relx=0.66, rely=0, relwidth=0.33, relheight=0.33)
chocolatebutton.place(relx=0, rely=0.33, relwidth=0.33, relheight=0.33)
eggsbutton.place(relx=0.33, rely=0.33, relwidth=0.33, relheight=0.33)
winebutton.place(relx=0.66, rely=0.33, relwidth=0.33, relheight=0.33)
lollipopbutton.place(relx=0, rely=0.66, relwidth=0.33, relheight=0.33)
popcornbutton.place(relx=0.33, rely=0.66, relwidth=0.33, relheight=0.33)
tacobutton.place(relx=0.66, rely=0.66, relwidth=0.33, relheight=0.33)

#Creating and placing the list of Basket Items
basketframe = Frame(root, bg='grey')
basketcontents = scrolledtext.ScrolledText(basketframe, bg='white', font=30, wrap=WORD)

#Creating and placing the currently selected frame
selected = Text(root, bg='white', font=40, wrap=WORD)
selected.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)

#Creating and placing the footer frame
footerframe = Frame(root, bg='black', bd=5)
addbutton = Button(footerframe, text='Add to Basket', font=30, command=lambda:add())
buybutton = Button(footerframe, text='Buy', font=40, command=lambda:buy())
clearbutton = Button(footerframe, text='Clear Basket', font=3, command=lambda:clear())
footerframe.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
addbutton.place(relx=0.05, rely=0, relwidth=0.3, relheight=1)
buybutton.place(relx=0.35, rely=0, relwidth=0.3, relheight=1)
clearbutton.place(relx=0.65, rely=0, relwidth=0.3, relheight=1)
