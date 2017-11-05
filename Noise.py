import cv2
import numpy as np
import sys

# Author Rishab Shah
# Adapted to Python by Nick VanDeusen

def Add_salt_pepper_Noise(Mat &srcArr, float pa, float pb )

def Add_gaussian_Noise(Mat &srcArr,double mean,double sigma);


def main:
    Mat image;
    image = imread(argv[1], 0);
    namedWindow( "Original image", CV_WINDOW_AUTOSIZE );
    imshow( "Original image", image);

    Mat noise_img = image.clone(); 
    float mean = 0;			
    float sigma = 50;		//Not the variance
    Add_gaussian_Noise(noise_img, mean, sigma);
    imshow( "Gaussian Noise", noise_img);

    Mat noise_dst = noise_img.clone();
    blur(noise_dst,noise_dst,Size(3,3));
    imshow( "Box filter", noise_dst);

    Mat noise_dst1 = noise_img.clone();
    GaussianBlur(noise_dst1, noise_dst1, Size(3,3),1.5);
    imshow( "Gaussian filter", noise_dst1);
    
    Mat noise_dst2 = noise_img.clone();
    medianBlur(noise_dst2,noise_dst2,3);
    imshow( "Median filter", noise_dst2);
    
    Mat noise_img2 = image.clone(); 
    float pa=0.01;			#Controls the amount of black spots in the noise
    float pb=0.01;			#Controls the amount of white spots in the noise
    Add_salt_pepper_Noise(noise_img2, pa, pb); 
    imshow( "Salt and Pepper Noise", noise_img2);

    Mat noise_dst3 = noise_img2.clone();
    blur(noise_dst3,noise_dst3,Size(3,3));
    imshow( "Box filter", noise_dst3);

    Mat noise_dst4 = noise_img2.clone();
    GaussianBlur(noise_dst4,noise_dst4,Size(3,3),1.5);
    imshow( "Gaussian filter", noise_dst4);
    
    Mat noise_dst5 = noise_img2.clone();
    medianBlur(noise_dst5,noise_dst5,3);
    imshow( "Median filter", noise_dst5);
	
if __name__ == '__main__':
    main()