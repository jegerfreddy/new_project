

# DOCS -> https://pypi.org/project/qrcode/

import qrcode
from PIL import Image

# Here we specify the data that we are going to store inside the QR code image.
image_path = "./data/img.png"
image = Image.open(image_path)

image_bytes = image.tobytes()

# Here we customize the properties of the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4
)

# Add the data to the customized QR code.
qr.add_data(image_bytes)

qr.make(fit=True)
img = qr.make_image(back_color=(255, 0, 0), fill_color=(255, 255, 255))

img.save('images/qrcode.png')
