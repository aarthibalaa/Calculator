import tkinter as tk
from tkinter import font, END, messagebox
import math


window = tk.Tk()
window.title('Simple Python GUI Calculator')

root_frame = tk.Frame(window, bg="gray10")
window.geometry('490x500')

i = 1.0
equation =''

def show(value):
    global i
    global equation
    if value == "\u0025":
        value = "/100"
    equation += value
    display_box.insert(i, value)
    i += 1



def clear():
    global equation
    display_box.delete('1.0', END)
    equation = ''


def calculate():
    try: 
        global equation
        result = ''
        result = eval(equation)
        clear()
        display_box.insert('1.0',result)

    except:
        messagebox.showerror(title = 'Error', message = "Enter a valid number")


display_frame = tk.LabelFrame(root_frame, width=490, height=80, bg="gray10")
display_frame.grid(row=0, column=0, pady=(10, 10))
display_frame.grid_propagate(0)

keypad_frame = tk.LabelFrame(root_frame, width=450, height=390, bg='gray19')
keypad_frame.grid(row=1, column=0, padx=10, pady=(10, 10))
keypad_frame.grid_propagate(0)

numbers_frame = tk.LabelFrame(keypad_frame, width=240, height=360, bg="gray10")
numbers_frame.grid(row=0, column=0, padx=(10, 20), pady=(10, 10))
numbers_frame.grid_propagate(0)

signs_frame = tk.LabelFrame(keypad_frame, width=160, height=360, bg='gray10')
signs_frame.grid(row=0, column=1, pady=(10, 10))
signs_frame.grid_propagate(0)

#Screen
display_box = tk.Text(display_frame, width=25, height=1, font = ("Italic",25), bg='gray23')
display_box.grid(row=0, column=0, padx=(20,5), pady=(20,5))

#Number Button
button1 = tk.Button(numbers_frame, text ='1', width=4, height=2, command= lambda num ='1' : show('1'), bg='gray19')
button1.grid(row=0,column=0,pady=10,padx=10)

button2 = tk.Button(numbers_frame, text ='2', width=4, height=2, command= lambda num ='2' : show('2'), bg='gray19')
button2.grid(row=0,column=1,pady=10,padx=10)

button3 = tk.Button(numbers_frame, text ='3', width=4, height=2, command= lambda num ='3' : show('3'), bg='gray19')
button3.grid(row=0,column=2,pady=10,padx=10)

button4 = tk.Button(numbers_frame, text ='4', width=4, height=2, command= lambda num ='4' : show('4'), bg='gray19')
button4.grid(row=1,column=0,pady=10,padx=10)

button5 = tk.Button(numbers_frame, text ='5', width=4, height=2, command= lambda num ='5' : show('5'), bg='gray19')
button5.grid(row=1,column=1,pady=10,padx=10)

button6 = tk.Button(numbers_frame, text ='6', width=4, height=2, command= lambda num ='6' : show('6'), bg='gray19')
button6.grid(row=1,column=2,pady=10,padx=10)

button7 = tk.Button(numbers_frame, text ='7', width=4, height=2, command= lambda num ='7' : show('7'), bg='gray19')
button7.grid(row=2,column=0,pady=10,padx=10)

button8 = tk.Button(numbers_frame, text ='8', width=4, height=2, command= lambda num ='8' : show('8'), bg='gray19')
button8.grid(row=2,column=1,pady=10,padx=10)

button9 = tk.Button(numbers_frame, text ='9', width=4, height=2, command= lambda num ='9' : show('9'), bg='gray19')
button9.grid(row=2,column=2,pady=10,padx=10)

button0 = tk.Button(numbers_frame, text ='0', width=4, height=2, command= lambda num ='0' : show('0'), bg='gray19')
button0.grid(row=3,column=0,pady=10,padx=10)

button_ce = tk.Button(numbers_frame, text ='C', width=4, height=2, command=lambda: clear(), bg='gray19')
button_ce.grid(row=3,column=1,pady=10,padx=10)

button_eq = tk.Button(numbers_frame, text ='=', width=4, height=2, command=lambda: calculate() , bg='gray19')
button_eq.grid(row=3,column=2,pady=10,padx=10)

#Sign buttons

button_add = tk.Button(signs_frame, text='+',width=4, height=2, command= lambda num ='+' : show('+'), bg='gray19')
button_add.grid(row=0,column=0, pady=10, padx=10)

button_sub = tk.Button(signs_frame, text='-',width=4, height=2, command= lambda num ='-' : show('-'), bg='gray19')
button_sub.grid(row=1,column=0, pady=10, padx=10)

button_mul = tk.Button(signs_frame, text='\u00D7',width=4, height=2, command= lambda num ='*' : show('*'), bg='gray19')
button_mul.grid(row=2,column=0, pady=10, padx=10)

button_div = tk.Button(signs_frame, text='\u00F7',width=4, height=2, command= lambda num ='\u00F7' : show('/'), bg='gray19')
button_div.grid(row=3,column=0, pady=10, padx=10)

button_pnt = tk.Button(signs_frame, text='.',width=4, height=2, command= lambda num ='.' : show('.') ,bg='gray19')
button_pnt.grid(row=0,column=1, pady=10, padx=10)

button_pow = tk.Button(signs_frame, text='^',width=4, height=2, command= lambda num ='**' : show('**'), bg='gray19')
button_pow.grid(row=1,column=1, pady=10, padx=10)


button_pi = tk.Button(signs_frame, text='\u03C0',width=4, height=2, command= lambda num ='\u03C0' : show('3.1415926'), bg='gray19')
button_pi.grid(row=2,column=1, pady=10, padx=10)

button_per = tk.Button(signs_frame, text='\u0025',width=4, height=2, command= lambda num ='\u0025' : show('\u0025'), bg='gray19')
button_per.grid(row=3,column=1, pady=10, padx=10)


#apply font for button
button_font = font.Font(size = 15, weight = 'bold', family="Helvetica")

# Common values for the weight parameter include:

# "normal": Normal font weight.
# "bold": Bold font weight.
# "light": Light font weight (thinner than normal).
# "medium": Medium font weight (between normal and bold).
# "ultrabold": Very bold font weight (heavier than bold).

for button in numbers_frame.winfo_children():
    button['font'] = button_font

for button in signs_frame.winfo_children():
    button['font'] = button_font





root_frame.pack()

window.mainloop()