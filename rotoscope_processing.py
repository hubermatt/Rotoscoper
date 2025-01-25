# This script will automatically draw rotoscope frames from a 
# folder of PNG images. It depends on having consistently-named frames.
# Luckily, screenshots taken on a computer often have sequential names
# such as 'Screenshot-57' and so on. If this were the name of your starting 
# frame, you would want to change the string on line 33 to be 
# Image.open(f"Screenshot-{pic_number}.png") and change the starting_frame_number 
# variable to be 57. This will allow the script to automatically iterate through 
# each of your frames to edit them.
#
# The r, g, and b values within the loop represent the Red, Green, and Blue
# intensity of each pixel. Edit the code to determine how to manipulate the
# pixels. The fourth value 'a' represents the alpha, or opacity, of a pixel.
# To set a pixel as transparent, set the 'a' value to 0.
#
# The resulting PNG images will be saved within the same folder as your 
# existing images. Note that this script requires the pillow python extension.
# If you don't already have it, get it instantly by typing the following into
# your VSCode terminal: 'python -m pip install pillow.' Also, make sure that 
# your working directory (shown in the terminal) is within the folder that 
# you want to pull your images from.
#
# This original script was created by Matthew Huber on 09/25/24.

from PIL import Image

starting_frame_number = 197                                                    # Screenshot number to start at (these numbers get attached to photo names)
final_frame_number = 198                                                     # Screenshot number to end at
downscale_factor = 1                                                           # Set this to 1 if you do not want to rescale your image


total_frame_count = final_frame_number - starting_frame_number                # This is the total amount of frames you are converting.

for x in range(starting_frame_number, final_frame_number):
    current_image = Image.open(f"Screenshot ({starting_frame_number}).png")             # Change the name according to the Screenshot names
    current_image = current_image.convert("RGBA")

    width = current_image.width
    height = current_image.height

    current_image = current_image.resize((int(width/downscale_factor), int(height/downscale_factor)))      # Un-comment this if you want to resize your image before conversion.

    image_pixels = current_image.load()

    for y in range(0, int(height/downscale_factor)):
        for x in range(0, int(width/downscale_factor)):
            (r, g, b, a) = image_pixels[x, y]

            image_pixels[x, y] = (r, g, b, a)

            #if (r > 200 ):                                                     # Adjust your thresholds and values accordingly to cut out the right colors
            #    image_pixels[x, y] = (255, 255, 255, 100)
            if (r > 69):
                image_pixels[x, y] = (50, 120, 140, 255)
            elif (b < 25):
                image_pixels[x, y] = (200, 80, 80, 255)
            else:
                image_pixels[x, y] = (0, 0, 0, 0)


    current_image.show()                                                     # Un-comment this if you want to open each image as it is processed.
    current_image.save(f'newpic{starting_frame_number}.png')
    starting_frame_number +=1