import tkinter as tk
from tkinter import messagebox

def hitung_diskon():
    try:
        # get value from entry
        harga_asli = float(entry_harga.get())
        diskon = float(entry_diskon.get())
        
        # formula
        hasil = harga_asli - (harga_asli * (diskon / 100))
        
        # update labeloutput
        label_hasil.config(text=f"Rp {hasil:,.2f}")
        
    except ValueError:
        messagebox.showerror("Error", "Input the right nominal")

window = tk.Tk()
window.title("Kalkulator Diskon Simple")
window.geometry("300x250")

# Label & Input Harga
tk.Label(window, text="Original Price:").pack(pady=5)
entry_harga = tk.Entry(window, background="lightgray")
entry_harga.pack()

# Label & Inputdiskon
tk.Label(window, text="Discount (%):").pack(pady=5)
entry_diskon = tk.Entry(window, background="lightgray")
entry_diskon.pack()

# Button
btn_hitung = tk.Button(window, text="Calculate!", command=hitung_diskon, background="aquamarine", foreground="black")
btn_hitung.pack(pady=20)

# Result Output
label_hasil = tk.Label(window, text="Rp 0", font=("Arial", 14, "bold"))
label_hasil.pack()

window.mainloop()