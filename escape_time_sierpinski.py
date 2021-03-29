import numpy as np
import imageio
import math
  
def main():
    pixels_width = 900
    pixels_height = 900
    
    # set my frame and set it to white
    fixed_point = np.zeros((pixels_width, pixels_height,3))
    
    for i in range(pixels_width):
      for j in range(pixels_height):
        x=float(i)/pixels_width
        y=float(-j)/pixels_height + 1
        for k in range(100):
          if(x < 0.5 and y <= 0.5):
            Newx = 2*x
            Newy = 2*y
          if(x > 0.5 and y <= 0.5):
            Newx= 2*x-1
            Newy= 2*y
          if(y > 0.5):
            Newx= 2*x
            Newy= 2*y-1

          x=Newx
          y=Newy
          if(x*x + y*y > 100000):
            if(k > 15):
              fixed_point[i][j]= np.array([2*k + 20,20,2*k + 20])
            else:
              fixed_point[i][j]= np.array([0,2*k + 20,2*k + 20])
              
            break

    imageio.imwrite('escape_time_sierpinski.png', fixed_point)
    return

main()