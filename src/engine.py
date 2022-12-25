import cv2
import matplotlib
import numpy as np
from pyzbar.pyzbar import decode


class QRCodeScanner:
    def __init__(self, show_images=False):
        self.show_images = show_images
        if show_images:
            matplotlib.use(arg='TkAgg', warn=False, force=True)

    def read_image(self, filename):
        image = cv2.imread(filename)
        if self.show_images:
            dim = image.shape
            self.bi_dim = (dim[1], dim[0])
            cv2.imshow('Default image', image)
            cv2.waitKey()
            cv2.destroyWindow(winname='Default image')
        return image

    def extract_info(self, img):
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

        if self.show_images:
            img_resized = cv2.resize(src=img, dsize=self.bi_dim)
            cv2.imshow('QR codes detection', img_resized)
            cv2.waitKey()
            cv2.destroyWindow(winname='QR codes detection')
        return decoded_list
