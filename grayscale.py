import os, sys 
from PIL import Image, ImageFilter

def average(pic):
  width, height = pic.size
  px = pic.load()
  a = 0
  for x in range(width):
    for y in range(height):
      a += sum(px[x,y])
  a /= width * height
  return a

def grayScale(pic, threshold):

  #get image size
  width, height = pic.size

  px = pic.load()
  #loop through every pixel
  for x in range(width):
    for y in range(height):
      #change pixel based on given parameters
      #r, g, b = px[x, y]
      s = sum(px[x,y])
      if s > threshold:
        px[x,y] = (255,255,255)
      else:
        px[x,y] = (0,0,0)
  #print finished image
  pic.show()

def originalPic(pic):
  pic.show()

def grayScale1(pic):
  grayScale(pic, 255*3/2)

def grayScale2(pic):
  threshold = average(pic)
  grayScale(pic, threshold)

def grayScale3(pic):
  threshold = (average(pic) + 255*3/2) / 2
  grayScale(pic, threshold)

def contrast(pic):
  #get image size
  width, height = pic.size

  px = pic.load()
  #loop through every pixel
  for x in range(width):
    for y in range(height):
      #change pixel based on given parameters
      r, g, b = px[x, y]
      s = sum(px[x,y])
      if s > 255*3/2:
        px[x,y] = ((r + 255)//2, (g + 255)//2, (b + 255)//2)
      else:
        px[x,y] = ((r + 0)//2, (g + 0)//2, (b + 0)//2)
  #print finished image
  pic.show()
  
  

if __name__ == "__main__":
  picSource = "./images/human.jpg"
  pic = Image.open(picSource)

  filters = [
    originalPic,
    grayScale1,
    grayScale2,
    grayScale3,
    contrast
  ]

  for filter in filters:
    filter(pic.copy())