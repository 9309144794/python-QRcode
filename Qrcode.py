"""simple QR code create"""

# import qrcode  as qr

# img= qr.make("Avinash")
# img.save("ak.png")



""" Advance QR code Create"""


import qrcode as qr
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from PIL import Image

qr= qr.QRCode(version=1,
              error_correction=qr.ERROR_CORRECT_H,
              box_size=10, border=4)

qr.add_data("Avinash Rathod")
qr.make(fit=True)
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255),       # Background white
        center_color=(131, 58, 180),      # Purple center
        edge_color=(253, 29, 29)          # Pink/Orange edges
    )
)
img.save("Avi.png")




