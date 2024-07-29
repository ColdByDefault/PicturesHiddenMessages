import stepic
from PIL import Image

# Load the encoded image
encoded_image = 'encoded_image.png'
img = Image.open(encoded_image)

# Decode the password from the image
decoded_password = stepic.decode(img)
print("Decoded password:", decoded_password)
