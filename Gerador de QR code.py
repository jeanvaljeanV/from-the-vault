import qrcode

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=11,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

# texto gerador de QR Code
text = "https://b001.io"

# Nome do arquivo
file_name = r"C:\Users\jean1\Desktop\qr_code.png"

#gerar QR Code
generate_qr_code(text, file_name)
print(f"QR code saved as {file_name}")