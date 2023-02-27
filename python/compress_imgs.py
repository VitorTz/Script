from PIL import Image
import os
import sys

def compress_images(folder_path):
    # loop through all files in the given folder path
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
            # open the image file
            img = Image.open(os.path.join(folder_path, file_name))

            # remove the original image file
            os.remove(os.path.join(folder_path, file_name))

            # save the image as PNG with compression level 9 (highest compression)
            img.save(os.path.join(folder_path, f"{os.path.splitext(file_name)[0]}.png"), "PNG", optimize=True, quality=70)

            

if __name__ == "__main__":
    folder = sys.argv[1]
    compress_images(folder)