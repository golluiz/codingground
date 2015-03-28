import numpy as np
import vigra as vg
import cv2 as ocv

def lognormal(invar):

	outvar = np.log(invar+1)
	outvar = outvar - outvar.min()
	outvar = outvar/outvar.max()	
	return outvar

def tonemap(image):
	# 	from http://uk.mathworks.com/company/newsletters/articles/rendering-high-dynamic-range-images-on-the-web.html
#	print image.max()
	print("%.5f" % image.min())
	imglog = lognormal(image)
#	print imglog.max()
#	print("%.5f" % imglog.min())
	imglab = vg.colors.transform_RGB2Lab(imglog)
#	print imglab.shape
	lum = imglab[:,:,1]
#	print 'Type of Lum ' + str(type(lum))
	#	from http://docs.opencv.org/trunk/doc/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html
	# create a CLAHE object (Arguments are optional).
	clahe = ocv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	lumclahe = ocv.CV_8UC1
#	print 'Type of Lumclahe ' + str(type(lumclahe))
	lumcl = clahe.apply(lum)
	#	from http://uk.mathworks.com/help/images/ref/imadjust.html
	#	from http://www.codeforge.com/read/168571/imadjust.cpp__html	
	imgtm = imglab
	return imgtm

def loadimage(imagefile):
	import os.path
	print ('In loadimage...' imagefile)
	if os.path.isfile(imagefile): 
		if vg.impex.isImage(imagefile):
			image = vg.readImage(imagefile)
			print ('Image dimensions: ' + str(image.shape))
			vg.imshow(image)
#			imgtm = tonemap(image)
			vg.imshow(imgtm)
		else:
			print ('File is not an image.')
			print ('Image formats accepted.' + vg.impex.listFormats())
	else:
		print ('File does not exist.')
	


