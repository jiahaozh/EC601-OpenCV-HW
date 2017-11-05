import cv2
import numpy as np
import sys

# Author Rishab Shah
# Adapted to Python by Nick VanDeusen

def Add_salt_pepper_Noise(srcArr, pa, pb):
	cv2.rng # rand number generate
	amount1 = srcArr.rows*srcArr.cols*pa # Need to run through all channels
	amount2 = srcArr.rows*srcArr.cols*pb
	
	counter = 0
	for counter in range(amount1):
		srcArr.at<uchar>(rng.uniform( 0,srcArr.rows), rng.uniform(0, srcArr.cols)) = 0

	for counter in range(amount1):
		srcArr.at<uchar>(rng.uniform(0,srcArr.rows), rng.uniform(0,srcArr.cols)) = 255

def Add_gaussian_Noise(srcArr, mean, sigma):
    NoiseArr = srcArr.clone()
    cv2.rng
    rng.fill(NoiseArr, RNG::NORMAL, mean,sigma)
    cv2.add(srcArr, NoiseArr, srcArr)

def main:
	# Original
	image = cv2.imread(sys.argv[1])
	cv2.namedWindow("Original image", cv2.WINDOW_NORMAL)
	cv2.imshow("Original image", image)
	
    noise_img = image.clone() 
    mean = 0		
    sigma = 50		# Not the variance
    Add_gaussian_Noise(noise_img, mean, sigma)
    cv2.imshow("Gaussian Noise", noise_img);

    noise_dst = noise_img.clone()
    cv2.blur(noise_dst, noise_dst, Size(3,3))
    cv2.imshow("Box filter", noise_dst)

    noise_dst1 = noise_img.clone()
    cv2.GaussianBlur(noise_dst1, noise_dst1, Size(3,3), 1.5)
    cv2.imshow("Gaussian filter", noise_dst1)
    
    noise_dst2 = noise_img.clone()
    cv2.medianBlur(noise_dst2, noise_dst2, 3)
    cv2.imshow("Median filter", noise_dst2)
    
    noise_img2 = image.clone()
    pa = 0.01	# Controls the amount of black spots in the noise
    pb = 0.01	# Controls the amount of white spots in the noise
    Add_salt_pepper_Noise(noise_img2, pa, pb); 
    cv2.imshow("Salt and Pepper Noise", noise_img2)

    noise_dst3 = noise_img2.clone()
    cv2.blur(noise_dst3,noise_dst3,Size(3,3))
    cv2.imshow("Box filter", noise_dst3)

    noise_dst4 = noise_img2.clone()
    cv2.GaussianBlur(noise_dst4, noise_dst4, Size(3,3), 1.5)
    cv2.imshow("Gaussian filter", noise_dst4)
    
    noise_dst5 = noise_img2.clone()
    cv2.medianBlur(noise_dst5, noise_dst5, 3)
    cv2.imshow("Median filter", noise_dst5)
	
if __name__ == '__main__':
    main()