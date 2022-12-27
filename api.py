"""
Created on Sun Dec 25 15:59:18 2022

@author: Alejandro Latorre Rojas
"""
import uvicorn
from fastapi import FastAPI, File, UploadFile
from PIL import Image

from src.engine import QRCodeScanner

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello Truora'}


@app.post('/get_text')
def extract_text(
    img: UploadFile = File(
        ...,
        title='QR decoder',
        description='API that extracts link associated to QR images',
    )
):
    qrcs = QRCodeScanner()
    qr_text = qrcs.extract_info(img=Image.open(img.file), decode_image=True)
    return {'text': qr_text}
    # if qr_img:
    #     qrcs = QRCodeScanner()
    #     qr_text = qrcs.extract_info(img=qr_img[0].data)
    #     return {'text': qr_text}


# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn main:app --reload
# sudo lsof -t -i tcp:8000 | xargs kill -9
# https://www.youtube.com/watch?v=kVoZ5CZRy4A
# Firebase
