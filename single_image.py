import image

def main():
  # Load an image from somewhere online
  pic = image.Pic('http://www.sbu.edu/images/default-source/alumni/show-your-spirit-zoom-backgrounds/campus-in-summer.jpg')
  # Modify our image
  print("Modifying image... ")
  boost_red(pic)
  print("Done modifying image")
  print("-------------------")
  # Save the image
  pic.save_image("myImage-red.jpg")


# BOOST THE RED - DON'T DELETE
# This is ONE example of a function that changes a picture.
# You will create several other functions that look similar to this.
def boost_red(pic):
  # Go through each row and column
  for row in range(pic.height):
    for col in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Resave them by altering the red
      pixel.red = red + 100
      pixel.green = green
      pixel.blue = blue

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel


main()
