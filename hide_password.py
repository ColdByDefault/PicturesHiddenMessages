import stepic
from PIL import Image

# Load the image
input_image = '1.png' # Change the Path to your Picture
img = Image.open(input_image)

# The password to hide
password = 'Your Password'

# Encode the password into the image
encoded_img = stepic.encode(img, password.encode())

# Save the encoded image
encoded_img.save('encoded_image.png')
print("Password hidden in 1.png")
