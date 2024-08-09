from PIL import Image

def extract_image(path):
    image = Image.open(path)
    return image
