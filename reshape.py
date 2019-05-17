import sys
import os.path
from PIL import Image

# obtained from folder average
reshape_size = (700, 450)

# original images
orgfolder = "DEEPstruc"

# destination folder for resized images
subfolder = "DEEPstruc_Normalized/"

# for image in original folder:
for path in os.listdir(orgfolder):
    try:
        image = Image.open(orgfolder + "/" + path)
    except IOError as e:
        # Report error, and then skip to the next argument
        print ("Problem opening", path, ":", e)
        continue

    # Resize the image
    image = image.resize(reshape_size, Image.ANTIALIAS)
    
    # Split our original filename into name and extension
    (name, extension) = os.path.splitext(path)
    
    # Save the resized image as "(original_name)_normal.png"
    image.save(subfolder + name + '_normal.png')