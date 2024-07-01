import qrcode
# img = qrcode.make('Khushi Bhattarai')
# type(img)  # qrcode.image.pil.PilImage
# img.save("khushi.png")

## wifi link
wifi_type = "WPA2-Personal"
wifi_ssid = "Gandaki University"
wifi_password = "GU#@2076"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)  # qrcode.image.pil.PilImage
img.save("librarywifi.png")