import qrcode

phone = "9816134847"
message ="hello meow k xa"
sms = f"SMSTO:{phone}:{message}"
img = qrcode.make(sms)
type(img)  # qrcode.image.pil.PilImage
img.save("sms.png")
