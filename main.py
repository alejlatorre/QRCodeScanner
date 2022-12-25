# %% 0. Libraries
import cv2
import matplotlib

matplotlib.use(arg='TkAgg', warn=False, force=True)
import numpy as np
from pyzbar.pyzbar import decode

# %% 1. Config
DATA_PATH = 'data/'
OUTPUT_PATH = 'outputs/'

# %% 2. Load image, convert to grayscale and Otsu's threshold
# FILENAME = 'istockphoto-1095468748-612x612.jpg'
# FILENAME = 'qrcode_rotated.jpg'
# FILENAME = 'qrcode_rotated_with_background.png'
FILENAME = 'qrcode_sproutqr.jpg'
# FILENAME = 'multi_qrcodes.png'
img = cv2.imread(DATA_PATH + FILENAME)
dim = img.shape
bi_dim = (dim[1], dim[0])
cv2.imshow('Default', img)

decoded_list = []
for d in decode(img):
    img = cv2.rectangle(
        img,
        (d.rect.left, d.rect.top),
        (d.rect.left + d.rect.width, d.rect.top + d.rect.height),
        (255, 0, 0),
        2,
    )
    img = cv2.polylines(img, [np.array(d.polygon)], True, (0, 255, 0), 2)
    img = cv2.putText(
        img,
        d.data.decode(),
        (d.rect.left, d.rect.top + d.rect.height),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 255),
        1,
        cv2.LINE_AA,
    )
    decoded_list.append(d.data.decode())

img_resized = cv2.resize(src=img, dsize=bi_dim)
cv2.imshow('Detection', img)
cv2.waitKey()
cv2.destroyWindow()

for i, val in enumerate(iterable=text_list):
    print('######################################')
    print(f'N{i}: {val}')
    print('######################################')

# FILENAME = 'qrcode_sproutqr_opencv.jpg'
# cv2.imwrite(OUTPUT_PATH + FILENAME, img)
# cv2.imread()
# cv2.imshow('Detection', img)
# cv2.waitKey(0)
# cv2.destroyWindow(winname='Detection')

# %%
