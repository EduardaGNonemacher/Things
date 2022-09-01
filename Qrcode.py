import pyqrcode
import png
from pyqrcode import QRCode

QrString = input('Link Para o QRcode: ')

Url = pyqrcode.create(QrString)

Url.png(r'QrCode.png', scale = 8)

print('QrCode criado com sucesso!!')

