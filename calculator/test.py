from tkinter import *
import numpy as np
import math
import re 

window = Tk()
window.title('My Calculator')
window.geometry('680x200')

# data enty box
el = Entry(window, font=('arial',20,'bold'),bd=10,bg='#808080', width=24, justify=RIGHT)
el.grid(row=0, column=0)

# output box
text = Text(window, height=1.2, width=32,font=('arial',15,'bold'),bd=10,bg='#808080')
text.grid(row=1, column=0)

# out operation
def func():
    text.delete("1.0", END)  # refreshing output box
    number = el.get()
    # sin function operation
    try:
        
        if 'sin' in number:
            pattern = re.compile(r"sin\((.*?)\)")
            matches = pattern.findall(number)
            num = []
            for i in matches:
                num.append(eval(str(i)))
            
            for num in num:
                sin_val = math.sin(num)
            
                number = number.replace(f'sin({str(num)})', f'{sin_val}')
        
        # cos function operation
        if 'cos' in number:
            pattern = re.compile(r"cos\((.*?)\)")
            matches = pattern.findall(number)
            num = []
            for i in matches:
                num.append(eval(str(i)))
            
            for num in num:
                cos_val = math.cos(num)
            
                number = number.replace(f'cos({str(num)})', f'{cos_val}')
        
        # tan function operation

        if 'tan' in number:
            pattern = re.compile(r"tan\((.*?)\)")
            matches = pattern.findall(number)
            num = []
            for i in matches:
                num.append(eval(str(i)))
            
            for num in num:
                tan_val = math.tan(num)
            
                number = number.replace(f'tan({str(num)})', f'{tan_val}')
            
            result = str(eval(number))

            text.insert(END, result)

        else:
            result = str(eval(number))
    
            text.insert(END, result)        

    except:
        text.insert(END, 'Error')
        print('Error')
    
# plus
def sum_func():
    el.insert(END, '+')
# multiplication
def mul_func():
    el.insert(END, '*')
# divide
def div_func():
    el.insert(END, '/')
# substraction
def subs_func():
    el.insert(END, '-')

# sin func
def sin_func():    
    el.insert(END, 'sin(')

# cos func
def cos_func():    
    el.insert(END, 'cos(')

# tan func
def tan_func():    
    el.insert(END, 'tan(')

# clear output
def cl_func():
    el.delete(0, END)
    text.delete("1.0", END)


# out button
b1 = Button(window, text='=',
 command= func,width=10,height=2,font=('arial',10,'bold'),bd=4,bg="orange")
b1.grid(row=2, column=0)

# scientific operation buttons
b2 = Button(window, text='+', command= sum_func,
width=3,height=1,font=('arial',15,'bold'),bd=4,bg="grey")
b2.grid(row=0, column=5)

b3 = Button(window, text='x', command= mul_func,
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b3.grid(row=1, column=5)

b4 = Button(window, text='/', command= div_func, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b4.grid(row=3, column=5)

b5 = Button(window, text='-', command= subs_func, 
width=3,height=1,font=('arial',15,'bold'),bd=4,bg="grey")
b5.grid(row=2, column=5)

b6 = Button(window, text='C', command= cl_func, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b6.grid(row=3, column=6)

b6 = Button(window, text='sin', command= sin_func, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b6.grid(row=0, column=6)

b7 = Button(window, text='cos', command= cos_func, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b7.grid(row=1, column=6)

b8 = Button(window, text='tan', command= tan_func, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b8.grid(row=2, column=6)

# basic numerical buttons
dot = lambda : el.insert(END, '.')
b9 = Button(window, text='.', command= dot, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b9.grid(row=3, column=3)

zero = lambda : el.insert(END, '0')
b10 = Button(window, text='0', command= zero, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b10.grid(row=3, column=2)

one = lambda : el.insert('end', '1')
b11 = Button(window, text='1', command= one, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b11.grid(row=2, column=4)

two = lambda : el.insert(END, '2')
b12 = Button(window, text='2', command= two, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b12.grid(row=2, column=3)

three = lambda : el.insert(END, '3')
b13 = Button(window, text='3', command= three, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b13.grid(row=2, column=2)

four= lambda : el.insert(END, '4')
b14 = Button(window, text='4', command= four, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b14.grid(row=1, column=4)

five = lambda : el.insert(END, '5')
b15 = Button(window, text='5', command= five, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b15.grid(row=1, column=3)

six = lambda : el.insert(END, '6')
b16 = Button(window, text='6', command= six ,
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b16.grid(row=1, column=2)

seven = lambda : el.insert(END, 7)
b17 = Button(window, text='7', command= seven, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b17.grid(row=0, column=4)

eight = lambda : el.insert(END, '8')
b18 = Button(window, text='8', command= eight, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b18.grid(row=0, column=3)

nine = lambda : el.insert(END, '9')
b19 = Button(window, text='9', command= nine, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b19.grid(row=0, column=2)

cls_br = lambda : el.insert(END, ')')
b20 = Button(window, text=')', command= cls_br, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b20.grid(row=0, column=7)

b21 = Button(window, text='Close', command= window.destroy, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="red")
b21.grid(row=3, column=4)

opn_br = lambda : el.insert(END, '(')
b22 = Button(window, text='(', command= opn_br, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b22.grid(row=1, column=7)

def dlt():
    input = el.get()
    result = input[:-1]
    el.delete(0, END)
    el.insert(END, result)

b23 = Button(window, text='DEL', command= dlt, 
width=4,height=2,font=('arial',10,'bold'),bd=4,bg="grey")
b23.grid(row=2, column=7)


window.mainloop()
