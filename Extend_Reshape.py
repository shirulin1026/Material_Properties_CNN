import os
from PIL import Image
path = "DEEP" 
files= os.listdir(path)

for file in files:
    #if not os.path.isdir(file):
    pic = Image.open(path+'/'+file)
    longer_side=max(pic.size)
    horizontal_padding=(longer_side-pic.size[0])/2
    vertical_padding=(longer_side-pic.size[1])/2
    pic2=pic.crop(
    (
    -horizontal_padding,
    -vertical_padding,
    pic.size[0]+horizontal_padding,
    pic.size[1]+vertical_padding
    ))
    pic2 = pic2.resize((500,500),Image.ANTIALIAS)
    (name, extension)=os.path.splitext(file)
    pic2.save("NEWDEEP"+'/'+name+extension)
 
print('Transfer successfully')
