import qrcode
import segno
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_instagram_qr(data, username, save_path="instagram_qr.png"):
    # Create QR with high error correction
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create QR with Instagram gradient colors
    qr_img = qr.make_image(fill_color="#E1306C", back_color="white")
    
    # Convert to RGBA for transparency support
    qr_img = qr_img.convert("RGBA")
    
    # Create background with Instagram gradient
    width, height = qr_img.size
    background = Image.new('RGBA', (width + 100, height + 150), 'white')
    
    # Create gradient background
    for y in range(height + 150):
        ratio = y / (height + 150)
        r = int(251 * (1 - ratio) + 192 * ratio)  # Orange to Pink
        g = int(173 * (1 - ratio) + 53 * ratio)
        b = int(80 * (1 - ratio) + 132 * ratio)
        
        draw = ImageDraw.Draw(background)
        draw.line([(0, y), (width + 100, y)], fill=(r, g, b, 255))
    
    # Paste QR code on gradient background
    qr_pos = (50, 50)
    background.paste(qr_img, qr_pos, qr_img)
    
    # Add username text
    draw = ImageDraw.Draw(background)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    text_bbox = draw.textbbox((0, 0), username, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_pos = ((width + 100 - text_width) // 2, height + 70)
    
    draw.text(text_pos, username, fill="white", font=font)
    
    # Save the final image
    background.save(save_path, format='PNG')
    return background

# Create Instagram-style QR code
instagram_qr = create_instagram_qr(
    "https://www.instagram.com/_avinash_2k03/", 
    "Avinash Rathod"
)
