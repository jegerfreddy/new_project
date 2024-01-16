

# DOCS -> https://pypi.org/project/qrcode/

import qrcode
from PIL import Image

# Here we specify the data that we are going to store inside the QR code image.
#TODO: Can't save data img to qr code
image_path = "./data/img.jpg"
image = Image.open(image_path)

image_bytes = image.tobytes()

# Here we customize the properties of the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data("Hello World!")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="black")

img.save('images/qrcode.png')
