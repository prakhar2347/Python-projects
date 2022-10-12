# Image-to-pencil-sketch
Write a python code to convert Images to Sketch
## Flow of Code
- We need to read the image in RBG format and then convert it to a grayscale image. 
- Then the next thing to do is invert the grayscale image also called negative image, this will be our inverted grayscale image. 
- Inversion can be used to enhance details. 
- Finally create the pencil sketch by mixing the grayscale image with the inverted blurry image. This can be done by dividing the grayscale image by the inverted blurry image. Since images are just arrays, do this programmatically using the divide function from the cv2 library in Python.

![](ImgToSketch.jfif)