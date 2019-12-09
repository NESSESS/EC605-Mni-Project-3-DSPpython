import sympy as sp
from sympy import Heaviside
from sympy.plotting import plot
from tkinter import*
def cvtTime(timestring,lapstring):
    s, t = sp.symbols('s, t')
    expression =lapstring.get()
    ans=sp.inverse_laplace_transform(expression, s, t)
    timestring.set(str(ans))

def cvtLaplace(timestring,lapstring):
    s, t = sp.symbols('s, t')
    expression =timestring.get()
    ans=sp.laplace_transform(expression, t, s)
    lapstring.set(ans[0])
def showtime(timestring,lapstring,left,right):
    if(left!=""and right!=""):
        lv=float(left.get())
        rv=float(right.get())
    s, t = sp.symbols('s, t')
    out=timestring.get()
    if lv==0:
        lv=0.01
    if lv>rv:
        rv=lv+0.01
    plot(out,(t,lv,rv))
def showlap(timestring,lapstring,left,right):
    if(left!=""and right!=""):
        lv=float(left.get())
        rv=float(right.get())
    s, t = sp.symbols('s, t')
    if lv<=0:
        lv=0.01
    if lv>rv:
        rv=lv+0.01
    out=lapstring.get()
    plot(out,(s,lv,rv))
top=Tk()
top.title('Laplace converter')
timestring=StringVar()
timestring.set("only 't' is allowed")
lapstring=StringVar()
lapstring.set("only 's' is allowed")
left=StringVar()
left.set("0")
right=StringVar()
right.set("15")
Label(top,text="Time:").grid(row=0, column=0, sticky='e')
Label(top, text="Laplace:").grid(row=1, column=0, sticky='e')
timeEntry=Entry(top,textvariable=timestring)
timeEntry.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=9)
lapEntry=Entry(top,textvariable=lapstring)
lapEntry.grid(row=1,column=1,padx=2,pady=2,sticky='we',columnspan=9)
cvl=Button(top, text="Convert to Laplace",command=lambda : cvtLaplace(timestring,lapstring))
cvl.grid(row=0, column=10, sticky='ew',padx=2, pady=2,columnspan=4)
cvt=Button(top, text="Convert to Time",command=lambda:cvtTime(timestring,lapstring))
cvt.grid(row=1, column=10, sticky='ew',padx=2, pady=2,columnspan=4)
showl=Button(top, text="Show figure",command=lambda:showlap(timestring,lapstring,left,right))
showl.grid(row=1,column=15,sticky='we',)
showt=Button(top, text="Show figure",command=lambda:showtime(timestring,lapstring,left,right))
showt.grid(row=0,column=15,sticky='we',)
Label(top,text="Min:").grid(row=2, column=0, sticky='e')
Label(top, text="Max:").grid(row=2, column=8, sticky='e')
l=Entry(top,textvariable=left)
l.grid(row=2,column=1)
r=Entry(top,textvariable=right)
r.grid(row=2,column=9)
top.mainloop()

