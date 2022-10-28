from PIL import Image, ImageOps
from matplotlib import pyplot as plt
import numpy as np
from numpy.fft import fft2, ifft2, ifftshift, fftshift
import time

# get the start time
st = time.time()

im = Image.open('vid4-8.tif')
#plt.imshow(im)
#plt.show()

org_img = np.array(im)

#zero pad image
#one fundamental apsect is that the function I want to transform has to decay to zero..
#and sqaured the image to make it smaller but
# also for the fft algorithm it is faster to have 2^x pixels and sqaured pictures
org_img = org_img[14:-14,104:-104]
pad_img = np.pad(org_img[10:-10,10:-10], ((10,10), (10,10)))

#plt.imshow(pad_img, cmap='gray')
#plt.show()

#fourier transform and shift so that the most important frequencies are in the center
D = ifftshift(fft2(fftshift(org_img)))

# take most important frequency
limit = 255
pad_D = np.pad(D[limit:-limit,limit:-limit], ((limit,limit), (limit,limit)))

#inverse frourier transform back to image space
inv_D = fftshift(ifft2(ifftshift(pad_D)))
#plt.imshow(inv_D.real, cmap='gray')
#plt.show()

#then i just to the sum of the rows and collums
#but maybe this can be done better
#maybe you can put this inv_D image into you labview program and see if that works faster...
row = sum(inv_D.real)
collums =sum(inv_D.transpose().real)

minposR = np.argmin(row)
minposC = np.argmin(collums)

plt.plot(np.arange(0,512), collums)
plt.show()


plt.imshow(org_img, cmap='gray')
plt.scatter(minposR, minposC, 50, c="y", marker="+")
plt.show()

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')


print('bkb')