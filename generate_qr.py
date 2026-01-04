import qrcode

url = "https://makeupstarstudio.netlify.app/"

img = qrcode.make(url)
img.save("business_card_qr.png")

print("QR generated")
