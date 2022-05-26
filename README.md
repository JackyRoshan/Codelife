 Using opencv+simplefacerecognition


## Requirements

Python 3.7 or later with dilb and opencv.


## Functions:

### Real-time facial recognition:
The program can display the name of the target when the camera captures its face after storing its photo.

### Image Comparison:
The program compares two pictures stored in a folder to confirm if they are pictures of the same person.

## Methodology:

### BGR to RGB
Three methods in the cv2 package are used here.

cv2.imread(path) loads an image from the specified file. Returns an empty matrix if the image cannot be read.
cv2.cvtColor(src,color) method is used to convert an image from one color space to another. Src(img) is the image whose color space we wish to convert.
as follows:
cv2.waitkey() allows the user to display a window for a given millisecond or until any key is pressed. If you pass 0 in the parameter, it will wait until any key is pressed.
Since we set it to 0, it will always show the picture window.


### Image encode
The face_recognition.face_encodings() and face_recognition.compare_faces() methods are both included in the face_recognition package.
face_encodings() will be given an image, and return the 128-dimensional face encoding for each face in the image.
compare_faces() will compare the list of face encodings with the candidate encodings to see if they match. Its return value will be true/false.


### Deep metric learning
Instead of trying to output a single label (or even the coordinates/bounding box of objects in an image), we are instead outputting a real-valued feature vector.
For the dlib facial recognition network we used here, the output feature vector is 128-d (which means a list of 128 real-valued numbers) that is used to quantify the face. Training the network is done using triplets.

For example, here we provide three images from the network:
Two of these images are example faces of the same person.
The third image is a random face from our dataset and is not the same person as the other two images. one of Chad Smith and two of Will Ferrell.
Our network quantifies the faces, constructing the 128-d embedding for each.
For two face images of the same person, we adjust the neural network weights by the distance metric to make the vectors closer.


## Reproduce Our Training

You can upload the pictures to the "images" file to make your own training.

## Quote
Dlib:(https://github.com/coneypo/Dlib_install)
