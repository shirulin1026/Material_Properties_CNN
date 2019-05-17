import sys
import os.path
from PIL import Image

reshape_size = (700, 450)
orgfolder = "DEEPstruc"
subfolder = "DEEPstruc_Normalized/"

# Loop through all provided arguments
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
    
    # Save the thumbnail as "(original_name)_thumb.png"
    image.save(subfolder + name + '_normal.png')