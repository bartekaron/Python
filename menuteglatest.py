from tkinter import *
from tkinter import messagebox
import math

def nevjegy():
    abl2 = Toplevel(foablak)
    uz2 = Message(abl2, text="Készítette: Bartek Áron\nBaja\n2022.04.12", width=300)
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()
    #Névjegy ablak vége 


    #Felszín ablak vége
def felszin():
    def szamit():

        cucc=mezo1.get()
        if len(cucc) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        cucc=int(cucc)

        cucc=mezo2.get()
        if  len(cucc) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        cucc=int(cucc)


        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        felszín = 2*(a*b+a*c+b*c)
        mezo4.delete(0,END)
        mezo4.insert(0,str(felszin))

    abl3=Toplevel(foablak)
    abl3.title("A téglatest felszíne")
    abl3.minsize(width=300, height=100)
    szoveg1 = Label(abl3, text="a")
    szoveg2 = Label(abl3, text="b")
    szoveg3 = Label(abl3, text="c")
    szoveg4 = Label(abl3, text="Eredmeny")
    gomb1 = Button(abl3, text ="Számítás", command=szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2)
    mezo1.grid(row=1, column=2)
    mezo2.grid(row=2, column=2)
    mezo3.grid(row=3, column=2)
    mezo4.grid(row=5, column=2)
    abl3.mainloop()
    #Felszín vége
def terfogat():

    def szamit():
        cucc=mezo1.get()
        if len(cucc) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        cucc=int(cucc)

        cucc=mezo2.get()
        if  len(cucc) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        cucc=int(cucc)

        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a*b*c
        mezo4.delete(0,END)
        mezo4.insert(0,str(terfogat))
    abl3=Toplevel(foablak)
    abl3.title("A téglatest térfogata")
    abl3.minsize(width=300, height=100)
    szoveg1 = Label(abl3, text="a")
    szoveg2 = Label(abl3, text="b")
    szoveg3 = Label(abl3, text="c")
    szoveg4 = Label(abl3, text="Eredmeny")
    gomb1 = Button(abl3, text ="Számítás", command=szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2)
    mezo1.grid(row=1, column=2)
    mezo2.grid(row=2, column=2)
    mezo3.grid(row=3, column=2)
    mezo4.grid(row=5, column=2)
    abl3.mainloop()

#Térfogat vége

def henger_felszín():
    def szamit1():
        cucc=mezo1.get()
        if len(cucc) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        cucc=int(cucc)

        cucc=mezo2.get()
        if  len(cucc) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        cucc=int(cucc)

        a = eval(mezo1.get())
        b = eval(mezo2.get())
        felszín = (2*math.pi*a*b+2*math.pi*a**2)
        mezo4.delete(0,END)
        mezo4.insert(0,str(felszín))
    abl3=Toplevel(foablak)
    abl3.title("A henger térfogata")
    abl3.minsize(width=300, height=100)
    szoveg1 = Label(abl3, text="Sugár(cm)")
    szoveg2 = Label(abl3, text="Magasság(cm")
    szoveg4 = Label(abl3, text="Eredmeny")
    gomb1 = Button(abl3, text ="Számítás", command=szamit1)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2)
    mezo1.grid(row=1, column=2)
    mezo2.grid(row=2, column=2)
    mezo4.grid(row=5, column=2)
    abl3.mainloop()

   
def henger_térfogat():
    def szamit():
        cucc=mezo1.get()
        if len(cucc) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        cucc=int(cucc)


        cucc=mezo2.get()
        if  len(cucc) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        cucc=int(cucc)
        
        
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        henger = (a**2*b*math.pi)
        mezo4.delete(0,END)
        mezo4.insert(0,str(henger))
    abl3=Toplevel(foablak)
    abl3.title("A henger felszíne")
    abl3.minsize(width=300, height=100)
    szoveg1 = Label(abl3, text="Sugár(cm)")
    szoveg2 = Label(abl3, text="Magasság(cm")
    szoveg4 = Label(abl3, text="Eredmeny")
    gomb1 = Button(abl3, text ="Számítás", command=szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2)
    mezo1.grid(row=1, column=2)
    mezo2.grid(row=2, column=2)
    mezo4.grid(row=5, column=2)
    abl3.mainloop()
   


#Főablak
foablak = Tk()
foablak.title("A téglatest adatai")
foablak.minsize(width = 300, height=100)

menusor = Frame(foablak)
menusor.pack(side=TOP, fill=X)
menu1 = Menubutton(menusor, text="Fájl", underline=0)
menu1.pack(side=LEFT)
fajl=Menu(menu1)
fajl.add_command(label="Névjegy", command = nevjegy, underline=0)
fajl.add_command(label="Kilépés", command=foablak.destroy, underline=0)
menu1.config(menu = fajl)

menu2 = Menubutton(menusor, text="Téglatest", underline=0)
menu2.pack(side = LEFT)
teglatest=Menu(menu2)
teglatest.add_command(label="Felszín", command = felszin, underline=0)
teglatest.add_command(label="Térfogat", command = terfogat, underline=0)

menu2.config(menu = teglatest)

menu2 = Menubutton(menusor, text="Henger", underline=0)
menu2.pack(side = LEFT)
henger=Menu(menu2)
henger.add_command(label="Henger felszíne", command = henger_felszín, underline=0)
henger.add_command(label="Henger térfogata", command = henger_térfogat, underline=0)
menu2.config(menu = henger)

foablak.mainloop()