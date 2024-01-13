import os
import secrets
from PIL import Image
from colorama import init
from flask import current_app
from wtforms.validators import ValidationError

ALLOWED_IMAGE_FORMATS = {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'webp', 'heic', 'heif', 'ico', 'raw', 'eps', 'pdf', 'psd', 'ai', 'indd', 'tif', 'xcf', 'jxr', 'jp2', 'wdp', 'hdp', 'jng', 'djvu', 'avif', 'jfif', 'exr', 'cr2', 'nef', 'arw', 'rw2', 'orf', 'dng', 'sr2', 'pef', 'dcr', 'erf', 'mrw', 'raf', 'mos', 'x3f', 'srf', '3fr', 'mef', 'pict', 'hdr', 'svgz', 'wmf', 'emf'}

def save_picture(location, image, image_quality=80, as_thumbnail=True):
    """Save a profile picture.

    Args:
        location : The static folder where the image will be saved (ex: static/{ folder name })
        image (FileStorage): The uploaded picture file.
        image_quality (int): The quality of the image (range: 0-100) (default: 80)
        as_thumbnail (bool): Reduces the quality of an image to 125x125 (default: True)

    Returns:
        str: The filename of the saved picture.
    """
    random_value = secrets.token_hex(8)
    new_file_name = random_value + '.webp'
    file_path = os.path.join(current_app.root_path, location, new_file_name)

    image_instance = Image.open(image)

    if as_thumbnail:
        output_size = (125, 125)
        image_instance.thumbnail(output_size)

    image_instance.save(file_path, 'webp', quality=image_quality)

    return new_file_name
