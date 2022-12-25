import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo

from src.engine import QRCodeScanner

root = tk.Tk()
root.title('QR Code Scanner')
root.resizable(False, False)
root.geometry('300x80')


def select_file():
    filetypes = (('PNG files', '*.png'), ('JPG files', '*.jpg'))
    filename = fd.askopenfilename(
        title='Select a QR Code', initialdir=os.getcwd(), filetypes=filetypes
    )
    qrcs = QRCodeScanner(show_images=False)
    image = qrcs.read_image(filename=filename)
    codes = qrcs.extract_info(img=image)
    for code in codes:
        print(code)
    exit()


open_button = ttk.Button(root, text='Select a QR Code', command=select_file)
open_button.pack(expand=True)

root.mainloop()
