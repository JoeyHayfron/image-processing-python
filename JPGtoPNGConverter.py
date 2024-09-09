import sys
import os
from PIL import Image


source_dir = sys.argv[1]
destination_dir = sys.argv[2]

try:
    source_images = os.listdir(source_dir)

    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir)

    if source_images:
        for image in source_images:
            with Image.open(os.path.join(source_dir, image)) as source_image:
                source_image.save(f"{destination_dir}{image.split('.')[0]}.png", 'png')
except (FileNotFoundError, IOError, TypeError, ValueError) as err:
    print(f"An error occurred {err}")
