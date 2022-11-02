import tkinter as tk
import time

window = tk.Tk()
window.title("Калькулятор")
window.geometry('500x500')
window.resizable(False, False)
window.configure(bg='grey')


def calculate(operation):
    """Считает данные"""
    global output_window
    try:
        if operation == 'C':  # Pass
            output_window = ''
        elif operation == 'Del':  # Pass
            output_window = output_window[0:-1]
        elif operation == 'x^2':
            output_window = str((eval(output_window)) ** 2)  # Pass
        elif operation == '=':  # Pass
            output_window = str(eval(output_window))
        elif operation == '%':
            output_window = str((eval(output_window)) / 100)  # Fail
        else:
            if output_window == '0':  # Pass
                output_window = ''
            output_window += operation
        label_text.configure(text=output_window)
    except ZeroDivisionError:
        label_text.configure(text=f'Делить на 0 нельзя')
        if output_window == 'Делить на 0 нельзя':
            label_text.configure(text=f'0')
    except SyntaxError:
        label_text.configure(text='Ошибка')


"""Окно вывода"""
output_window = '0'
label_text = tk.Label(text=output_window, font=('Roboto', 30, 'bold'), bg='grey', fg='white')
label_text.place(x=18, y=30)

buttons = ['%', 'C', '*', 'Del', '7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '/', 'x^2', '0']
equal_sum = '='
x = 18
y = 90

for button in buttons:
    """Создание кнопок"""
    get_lbp = lambda x=button: calculate(x)
    tk.Button(text=button, bg='white', font=('Arial', 20), command=get_lbp).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 18
        y += 81

get_lbp = lambda x=equal_sum: calculate(x)
tk.Button(text=equal_sum, bg='white', font=('Arial', 20), command=get_lbp).place(x=x, y=y, width=232, height=79)
x += 117
if x > 400:
    x = 18
    y += 81

window.mainloop()
