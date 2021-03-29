from PIL import Image
import numpy
import math

def block(array, blockSize):
  num_blocks = (math.floor(array.shape[0] / blockSize)) * (math.floor(array.shape[1] / blockSize))
  block = numpy.zeros((num_blocks,blockSize,blockSize,3), numpy.uint8)
  block_num = 0
  for blockWidth in range(math.floor(array.shape[0] / blockSize)):
    for blockHeight in range(math.floor(array.shape[1] / blockSize)):
      block[block_num] = array[blockSize*blockWidth:blockSize*(blockWidth+1),blockSize*blockHeight:blockSize*(blockHeight+1)]
      block_num += 1
  return block
    
def downsize(array):
  smallarray = numpy.zeros((math.floor(array.shape[0] / 4), math.floor(array.shape[1] / 4),3), dtype = numpy.uint8)
  for row in range(smallarray.shape[0]):
    for col in range(smallarray[row].shape[0]):
      first = math.floor(numpy.sum(array[4*row:4*row+4,4*col:4*col+4,0]) / 16)
      second = math.floor(numpy.sum(array[4*row:4*row+4,4*col:4*col+4,1]) / 16)
      third = math.floor(numpy.sum(array[4*row:4*row+4,4*col:4*col+4,2]) / 16)
      smallarray[row][col] = numpy.array([first,second,third])
  return smallarray

def main():
  Image.warnings.simplefilter('error', Image.DecompressionBombWarning)
  originalImage = Image.open('autumn.tif')
  originalArray = numpy.array(originalImage)
  smallArray = downsize(originalArray)
  smallImage = Image.fromarray(smallArray)
#  smallImage.show()
#  originalImage.show()
  blockSize = 20
  
  smallBlocks = block(smallArray, round(blockSize/4))
  originalBlocks = block(originalArray, blockSize)
  print(smallBlocks.shape, originalBlocks.shape)

main()