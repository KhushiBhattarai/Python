# Create a QR Code Generator That Sends an Email to a User
#Title: My First Email Using Python
#Body: Hello, this is my first email using Python

import qrcode

email_address = "khushibhattarai22@gmail.com"
subject = "My first email using python"
body = "Hello, this is my first email using python"

mail = f"mailto:{email_address}?subject={subject}&body={body}"
img = qrcode.make(mail)
type(img)  # qrcode.image.pil.PilImage
img.save("mail.png")