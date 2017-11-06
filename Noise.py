import cv2
import numpy as np
import sys

# Author Rishab Shah
# Adapted to Python by Nick VanDeusen

def Add_salt_pepper_Noise(srcArr, pa, pb):
	# shape[0] = # of rows
	# shape[1] = # of cols
	amount1 = srcArr.shape[0] * srcArr.shape[1] * pa # Need to run through all channels
	amount2 = srcArr.shape[0] * srcArr.shape[1] * pb
	
	counter = 0
	for counter in range(0, int(amount1)):
		srcArr[np.random.randint(0, srcArr.shape[0]), np.random.randint(0, srcArr.shape[1])] = 0

	for counter in range(0, int(amount2)):
		srcArr[np.random.randint(0, srcArr.shape[0]), np.random.randint(0, srcArr.shape[1])] = 255

def Add_gaussian_Noise(srcArr, mean, sigma):
    NoiseArr = srcArr.copy()
    cv2.randn(NoiseArr, mean, sigma)
    cv2.add(srcArr, NoiseArr, srcArr)

def main():
	# Original Image
	image = cv2.imread(sys.argv[1])
	#cv2.namedWindow("Original image", cv2.WINDOW_NORMAL)
	#cv2.imshow("Original image", image)
	
	meanVals = [0, 5, 10, 20]	
	sigmaVals = [0, 20, 50, 100]		# Not the variance
	kernelVals = [3, 5, 7]
	paVals = [0.01, 0.03, 0.05, 0.4]	# Controls the amount of black spots in the noise
	pbVals = [0.01, 0.03, 0.05, 0.4]	# Controls the amount of white spots in the noise
	dir = "Noise_Out/"
	for kernel in kernelVals:
		for mean in meanVals:
			for sigma in sigmaVals:
				##### Add Gaussian Noise #####
				noise_img = image.copy() 
				Add_gaussian_Noise(noise_img, mean, sigma)
				#cv2.imshow("Gaussian Noise", noise_img);
				cv2.imwrite(dir+"GaussNoise"+"_M"+str(mean)+"_S"+str(sigma)+".png",noise_img)
				# Box Filter
				noise_dst = noise_img.copy()
				cv2.blur(noise_dst, (kernel,kernel))
				#cv2.imshow("Box filter", noise_dst)
				cv2.imwrite(dir+"BoxFilter"+"_M"+str(mean)+"_S"+str(sigma)+"_K"+str(kernel)+".png",noise_dst)
				# Gaussian Filter
				noise_dst1 = noise_img.copy()
				cv2.GaussianBlur(noise_dst1, (kernel,kernel), 1.5)
				#cv2.imshow("Gaussian filter", noise_dst1)
				cv2.imwrite(dir+"GaussFilter"+"_M"+str(mean)+"_S"+str(sigma)+"_K"+str(kernel)+".png",noise_dst1)
				# Median Filter
				noise_dst2 = noise_img.copy()
				cv2.medianBlur(noise_dst2, kernel)
				#cv2.imshow("Median filter", noise_dst2)
				cv2.imwrite(dir+"MedianFilter"+"_M"+str(mean)+"_S"+str(sigma)+"_K"+str(kernel)+".png",noise_dst2)
				
		for pa in paVals:
			for pb in pbVals:
				##### Add salt-and-pepper noise #####
				noise_img2 = image.copy()
				Add_salt_pepper_Noise(noise_img2, pa, pb); 
				#cv2.imshow("Salt and Pepper Noise", noise_img2)
				cv2.imwrite(dir+"SnPNoise"+"_pa"+str(pa)+"_pb"+str(pb)+".png",noise_img2)
				# Box Filter
				noise_dst3 = noise_img2.copy()
				cv2.blur(noise_dst3, (kernel,kernel))
				#cv2.imshow("Box filter", noise_dst3)
				cv2.imwrite(dir+"SnP_BoxFilter"+"_pa"+str(pa)+"_pb"+str(pb)+"_K"+str(kernel)+".png",noise_dst3)
				# Gaussian Filter
				noise_dst4 = noise_img2.copy()
				cv2.GaussianBlur(noise_dst4, (kernel,kernel), 1.5)
				#cv2.imshow("Gaussian filter", noise_dst4)
				cv2.imwrite(dir+"SnP_GaussFilter"+"_pa"+str(pa)+"_pb"+str(pb)+"_K"+str(kernel)+".png",noise_dst4)				
				# Median Filter
				noise_dst5 = noise_img2.copy()
				cv2.medianBlur(noise_dst5, kernel)
				#cv2.imshow("Median filter", noise_dst5)
				cv2.imwrite(dir+"SnP_MedianFilter"+"_pa"+str(pa)+"_pb"+str(pb)+"_K"+str(kernel)+".png",noise_dst5)	
	cv2.waitKey(0)
	
if __name__ == '__main__':
    main()