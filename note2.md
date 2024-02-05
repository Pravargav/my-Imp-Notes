#How to open pycharm project
----------------------------
Always open pycharm from file manager open as pycharm project then only terminal opens unless terminal cannot open as local


Imagedatagenarator doesnot add new augmented images(5) to the existing original image(1) containint directory.ie.5+1 =6 in directory is false.
it generates 5 images of exisitin single image virtually not physically and use those 5 virtual images for training not the single image in the directory used for training.
->directory name: dir
->directory has only one image for training 
->dir/img.jpg
->after using image generator 
->diretory: dir/img.jpg no change 
->but 5 virtual images generated using img.jpg virtually img1,img2...img5 and deleted automatically after training 
