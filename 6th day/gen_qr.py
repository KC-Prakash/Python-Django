import qrcode
img = qrcode.make('https://google.com')
type(img)  # qrcode.image.pil.PilImage
img.save("google.png")