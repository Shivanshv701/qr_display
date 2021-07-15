# qr_display

The program displays the QR code of the enterred URL,
When the program is executed, it prompts the user to input the URL,
When URL is enterred, it executes the create() of pyqrcode module to create the QR code of that URL and save it in a variable named url
Then url.png() is executed to save the image as myqr.png in the current working directory.

The image of the QR is displayed using matplotlib.pyplot and matplotlib.image
