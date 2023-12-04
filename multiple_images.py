import image
from PIL import Image
#Work with my older brother on this lab
def main():
    # A list of face images that are available
    # Face images of men
    # face_files = ["alex.jpg", "alexander.jpg", "alfred.jpg", "ambroz.jpg"]
    # Face images of women
    face_files = ["zelmira.jpg","zita.jpg", "zlata.jpg", "zlatica.jpg", "zora.jpg"]
    base_url = "http://raw.githubusercontent.com/cs-133-01-22fa/faces/main/"

    # Load a list of pics
    face_pics = []
    for face_path in face_files:
        face_pics.append(image.Pic(base_url + face_path))

    print("Calculating average image...")
    average_pic = average_faces(face_pics)
    print("Done calculating average image")
    print("-------------------")
    # Save the averaged image
    average_pic.save("average_face.jpg")

def average_faces(face_pics):
    if not face_pics:
        raise ValueError("No face images provided")

    width, height = face_pics[0].get_width(), face_pics[0].get_height()
    
    # Correctly using Image.new from PIL
    avg_image = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            avg_r, avg_g, avg_b = 0, 0, 0
            for pic in face_pics:
                pixel = pic.get_pixel(y, x)
                avg_r += pixel.red
                avg_g += pixel.green
                avg_b += pixel.blue
            avg_r //= len(face_pics)
            avg_g //= len(face_pics)
            avg_b //= len(face_pics)
            avg_image.putpixel((x, y), (avg_r, avg_g, avg_b))

    return avg_image

if __name__ == '__main__':
    main()
