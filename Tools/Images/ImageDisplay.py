from PIL import Image


def display_image(image_path):
    display_img = Image.open(image_path)
    display_img.show()
