# Detection-of-Foot-and-Mouth-Disease-in-Cattle
A Portable device based on Machine Learning algorithm using de10nano FPGA to detect Foot and Mouth disease in cattle

__ABOUT THE PROJECT:__
  
  The Portable device is built using the DE 10-Nano Cyclone V SoC FPGA board. The device detects the possiblity of Foot and Mouth disease in cattle. The device is trained using the SVM Machine Learning algorithm.

__BUILT WITH:__

The major libraries used in this project are:
* sklearn
* pandas
* matplotlib
* skimage
* numpy
* pickle
* opencv
* subprocess
* Tkinter

__GETTING STARTED:__

*__Training model__*

The __training_model.py__ consists the code for training and testing the dataset. This code generates the trained model which is used in detection of the FMD disease. This model provides efficiency upto 75%, with the highest obtained accuracy of 83.066%. This model generates the pickle file '__img_model.p__' used for detecting the disease. The pickle file is used to serialize and de-serialize the python object structures. Serializing converts the object in the memory to byte stream, this helps in the easy execution of the program in different OS systems and can be sent easily over the network, making the model more compatible.

*__Prediction__*

The pre-trained pickle module __img_model__ is imported in the __Prediction.py__ python module. The __Prediction.py__ interfaces the __camerain.cpp__ code using the subprocess library. Graphical User Interface is built by the usage of Tkinter library for easy accessiblity of the end users.







