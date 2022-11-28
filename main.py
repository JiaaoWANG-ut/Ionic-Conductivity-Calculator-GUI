from tkinter import *

 

root = Tk()

root.title('Ionic Conductivity Calculator')

 
frame = Frame(root)

frame.pack(padx=10, pady=10)

 

v1 = DoubleVar()

v2 = DoubleVar()

v3 = DoubleVar()

a = DoubleVar()
b = DoubleVar()
c = DoubleVar()
n = DoubleVar()
D = DoubleVar()
T = DoubleVar()
def test(content):

    return content.isdigit()

 
testCMD = frame.register(test)














Label(frame, text='Conductivity Calculator: Based on Nernst-Einstein Equation',justify=LEFT).grid(row=0, column=1)

Label(frame, text='k=n/(V·N)·D·(F^2/RT), ions type=Li, z=1').grid(row=1, column=1)

Label(frame, text='n: Ions number',justify=LEFT).grid(row=2, column=1)


Entry(frame, width=10, textvariable=n, validate='key', \

           validatecommand=(testCMD, '%P')).grid(row=2, column=3)


Label(frame, text='V: Volume(a*b*c) (nm^3)').grid(row=3, column=1)


Entry(frame, width=10, textvariable=a, validate='key', \

           validatecommand=(testCMD, '%P')).grid(row=3, column=3)

Entry(frame, width=10, textvariable=b, validate='key', \

           validatecommand=(testCMD, '%P')).grid(row=3, column=4)
    
Entry(frame, width=10, textvariable=c, validate='key', \

           validatecommand=(testCMD, '%P')).grid(row=3, column=5)
    


Label(frame, text='N: Avogadro constant').grid(row=4, column=1)

Label(frame, text='F: Faraday\'s  constant').grid(row=5, column=1)

Label(frame, text='R: Ideal gas constant').grid(row=6, column=1)

Label(frame, text='T: Temperature (K)').grid(row=7, column=1)

Entry(frame, width=10, textvariable=T, validate='key', \

           validatecommand=(testCMD, '%P')).grid(row=7, column=3)

Label(frame, text='D: Diffusion Coff (cm^2/s)').grid(row=8, column=1)

Entry(frame, width=10, textvariable=D, validate='key', \

           validatecommand=(testCMD, '%P')).grid(row=8, column=3)

    
    
    
Label(frame, text='Ionic Conductivity').grid(row=9, column=1)

Entry(frame, width=30, textvariable=v3, state='readonly').grid(row=9, column=4)

Label(frame, text='mS/cm').grid(row=9, column=5)



Label(frame, text='Jiaao Wang@ Henkelman Group, Li-ion Conductivity Calculator,     email:wangjiaao0720@utexas.edu').grid(row=15, column=1)

def calc():

    result = float(n.get()) / ( float(a.get()) * float(b.get()) * float(c.get()) * 602 ) * 1000 * float(D.get())* (96500**2/(8.314*float(T.get())))

    v3.set(str(result))

 

Button(frame, text='Calculate', command=calc).grid(row=10, column=20, pady=50)

 

mainloop()
