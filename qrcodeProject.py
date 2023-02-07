import qrcode
from PIL import Image

code = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 4,)

code.add_data("https://github.com/AdityaSanyal1996")
code.make(fit = True)

img = code.make_image(fill_color = "purple", back_color = "white")
img.save("Github_Profile.png") 