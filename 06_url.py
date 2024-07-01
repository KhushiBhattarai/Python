import qrcode
img = qrcode.make("https://www.youtube.com/watch?v=R3K1sFYGmmc")
type(img)
img.save("website.png")