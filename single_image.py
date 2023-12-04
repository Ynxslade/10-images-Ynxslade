import image
import random
#Worked with my older brother on this lab
# Function to boost the red component of each pixel
def boost_red(pic):
    for row in range(pic.height):
        for col in range(pic.width):
            pixel = pic.pixels[row][col]
            pixel.red = min(255, pixel.red + 100)  # Increase red but cap at 255
            pic.pixels[row][col] = pixel

# Function to invert the colors of the image
def invert(pic):
    for row in range(pic.height):
        for col in range(pic.width):
            pixel = pic.pixels[row][col]
            pixel.red = 255 - pixel.red
            pixel.green = 255 - pixel.green
            pixel.blue = 255 - pixel.blue
            pic.pixels[row][col] = pixel

# Function to convert the image to grayscale
def grayscale(pic):
    for row in range(pic.height):
        for col in range(pic.width):
            pixel = pic.pixels[row][col]
            gray = (pixel.red + pixel.green + pixel.blue) // 3
            pixel.red = pixel.green = pixel.blue = gray
            pic.pixels[row][col] = pixel

# Function to apply a grainy effect to the image
def grainy(pic):
    for row in range(pic.height):
        for col in range(pic.width):
            pixel = pic.pixels[row][col]
            color_boost = random.choice(['red', 'green', 'blue'])
            if color_boost == 'red':
                pixel.red = min(255, pixel.red + 100)
            elif color_boost == 'green':
                pixel.green = min(255, pixel.green + 100)
            else:
                pixel.blue = min(255, pixel.blue + 100)
            pic.pixels[row][col] = pixel

# Function to selectively invert colors within a specified rectangle
def selective_invert(pic, row1, col1, row2, col2):
    for row in range(row1, row2):
        for col in range(col1, col2):
            pixel = pic.pixels[row][col]
            pixel.red = 255 - pixel.red
            pixel.green = 255 - pixel.green
            pixel.blue = 255 - pixel.blue
            pic.pixels[row][col] = pixel

# Function to create a mirrored image effect
def mirror_image(pic):
    width, height = pic.width, pic.height
    for row in range(height):
        for col in range(width // 2):
            pixel = pic.pixels[row][col]
            pic.pixels[row][width - col - 1] = pixel

# Function to apply a blur effect
def blur(pic, window):
    for row in range(pic.height):
        for col in range(pic.width - window + 1):
            avg_red = avg_green = avg_blue = 0
            for w in range(window):
                pixel = pic.pixels[row][col + w]
                avg_red += pixel.red
                avg_green += pixel.green
                avg_blue += pixel.blue
            avg_red //= window
            avg_green //= window
            avg_blue //= window
            pic.pixels[row][col].red = avg_red
            pic.pixels[row][col].green = avg_green
            pic.pixels[row][col].blue = avg_blue

# Main function to run the image manipulations
def main():
    # Load an image
    pic = image.Pic('http://www.sbu.edu/images/default-source/alumni/show-your-spirit-zoom-backgrounds/campus-in-summer.jpg')

    # Apply different manipulations
    boost_red(pic)
    grayscale(pic)
    invert(pic)
    grainy(pic)
    selective_invert(pic, 10, 10, 50, 50)  # Example coordinates
    mirror_image(pic)
    blur(pic, 5)  # Example window size for blur

    # Save the modified image
    pic.save_image("myImage-modified.jpg")

if __name__ == '__main__':
    main()