try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.tesseract_cmd = r'/Users/k4cp3rskiii/.conda/envs/Paski_TVP/lib/python3.9/site-packages'


print(pytesseract.get_languages(config=''))

print(pytesseract.image_to_string('images.txt', lang='pol'))



