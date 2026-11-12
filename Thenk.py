import random
import tkinter as tk
from tkinter import messagebox

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def generate():
    
    code = entry_code.get().strip()
    if len(code) != 3 or not code.isdigit():
        messagebox.showerror("Ошибка", "Нужно ровно 3 цифры, например 123")
        return
    
    block = ""
    for i in range(5):
        block += block.join(random.choice(ALPHABET))
    blocks = [block]

    b = block
    for j in range(3):
        step = int(str(code)[j])
        dl = random.choice(range(5 - j))
        b = b[:dl] + b[dl + 1:]
        bl = ""

        if j % 2 == 0:
            for f in range(len(b)):
                bl += ALPHABET[(ALPHABET.index(b[f]) + step) % 36]
        else:
            for f in range(len(b)):
                bl += ALPHABET[(ALPHABET.index(b[f]) - step) % 36]

        blocks.append(bl)

    entry_key.config(state='normal')
    entry_key.delete(0, tk.END)
    entry_key.insert(0, '-'.join(blocks))
    entry_key.config(state='readonly')


def close():
    window.destroy()


window = tk.Tk()
window.geometry('474x474')
bg_img = tk.PhotoImage(file='pic.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_code = tk.Label(frame, text='DEC:', font=('Arial', 20), bg='blue', fg='white')
lbl_code.grid(column=0, row=0, padx=10, pady=15)
entry_code = tk.Entry(frame, width=10)
entry_code.insert(0, '123')
entry_code.grid(column=1, row=0, padx=10, pady=15)

lbl_key = tk.Label(frame, text='Key:', font=('Arial', 20))
lbl_key.grid(column=0, row=1, padx=10, pady=15)
entry_key = tk.Entry(frame, width=28, state='readonly', justify='center')
entry_key.grid(column=1, row=1, padx=10, pady=15)

btn_gen = tk.Button(frame, text='Generate', command=generate)
btn_gen.grid(column=0, row=2, padx=10, pady=15)
btn_exit = tk.Button(frame, text='Close', command=close)
btn_exit.grid(column=1, row=2, padx=10, pady=15)

window.mainloop()