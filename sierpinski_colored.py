import numpy as np
import imageio

def w1(input_image):
  input_image = np.array([[0.5, 0],[0, 0.5]]) @ input_image
  return input_image

def w2(input_image):
  input_image = np.array([[0.5, 0],[0, 0.5]]) @ input_image
  input_image[1] += 0.5
  return input_image
  
def w3(input_image):
  input_image = np.array([[0.5, 0],[0, 0.5]]) @ input_image
  input_image[0] += 0.5
  return input_image
  
def main(n=100000):
    pixels_width = 900
    pixels_height = 900
    # set my frame and set it to white
    fixed_point = np.zeros((pixels_width, pixels_height))
    for i in range(pixels_width):
        fixed_point.fill(255)
    #input image doesn't matter so just random values here
    input_image = [1, 1]
    for i in range(n):
        which_transformation = np.random.randint(0, 3)
        # the randomly selected transformation
        color = 0
        if(which_transformation == 0):
          input_image = w1(input_image)
          color = 0
        elif(which_transformation == 1):
          input_image = w2(input_image)
          color = 170
        elif(which_transformation == 2):
          input_image = w3(input_image)
          color = 85
        #transform point to the canvas grid
        pix_coord = np.around((input_image[0:2]) * [pixels_width, pixels_height]).astype(int)
        # if the pixel is on the canvas
        if (pix_coord >= [0, 0]).all() and (pix_coord < [pixels_width, pixels_height]).all():
            #set the point to appropriate color
            fixed_point[pix_coord[0], pix_coord[1]] = color
    imageio.imwrite('sierpinski_colored.png', fixed_point)
    return

main()