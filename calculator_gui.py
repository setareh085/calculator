import tkinter as tk

# --- توابع ---
def press(num):
    """هر بار که روی دکمه کلیک می‌کنی، متن وارد نمایشگر میشه"""
    entry_var.set(entry_var.get() + str(num))

def clear():
    """پاک کردن نمایشگر"""
    entry_var.set("")

def calculate():
    """محاسبه عبارت وارد شده"""
    try:
        result = eval(entry_var.get())   # محاسبه رشته ریاضی
        entry_var.set(str(result))
    except:
        entry_var.set("Error")          # در صورت خطا

# --- ساخت پنجره اصلی ---
root = tk.Tk()
root.title("Calculator")

# --- نمایشگر (Entry) ---
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=5)

# --- دکمه‌ها ---
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=2, pady=2)

# --- دکمه پاک کردن ---
clear_btn = tk.Button(root, text="C", width=5, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="we")

# --- اجرای برنامه ---
root.mainloop()
