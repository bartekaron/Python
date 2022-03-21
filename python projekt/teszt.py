from tkinter import *
import math
import cmath
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b 
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: "+str(c))
def kivonas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a - b 
    mezo3.delete(0, END)
    mezo3.insert(0, "Kivonás: "+str(c))

def szorzas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a * b 
    mezo3.delete(0, END)
    mezo3.insert(0, "Szorzás: "+str(c))

def osztas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a / b if b != 0 else "Nem lehet nullával osztani"
    mezo3.delete(0, END)
    mezo3.insert(0, "Osztás: "+str(c))

def negyzetreemeles():
    a = int(mezo1.get())
    c = a * a 
    mezo3.delete(0, END)
    mezo3.insert(0, "Négyzetre emelés: "+str(c))

def gyokvonas():
    a = int(mezo1.get())
    c = math.sqrt(a) if a > 0 else "Nem lehet minusszal gyököt vonni"
    mezo3.delete(0, END)
    mezo3.insert(0, "Gyökvonás: "+str(c))

foablak=Tk()
cimke=Label(foablak, text="Üdvözlet!", fg="red",)
cimke.grid()
cimke=Label(foablak, text="Nem lehet nullával osztani.(Minden nullával osztott szám 0)", fg="red")
cimke.grid()
gomb1=Button(foablak, text="Oké")
gomb1.grid()
megse=Button(foablak, text="Mégse")
megse.grid()
mezo1=Entry(foablak, width=10)
mezo1.grid(row=1, column=2)
mezo2=Entry(foablak, width=10)
mezo2.grid(row=2, column=2)
gomb4=Button(foablak, text="Összead", command=osszeg)
gomb4.grid()
gomb5=Button(foablak, text="Kivonás", command=kivonas)
gomb5.grid()
gomb6=Button(foablak, text="Szorzás", command=szorzas)
gomb6.grid()
gomb7=Button(foablak, text="Osztás", command=osztas)
gomb7.grid()
gomb8=Button(foablak, text="Négyzetre emelés", command=negyzetreemeles)
gomb8.grid()
gomb9=Button(foablak, text="Gyökvonás", command=gyokvonas)
gomb9.grid()
mezo3=Entry(foablak, width=55,)
mezo3.grid(row=1)
gomb3=Button(foablak, text="Kilépés", command=foablak.destroy)
gomb3.grid(row=15, column=2)

can1 = Canvas(foablak, width =450, height =450, bg ="white")
photo = PhotoImage(file = 'R.gif')
item = can1.create_image(80, 80, image =photo)
can1.grid()

foablak.mainloop()