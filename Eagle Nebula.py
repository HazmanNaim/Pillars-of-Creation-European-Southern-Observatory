
import matplotlib.pyplot as mpl
from matplotlib.colors import LogNorm 
from astropy.io import fits

#Read FITS file
M16_673nm = fits.open('673nmos.fits')  


print("-------------------------------")
#All FITS information from fits file
M16_673nm.info()

#Storing the 673nm data band data as 2D numpy array
imagedata673nm= M16_673nm[0].data
imagedata673nm = imagedata673nm.transpose()     #The reason why I transpose the array is because I rotate the image by 90 degree clockwise

#This is to know the shape of the array (image is the array itself)
#For 673nm bandpass data
print("-------------------------------")
print("502nm band data")
print(type(imagedata673nm))
print(imagedata673nm)
print(imagedata673nm)
print("-------------------------------")

#Showing Image
#673nm data
mpl.imshow(imagedata673nm, cmap='gray')
mpl.title('Image of M16 with 673nm data Bandpass Filter', fontsize=10)
mpl.colorbar()
mpl.show()

#Histogram
#673nm data
histogram = mpl.hist(imagedata673nm.flat, bins=500)
mpl.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False) #Turn off Scientific Notation
mpl.xlim(0,100) #Set Range
mpl.ylim(0,5000000)
mpl.title('Intensity of each pixel (673nm data band)')
mpl.show()

#Logarithm Scaling
mpl.imshow(imagedata673nm, norm = LogNorm())
mpl.colorbar()
mpl.title('"Pillars of Creation" in the Eagle Nebula \n with 673nm Bandpass Filter \n (Logarithmic Stretch)', fontsize=9)
mpl.show()

#Black and White image
mpl.imshow(imagedata673nm, cmap='gray', norm = LogNorm())
mpl.colorbar()
mpl.title('"Pillars of Creation" in the Eagle Nebula \n with 673nm Bandpass Filter \n (Logarithmic Stretch + Black and White)', fontsize=9)
mpl.show()

