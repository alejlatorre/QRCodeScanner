import cv2
import numpy as np
from pyzbar.pyzbar import decode

# import matplotlib

# matplotlib.use(arg='TkAgg', warn=False, force=True)


class QRCodeScanner:
    def __init__(self, show_images=False):
        pass

    def read_image(self, filename):
        self.image = cv2.imread(filename)

    def extract_info(self):
        img = self.image
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
        return decoded_list
