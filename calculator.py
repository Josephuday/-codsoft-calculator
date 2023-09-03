import tkinter as tk

def clear():
    entry.delete(0, tk.END)

def btn_clk(num):
    cur_num = entry.get()
    clear()
    f_num = cur_num + num
    entry.insert(0, f_num)

def calc(math_type):
    global first_num, math
    math = math_type
    first_num = entry.get()
    clear()

def equal():
    result = ''
    global first_num
    second_num = entry.get()
    clear()
    if math == 'add':
        result = int(first_num) + int(second_num)
    elif math == 'sub':
        result = int(first_num) - int(second_num)
    elif math == 'mul':
        result = int(first_num) * int(second_num)
    elif math == 'div':
        if int(second_num) != 0:
            result = int(first_num) / int(second_num)
        else:
            result = "Cannot divide by zero"
    entry.insert(0, str(result))

try:
    mw = tk.Tk()
    mw.title('Calculator')

    entry = tk.Entry(mw, width=14, font=('Arial', 28), justify=tk.RIGHT)

    btn_0 = tk.Button(mw, text='0', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('0'))
    btn_1 = tk.Button(mw, text='1', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('1'))
    btn_2 = tk.Button(mw, text='2', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('2'))
    btn_3 = tk.Button(mw, text='3', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('3'))
    btn_4 = tk.Button(mw, text='4', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('4'))
    btn_5 = tk.Button(mw, text='5', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('5'))
    btn_6 = tk.Button(mw, text='6', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('6'))
    btn_7 = tk.Button(mw, text='7', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('7'))
    btn_8 = tk.Button(mw, text='8', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('8'))
    btn_9 = tk.Button(mw, text='9', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('9'))

    btn_clear = tk.Button(mw, text='clear', padx=74, pady=10, font=('Arial', 14), command=clear)
    btn_div = tk.Button(mw, text='/', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('div'))
    btn_mul = tk.Button(mw, text='*', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('mul'))
    btn_sub = tk.Button(mw, text='-', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('sub'))
    btn_add = tk.Button(mw, text='+', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('add'))
    btn_equal = tk.Button(mw, text='=', padx=36, pady=40, font=('Arial', 14), command=equal)

    # showing widgets
    btn_equal.grid(row=5, column=2, rowspan=2, padx=2, pady=2)
    btn_add.grid(row=6, column=1, padx=2, pady=2)
    btn_sub.grid(row=6, column=0, padx=2, pady=2)
    btn_mul.grid(row=5, column=1, padx=2, pady=2)
    btn_div.grid(row=5, column=0, padx=2, pady=2)

    btn_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)
    btn_0.grid(row=4, column=0, padx=2, pady=2)

    btn_1.grid(row=3, column=0, padx=2, pady=2)
    btn_2.grid(row=3, column=1, padx=2, pady=2)
    btn_3.grid(row=3, column=2, padx=2, pady=2)
    btn_4.grid(row=2, column=0, padx=2, pady=2)
    btn_5.grid(row=2, column=1, padx=2, pady=2)
    btn_6.grid(row=2, column=2, padx=2, pady=2)

    btn_7.grid(row=1, column=0, padx=2, pady=2)
    btn_8.grid(row=1, column=1, padx=2, pady=2)
    btn_9.grid(row=1, column=2, padx=2, pady=2)
    entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    mw.mainloop()

except tk.TclError:
    print("This environment doesn't support graphical interfaces.")
    print("You can't run this program in a text-only terminal.")