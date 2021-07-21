# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:41:41 2021

@author: abc
"""

"""

what is gaussian(denoising) filter ?

"""

import cv2
import numpy as np
from skimage import io, img_as_float
from skimage.filters import gaussian

#read our image and convert it into floating point value
img_gaussian_noise = img_as_float(io.imread("BSE_25sigma_noisy.jpg", as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread("BSE_salt_pepper.jpg", as_gray=True))

#activate gaussian image
img = img_gaussian_noise

#define gaussian kernel
gaussian_kernel = np.array([[1/16, 1/8, 1/16],
                            [1/8, 1/4, 1/8],
                            [1/16, 1/8, 1/16]])

#define convoution filter
conv_using_cv2 = cv2.filter2D(img, -1, gaussian_kernel, borderType=cv2.BORDER_CONSTANT)

#SHOW OUR IMAGE
cv2.imshow("Original image", img)
cv2.imshow("cv2 filter", conv_using_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#########################################################################################

#EASY WAY FOR DOING ABOVE 

import cv2
import numpy as np
from skimage import io, img_as_float
from skimage.filters  import gaussian

#read images and convert it into floating point value
img_gaussian_noise = img_as_float(io.imread("BSE_25sigma_noisy.jpg", as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread("BSE_salt_pepper.jpg", as_gray=True))

#activate gaussian image
img = img_gaussian_noise

#define gaussian using opencv
gaussian_using_cv2 = cv2.GaussianBlur(img, (3,3), 0, borderType=cv2.BORDER_CONSTANT)
#here in opencv we use kernel size like(3,3)

#show our image
cv2.imshow("Original image", img)
cv2.imshow("cv2 filter", gaussian_using_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#######################################################################################

#Another way of doing it is using skimage

import cv2
import numpy as np
from skimage import io, img_as_float
from skimage.filters import gaussian

#read our image and convert it into floating point value
img_gaussian_noisy = img_as_float(io.imread("BSE_25sigma_noisy.jpg", as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread("BSE_salt_pepper.jpg", as_gray=True))

#activate gaussian image
img = img_gaussian_noise

#define gaussian filter using skimage
gaussian_using_skimage = gaussian(img, sigma=1, mode="constant", cval=0.0)

#show our image
cv2.imshow("original image", img)
cv2.imshow("skimage filter", gaussian_using_skimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

##############################################

#let's see result of salt pepper noise image

import cv2
import numpy as np
from skimage import io, img_as_float
from skimage.filters import gaussian

#read our image and convert it into floating point value
img_gaussian_noisy = img_as_float(io.imread("BSE_25sigma_noisy.jpg", as_gray=True))
img_salt_pepper_noise = img_as_float(io.imread("BSE_salt_pepper.jpg", as_gray=True))

#activate gaussian image
img = img_salt_pepper_noise

#define gaussian filter using skimage
gaussian_using_skimage = gaussian(img, sigma=1, mode="constant", cval=0.0)

#show our image
cv2.imshow("original image", img)
cv2.imshow("skimage filter", gaussian_using_skimage)
cv2.waitKey(0)
cv2.destroyAllWindows()




