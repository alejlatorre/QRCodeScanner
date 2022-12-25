import pickle
from datetime import datetime

from src.engine import QRCodeScanner

OUTPUT_PATH = 'outputs/'

FILENAME = 'qr_code_scanner_v1.pkl'
outfile = open(OUTPUT_PATH + FILENAME, 'wb')
pickle.dump(QRCodeScanner(), outfile)
outfile.close()

infile = open(OUTPUT_PATH + FILENAME, 'rb')
qrcs = pickle.load(infile)
print(dir(qrcs))
infile.close()
