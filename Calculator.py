import tkinter as tk
import math

root = tk.Tk()
root.title('Scientific Calculator')
root.configure(bg='#003b5f')
root.resizable(width=False, height=False)


ent_field = tk.Entry(root, bg='#ADD8E6', fg='#000080', font=('Arial', 25),
                     borderwidth=10, justify="right")
ent_field.grid(row=0, columnspan=10, padx=10, pady=10,
               sticky='n'+'s'+'e'+'w')
ent_field.insert(0, '0')

FONT = ('Arial', 10, 'bold')


class SC_Calculator():
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum+secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str+val)
            self.inp_value = False
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

    def Delete_Last(self):
        current_text = ent_field.get()
        new_text = current_text[:-1] if len(current_text) > 1 else '0'
        self.Entry(new_text)
    
    def SQ_Root(self):
        try:
            self.current = math.sqrt(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Pi(self):
        self.result = False
        self.current = math.pi
        self.Entry(self.current)

    def E(self):
        self.result = False
        self.current = math.e
        self.Entry(self.current)

    def Deg(self):
        try:
            self.result = False
            self.current = math.degrees(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Rad(self):
        try:
            self.result = False
            self.current = math.radians(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Exp(self):
        try:
            self.result = False
            self.current = math.exp(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Fact(self):
        try:
            self.result = False
            self.current = math.factorial(float(ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_sin.grid(row=3, column=4, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_cos = tk.Button(root, text='cos', command=lambda: sc_app.Cos(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_cos.grid(row=3, column=5, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_tan = tk.Button(root, text='tan', command=lambda: sc_app.Tan(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_tan.grid(row=3, column=6, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_sinh = tk.Button(root, text='sinh', command=lambda: sc_app.Sinh(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_sinh.grid(row=4, column=4, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_cosh = tk.Button(root, text='cosh', command=lambda: sc_app.Cosh(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_cosh.grid(row=4, column=5, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_tanh = tk.Button(root, text='tanh', command=lambda: sc_app.Tanh(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_tanh.grid(row=4, column=6, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_ln = tk.Button(root, text='ln', command=lambda: sc_app.Ln(),
                   font=FONT, width=5, height=2, fg="#000000",
                   highlightbackground='#ADD8E6', highlightthickness=2)
btn_ln.grid(row=5, column=4, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_log2 = tk.Button(root, text='log2', command=lambda: sc_app.Log_2(),
                     font=FONT, width=5, height=2, fg="#000000",
                     highlightbackground='#ADD8E6', highlightthickness=2)
btn_log2.grid(row=5, column=5, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_log10 = tk.Button(root, text='log10', command=lambda: sc_app.Log_10(),
                      font=FONT, width=5, height=2, fg="#000000",
                      highlightbackground='#ADD8E6', highlightthickness=2)
btn_log10.grid(row=5, column=6, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_x_pow2 = tk.Button(root, text='x\u00B2', command=lambda: sc_app.Pow_2(),
                       font=FONT, width=5, height=2, fg="#000000",
                       highlightbackground='#ADD8E6', highlightthickness=2)
btn_x_pow2.grid(row=1, column=7, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_x_pow3 = tk.Button(root, text='x\u00B3', command=lambda: sc_app.Pow_3(),
                       font=FONT, width=5, height=2, fg="#000000",
                       highlightbackground='#ADD8E6', highlightthickness=2)
btn_x_pow3.grid(row=2, column=7, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_10_pow_n = tk.Button(root, text='10\u207F', command=lambda: sc_app.Pow_10_n(),
                         font=FONT, width=5, height=2, fg="#000000",
                         highlightbackground='#ADD8E6', highlightthickness=2)
btn_10_pow_n.grid(row=3, column=7, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_1div_by_x = tk.Button(root, text='1/x', command=lambda: sc_app.One_div_x(),
                          font=FONT, width=5, height=2, fg="#000000",
                          highlightbackground='#ADD8E6', highlightthickness=2)
btn_1div_by_x.grid(row=4, column=7, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_abs = tk.Button(root, text='Abs', command=lambda: sc_app.Abs(),
                    font=FONT, width=5, height=2, fg="#000000",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_abs.grid(row=5, column=7, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

if __name__ == '__main__':

    sc_app = SC_Calculator()

    root.mainloop()
