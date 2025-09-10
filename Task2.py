from tkinter import *
from tkinter import filedialog, messagebox
import os

def process_image(mode):
    try:
        key = key_entry.get()
        if not key.isdigit() or not (1 <= int(key) <= 255):
            messagebox.showerror("Error", "Please enter a numeric key between 1 and 255")
            return
        key = int(key)

        filepath = filedialog.askopenfilename(
            title=f"Select Image to {mode.upper()}",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if not filepath:
            return

        with open(filepath, 'rb') as f:
            image_data = bytearray(f.read())

        for i in range(len(image_data)):
            image_data[i] ^= key

        base, ext = os.path.splitext(filepath)
        out_filename = f"{base}_{mode}{ext}"
        with open(out_filename, 'wb') as f:
            f.write(image_data)

        messagebox.showinfo("Success", f"Image {mode}ed successfully!\nSaved as:\n{out_filename}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = Tk()
root.title("IMAGE ENCRYPT & DECRYPT")
root.geometry("400x300")
root.config(bg="lightblue")

frame = Frame(root, bg="lightyellow", bd=5, relief=RIDGE)
frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=350, height=200)

title_label = Label(frame, text="🔒 IMAGE ENCRYPTION", font=("Arial", 14, "bold"), bg="lightyellow")
title_label.pack(pady=5)

label = Label(frame, text="ENTER A KEY TO ENCRYPT & DECRYPT AN IMAGE", font=("Arial", 10), bg="lightyellow")
label.pack(pady=5)

key_entry = Entry(frame, font=("Arial", 14), justify="center")
key_entry.pack(pady=10)

btn_frame = Frame(frame, bg="lightyellow")
btn_frame.pack(pady=10)

encrypt_btn = Button(btn_frame, text="ENCRYPT", bg="red", fg="white", font=("Arial", 12, "bold"),
                     width=10, command=lambda: process_image("encrypt"))
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = Button(btn_frame, text="DECRYPT", bg="blue", fg="white", font=("Arial", 12, "bold"),
                     width=10, command=lambda: process_image("decrypt"))
decrypt_btn.grid(row=0, column=1, padx=10)

root.mainloop()
