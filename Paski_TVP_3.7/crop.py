# Import packages
import cv2

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Cropping an image
def get_cropped(path):
    # print(path)
    img = cv2.imread(f'{path}')
    img = remove_noise(img)
    # img = thresholding(img)
    sizes = img.shape
    dl = sizes[1]
    hei = sizes[0]
    cropped_image = img[int(0.80*hei):int(0.89*hei), int(0.20*dl):dl]
    return cropped_image


