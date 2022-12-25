# %% 0. Libraries
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo

from src.engine import QRCodeScanner

root = tk.Tk()
root.title('QR Code Scanner')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (('PNG files', '*.png'), ('JPG files', '*.jpg'))
    filename = fd.askopenfilename(
        title='Open a file', initialdir='/', filetypes=filetypes
    )
    qrcs = QRCodeScanner()
    qrcs.read_image(filename=filename)
    codes = qrcs.extract_info()
    for i, code in enumerate(codes):
        print(f'N{i}: {code}')
    exit()


open_button = ttk.Button(root, text='Open an image', command=select_file)
open_button.pack(expand=True)

root.mainloop()

# %% 2. Load image, convert to grayscale and Otsu's threshold
# FILENAME = 'istockphoto-1095468748-612x612.jpg'
# FILENAME = 'qrcode_rotated.jpg'
# FILENAME = 'qrcode_rotated_with_background.png'
# FILENAME = 'qrcode_sproutqr.jpg'
# FILENAME = 'multi_qrcodes.png'
# FILENAME = 'qrcode_sproutqr_opencv.jpg'
# cv2.imwrite(OUTPUT_PATH + FILENAME, img)
# cv2.imread()
# cv2.imshow('Detection', img)
# cv2.waitKey(0)
# cv2.destroyWindow(winname='Detection')

# %%
