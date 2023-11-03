# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# def create_string(image_path):

#     text = pytesseract.image_to_string(image_path,lang='eng')

#     text = text.replace("\n",'')

#     return text


import pytesseract
import tempfile
import os

# Set the Tesseract executable path
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def create_string(image_bytes):
    # Create a temporary file to save the image data
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_image:
        temp_image.write(image_bytes)
        temp_image_path = temp_image.name

    try:
        # Use PyTesseract to extract text from the temporary image file
        text = pytesseract.image_to_string(temp_image_path, lang='eng')
        text = text.replace("\n", '')
    finally:
        # Clean up by deleting the temporary image file
        os.remove(temp_image_path)

    return text


