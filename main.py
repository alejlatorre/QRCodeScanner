"""
Created on Sun Dec 25 15:59:18 2022

@author: Alejandro Latorre Rojas
"""

import pickle

import uvicorn
from fastapi import FastAPI

app = FastAPI()

OUTPUT_PATH = 'outputs/'
PKL_FILENAME = 'qr_code_scanner_v1.pkl'
qrcs = pickle.load(open(OUTPUT_PATH + PKL_FILENAME, 'rb'))

# Index route, opens automatically on https://127.0.0.1:8000
@app.get('/')
async def root():
    return {'message': 'Hello World'}


# Expose the qr code extractor
@app.post('/qr_extraction')
def qr_extraction(filename):
    print(f'Filename: {filename}')
    image = qrcs.read_image(filename)
    qr_text = qrcs.extract_info(img=image)
    print(f'Text: {qr_text}')
    return {'text': qr_text}


# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn main:app --reload
# sudo lsof -t -i tcp:8000 | xargs kill -9
