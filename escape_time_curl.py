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
        x=float(4*i)/pixels_width - 2
        y=float(-4*j)/pixels_height + 2
        for k in range(100):
          if(x < 0 and y <= 0):
            Newx = 2*x + 1
            Newy = 2*y + 1
          if(y>0):
            Newx=2*y-1
            Newy=-2*x+1
          if(x>=0 and y<=0):
            Newx=2*x-1
            Newy=2*y+1

          x=Newx
          y=Newy
          if(x*x + y*y > 100000):
            fixed_point[i][j]= np.array([0,0,k])
            break

    imageio.imwrite('escape_time_curl.png', fixed_point)
    return

main()