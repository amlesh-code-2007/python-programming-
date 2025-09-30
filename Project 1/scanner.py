# Genrate a QR Code Using Python

import qrcode
data = "Shivam kumar"

qr = qrcode.make(data)

qr.save("qrcode.png")

print("Qr Code Generated Successfully! ")