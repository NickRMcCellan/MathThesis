import numpy as np
import imageio
import math
  
def main():
    pixels_width = 900
    pixels_height = 900
    
    # set my frame
    fixed_point = np.zeros((pixels_width, pixels_height,3))
    l = np.array([0,0])
    
    for i in range(pixels_width):
      for j in range(pixels_height):
        x=float(16*i)/pixels_width - 8
        y=float(-13*j)/pixels_height + 12
        for k in range(75):
            l[0]=0.857*x + 1.4114
            l[1]= -0.8462*x + 2.59
            if((x>0 and y>l[0]) or (x<=0 and y>l[1])):
                Newx=1.174*x-.0552*y+.0884 
                Newy=.0552*x+1.174*y-1.878
            if(x<0 and y<l[1]):
                Newx=2.119*x+2.505*y-4.01
                Newy=-2.216*x+1.927*y-3.083
            if(x>=0 and y<l[0]):
                Newx =-2.205*x+2.573*y-1.132
                Newy =2.389*x+1.378*y-.6066
            if((abs(x)<.01) and (abs(y)<.44)):
                Newx = x
                Newy = 6.25*y

            x=Newx;
            y=Newy;
            if(x*x+y*y>10000):
              fixed_point[i][j] = np.array([0,0,k])
              break

    imageio.imwrite('escape_time_fern.png', fixed_point)
    return

main()