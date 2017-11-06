Exercise 1:

A cv::Mat object follows the conventional "row-major" matrix indexing. For instance,
mat.at(i,j) refers to row i and column j of the mat object.

Exercise 2:

1.)
	- only the "original image" frame actually contains color.
	- Red, Green, and Blue maintain good resolution of the original image.
	- For the R/G/B images, the closer to white a portion of the image is,
	the intensity of that color is present in the original image. The closer
	to black a portion of the image is, the less present that color is in the
	original image.
	- For Y/Cb/Cr, only the yellow frame has decent resolution of the original image.
	- 
	- see ColorImage.py
	
2.)
	- RGB Pixel 	@ [20,25]	= [102 165 156] ; Range = [102,165]
	- YCRCB Pixel 	@ [20,25] 	= [155 129  98] ; Range = [ 98,155]
	- HSV Pixel 	@ [20,25] 	= [ 34  97 165] ; Range = [ 34,165]
	
Exercise 3:

	- Lenna.png image was used during my analysis of the various image outputs
	-! Gaussian Noise Observations !-
		- Given kernel values has had no discernable effect on the image, regardless of the other parameters.
		- As sigma increases, the image inherits a more 'blue'ish hue.
		- Given mean values has had no discernable effect on the iamge, regardless of the other parameters.
		
	-! Salt and Pepper Noise Observations !-
		- Given kernel values has had no discernable effect on the image, regardless of the other parameters.
		- As pa increases, the density of black pixels on the image increases.
		- As pb increases, the density of white pixels on the image increases.