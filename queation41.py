#pyhton program to find the size (resolution ) of a image
import PIL
from PIL import Image
img=PIL.Image.open("C:/Users/ashis/OneDrive/Desktop/images/Screenshot 2026-02-22 165738")
width,height=img.size
print(width,"x",height)

# one another method
from PIL import Image

img = Image.open(r"C:\Users\ashis\OneDrive\Desktop\images\Screenshot 2026-02-22 165738.png")
width, height = img.size

print(width, "x", height)