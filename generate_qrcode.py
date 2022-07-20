import qrcode

input_URL = "https://www.discord.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="#7289da", back_color="#ffffff")
img.save("discord_qrcode.png")

print(qr.data_list)
