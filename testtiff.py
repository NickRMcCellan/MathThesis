from PIL import Image
import numpy

Image.warnings.simplefilter('error', Image.DecompressionBombWarning)

im = Image.open('autumn.tif')
im.show()

imarray = numpy.array(im)

print(imarray.shape)
print(im.size)

Image.fromarray(imarray)