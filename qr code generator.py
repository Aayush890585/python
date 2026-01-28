import qrcode

data = "https://www.kaggle.com/"

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H  # High redundancy
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(
    fill_color="blue",
    back_color="white"
)

img.save("custom_qr.png")
