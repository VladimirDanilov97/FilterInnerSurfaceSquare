import tkinter as tk
from tkinter import ttk
from math import pi, asin, cos

class Filter():
    def __init__(self, D, H, R, r, h):
        self.D = D
        self.H = H
        self.R = R
        self.r = r
        self.h = h
    def calculate_surface(self):
        s1 = pi*self.D*self.H
        s2 = 2 * pi*self.D**2/4
        fk = self.r/self.D
        fd = self.R/self.D

        phi = asin((0.5-fk)/(fd-fk))

        s3_1 = self.R**2*(1-cos(phi))
        s3_2 =  (self.D/2-self.r * (1-2*cos(phi)/(pi-2*phi)))*(pi/2-phi)
        s3_3 = pi*self.D*self.h

        s3 = 2*(2*pi*(s3_1 + self.r*s3_2) + s3_3)

        return round((s1+s2+s3)*10**-6, 0)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Внутренняя поверхность фильтра')

        self.D_label = ttk.Label(self, text='Внутренний диаметр')
        self.D_label.grid(row=1, column=1)
        self.D_entry = ttk.Entry()
        self.D_entry.grid(row=1, column=2)

        self.H_label = ttk.Label(self, text='Высота обечайки')
        self.H_label.grid(row=2, column=1)
        self.H_entry = ttk.Entry()
        self.H_entry.grid(row=2, column=2)

        
        self.h_label = ttk.Label(self, text='Высота отбортовки')
        self.h_label.grid(row=3, column=1)
        self.h_entry = ttk.Entry()
        self.h_entry.grid(row=3, column=2)

        self.R_label = ttk.Label(self, text='Радиус днища')
        self.R_label.grid(row=4, column=1)
        self.R_entry = ttk.Entry()
        self.R_entry.grid(row=4, column=2)

        self.r_label = ttk.Label(self, text='Радиус отбортовки')
        self.r_label.grid(row=5, column=1)
        self.r_entry = ttk.Entry()
        self.r_entry.grid(row=5, column=2)

        self.answer = ttk.Label(self, text='')
        self.answer.grid(row=6, column=1, columnspan=2)
        self.btn = ttk.Button(self, text='calculate', command=self.btn_on_click) 
        self.btn.grid(row=7, column=1, columnspan=2)

    def btn_on_click(self):
        D = int(self.D_entry.get())
        H = int(self.H_entry.get())
        R = int(self.R_entry.get())
        r = int(self.r_entry.get())
        h = int(self.h_entry.get())

        f = Filter(D=D, H=H, R=R, r=r, h=h)
        answer = f.calculate_surface()

        self.answer.config(text = str(answer))

if __name__ == '__main__':
    app = App()
    app.mainloop()  

    
    