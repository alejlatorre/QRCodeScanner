# %% 0. Libraries
import cv2
import matplotlib

matplotlib.use(arg='TkAgg', warn=False, force=True)
# import numpy as np

# %% 1. Config
DATA_PATH = 'data/'
OUTPUT_PATH = 'output/'

# %% 2. Load image, convert to grayscale and Otsu's threshold
FILENAME = 'istockphoto-1095468748-612x612.jpg'
img = cv2.imread(DATA_PATH + FILENAME)
gray_img = 255 - cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', gray_img)
cv2.waitKey()
cv2.destroyAllWindows()


# NOW = datetime.now().strftime('%Y%m%d%H%m%s')
# FILENAME = f'test_{NOW}.png'


# thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# # %% 3. Compute rotated bounding box
# coordinates = np.column_stack(np.where(thresh > 0))
# angle = cv2.minAreaRect(coordinates)[-1]

# angle = -(90 + angle) if angle < -45 else -angle
# print(f'Skew angle: {angle}')

# # %% 4. Rotate image to deskew
# (h, w) = img.shape[:2]
# center = (w // 2, h // 2)
# rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
# rotated = cv2.warpAffine(
#     img, rotation_matrix, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE
# )

# cv2.imshow('Rotated', rotated)
# cv2.waitKey()

# %%
