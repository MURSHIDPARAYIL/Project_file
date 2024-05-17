import cv2
import pytesseract
import urllib.request
from PIL import Image


urllib.request.urlretrieve(
    'https://wallup.net/wp-content/uploads/2018/09/30/346172-minimalistic-text-typography-black-background-748x421.jpg',"gfg.png")

img = Image.open("gfg.png")
#img.show()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img_text = pytesseract.image_to_string(Image.open("gfg.png"))

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)

# Displaying the extracted text
print(text[:-1])
