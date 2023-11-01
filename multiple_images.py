import image

def main():
  # A list of face images that are available
  # Face images of men
  face_files = ["alex.jpg", "alexander.jpg", "alfred.jpg", "ambroz.jpg"]
  # Face images of women
  #face_files = ["zelmira.jpg","zita.jpg", "zlata.jpg", "zlatica.jpg", "zora.jpg"]
  base_url = "http://raw.githubusercontent.com/cs-133-01-22fa/faces/main/"

  # Load a list of pics
  face_pics = []
  for face_path in face_files:
    face_pics.append(image.Pic(base_url + face_path))

  print("Modifying images... ")
  average_pics(face_pics)
  # Save the image
  face_pics[0].save_image("average.jpg")
  print("Done modifying images")
  print("-------------------")

def average_pics(faces):
  '''
  Takes a list of face images and modifies the first
  image in the list to be the average of the entire list.
  '''
  # We want to modify the first face, so save it in a variable
  first_face = faces[0]

  # The pics all have the same dimensions, so we'll just use the first
  for row in range(first_face.height):
    for col in range(first_face.width):

      # Get the average RGB value at row/col for all our pics
      # We'll need go through each face pic in faces to do this
      # After we get the RGB average, apply it to row/col in first_face

      # TIP: This looks similar to blur
      pass # delete this line when you write your code


main()
