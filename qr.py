import pyqrcode
import matplotlib.pyplot as plt
import matplotlib.image as img

# String which represents the QR code
s = input("Enter the url:")

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale=6)

#Displaying the QR code

plt.imshow(img.imread('myqr.png'))
plt.show()
