from tkinter import *
import math
p=7.8
g=0.7

def térfogat():
    a = float(mezo.get())
    b = float(mezo1.get())
    c = round(a**2*b*math.pi, 2)
    mezo2.delete(0, END)
    mezo2.insert(0,""+str(c)+" cm3")

def vastömeg():
    a = float(mezo.get())
    b = float(mezo1.get())
    c = a**2*b*math.pi
    d = round(c * p, 2)
    mezo3.delete(0, END)
    mezo3.insert(0,"" +str(d)+" g")

def fahenger():
    a = float(mezo.get())
    b = float(mezo1.get())
    c = a**2*b*math.pi
    q = round(c * g, 2)
    mezo4.delete(0, END)
    mezo4.insert(0,"" +str(q)+" g")

   
    
foablak=Tk()
foablak.title("tk")
cimke=Label(foablak, text="Sugár (cm):", fg="black", compound="top")
cimke.grid()
mezo=Entry(foablak, width=23,)
mezo.grid(row=0, column=2)
cimke1=Label(foablak, text="Magasság (cm):", fg="black", compound="top")
cimke1.grid()
mezo1=Entry(foablak, width=23,)
mezo1.grid(row=1, column=2)
gomb=Button(foablak, text="Kiszámít", command=lambda:[térfogat(), vastömeg(), fahenger()], )
gomb.grid(row=2, column=3)


cimke3=Label(foablak, text="Térfogat:", fg="black")
cimke3.grid()
mezo2=Entry(foablak, width=23,)
mezo2.grid(row=3, column=2)
cimke4=Label(foablak, text="Vashenger:", fg="black")
cimke4.grid()
mezo3=Entry(foablak, width=23,)
mezo3.grid(row=4, column=2)
cimke5=Label(foablak, text="Fahenger:", fg="black")
cimke5.grid()
mezo4=Entry(foablak, width=23,)
mezo4.grid(row=5, column=2)


foablak.mainloop()