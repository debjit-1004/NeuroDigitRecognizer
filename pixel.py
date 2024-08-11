from PIL import Image

# Open an image file
image_path = 'drawing_grayscale.png'
img = Image.open(image_path)


data=list(img.getdata())


for i in range(len(data)):
   data[i]=255-data[i]
print(data)
