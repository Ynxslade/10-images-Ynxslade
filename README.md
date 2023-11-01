# Images Lab

## Overview

### Code
Develop code (in ```single_image.py```) to manipulate the SBU campus image, and in ```multiple_images.py``` to average multiple images of faces.

### Document
Remember to comment your code.

### Submit
* Stage your code as well as all of your images.
* Commit to the GitHub repository for grading.

### Credits
This lab was originally developed by [Evan M. Peck](http://www.eg.bucknell.edu/~emp017/) and is available in its original form here: [https://ethicalcs.github.io/#manipulators](https://ethicalcs.github.io/#manipulators).

## Detailed Instructions
This lab begins with media manipulation (changing RGB values in pixels), and then transitions to generate the "average" of facial images. In this lab, you will practice:
* Nested loops
* 2D arrays
* Image manipulation
* External libraries

Sophisticated algorithms have made big news recently in the ways they can mirror and fake reality (these [fake images](https://www.vox.com/future-perfect/2019/5/31/18645993/ai-deepfakes-gan-explained-machine-learning) tell a scary story of how far AI has come). While we won’t go that far, in this lab we will begin to see how easy it is to modify and change the digital world we see everyday.

### Test & understand provided code

We’ll start with a basic change to an image using the provided code in ```single_image.py``` and ```image.py```. Make sure it runs correctly. You should see the file ```myImage-red.jpg``` in your directory. The image should look like the image below, but with a red tint.

<img src="assignment_images/campus-in-summer.jpg" width="400"> <br />

As you look through the code, please refer to the ```Pic API``` document to help understand how to use the image library provided for you.

#### What main() does
* Loads an image from a website. Right now, it’s an image from the SBU website.
* Sends that image to a function (```boost_red```), which changes it.
* Saves the modified image

#### How boost_red(pic) works (and how you should write your filters)
* ```boost_red(pic)``` cycles through each possible pixel-coordinate on the image
  * each row of the image
  * each column of the image
  ```
  for row in range(pic.height):
      for col in range(pic.width):
  ```
* ```boost_red``` loads a single pixel at that particular row and column
  ```
  pixel = pic.pixels[row][col]
  ```
  * Then, we access the red, green, and blue values of the pixel with:
   ```
   red = pixel.red
   green = pixel.green
   blue = pixel.blue
   ```
  * Then, we change the pixel’s existing RGB with our new values we want.
   ```
   pixel.red = red + 100
   pixel.green = green
   pixel.blue = blue
   ```
  * Finally, ```boost_red``` resaves our modified pixel back at its location
   ```
   pic.pixels[row][col] = pixel
   ```

### Part 1: Pixel Manipulation
Now it’s time to write your own code to manipulate the image:
* You’ll be creating additional functions (that look very similar at first!) to ```boost_red```.
* Start by copy/pasting your ```boost_red(pic)``` function and then changing the name and modifying it (don’t delete ```boost_red(pic)```).
* Read the descriptions and implement code for the functions invert, greyscale, and grainy.
* Don’t forget to add calls to your new functions in ```main()``` after constructed.

#### invert(pic)
For each pixel, subtract all three color values of an individual pixel *from* 255. For example, a pixel's red value should be set to whatever ```255 - red``` results in.

Below is an example before and after image. In the image, blues (for example) were converted to yellows/reds.

<img src="assignment_images/inverted.jpg" width="400">

#### greyscale(pic)
For each pixel, average the three RGB values and apply that average to red, blue, and green (so they should all be the same value). Note that the average of the three RGB values must be converted to an integer before applying.

Below is an example before and after image. All colors should become a shade of grey.

<img src="assignment_images/greyscale.jpg" width="500">

#### grainy(pic)
This is similar to the ```boost_red()``` function, but for each pixel, you randomly choose whether to boost red, green, or blue by 100.

Below is an example before and after image.

<img src="assignment_images/grainy.jpg" width="400">

### Part 2: Selective Filters

Now we’ll modify ***one*** of our filters so that we can specify which portion of the image should be  modified. We’ll allow people to specify a rectangle within the image that your filter  will modify.
* ```row1``` and ```col1``` : the top left coordinates the rectangle to modify
* ```row2``` and ```col2```: the bottom right coordinates of the rectangle to modify

Create a new copy of ***one*** of the functions you completed above. Add 4 more parameters. For example, invert would be:

```
def invertspot(pic, row1, col1, row2, col2):
```

For example, the image below was created by that function using the following inputs:

```
invertspot(pic, 20, 210, 250, 370)
```

<img src="assignment_images/invertspot.jpg" width="200">

### Part 3: Coordinate Manipulation
So far, we have only manipulated pixels in-place. That means that we load a pixel at coordinates x/y, modify it, and then save it at pixel x/y. For this problem, you should be creating a mirrored image like the one below (before is on top, after is on the bottom).

<img src="assignment_images/mirror.jpg" width="500"> <br />

In order to do this, take each pixel on the right half of the screen, and then put the same RGB values on the mirrored x-position on the left side of the screen. Here are some tips to help you solve this problem:
* You will have to change the range value on your for loop for this one.
* The x/y coordinates of the pixel you change are not the same as the pixel you load. Draw a picture! Think through a couple of concrete cases.
  * For example, if you had a picture that was 200 pixels wide and 100 pixels tall,
think about what coordinates you’d want your for loops to go through
  * What are the minimum and maximum x and y values?
  * If you had a point at col = 75, row = 90, where would you want to mirror that to?

### Part 4: Contextual Manipulation
Sometimes, it’s important to modify the value of a pixel not only based on its own values, but based on its context - the values of the pixels around it. We’ll explore this by creating a kind of blur effect on our images.

There are several ways to create a blurring effect. We’ll use the following...

```
def blur(pic, window):
```

For example, if the window is 4:
* If the current pixel has red = 10, and the next 5 pixels have red values of 20, 30, 40, 50, 60:   
  * Then our new red is the average of the current pixel’s red (10) + the red values of the next 3 pixels (20 + 30 + 40) resulting in code like ```new_red = (10 + 20 + 30 + 40) / 4```
* Do the same computation for green and blue values
* For simplicity, don’t worry about blurring pixels on the extreme right side of the image, starting at the pixel column of ```width - window + 1```

Running a blur with a window of 8, should look roughly like the image below:

<img src="assignment_images/blur.jpg" width="500">

### Part 5: RGB Across Multiple Images
While looking at one image is interesting, looking at many images can reveal fascinating patterns about the places and people. One way we can get a visual sense of this is by looking at the average of images. Averaging faces can provide interesting insights into people or give us a peek into how face-recognition algorithms are likely to classify us.

<img src="assignment_images/averages.jpg" width="500"> <br />

The ```multiple_images.py``` program differs from your previous one by:
* loading more than one image into a list, and
* feeding a list of images to the ```average_pics``` function.

Your job is to finish the ```average_pics``` function. It should average the RGB values of each image at a given coordinate, and then save the averaged values in the first image

For example, suppose we have 3 pictures and we are looking at the upper-left corner:
* Pic 1 at col = 0, row = 0: (Red:0, Green:100, Blue:250)
* Pic 2 at col = 0, row = 0: (Red:30, Green:50, Blue:250)
* Pic 3 at col = 0, row = 0: (Red:0, Green:150, Blue:100)

We would change Pic 1 at col = 0, row = 0 to Red:10, Green:100, Blue:200.

*Hint*: The structure will end up looking very similar to your blur function.

Once you’ve successfully finished averaged the faces of men in the files listed (all files starting with 'a'), change the set of faces that you average to the faces of women (all files starting with 'z'). Reflect on the following questions:
* Do the two sets look significantly different from the other?
* Are there faces that seem particularly important to the final visual output?
