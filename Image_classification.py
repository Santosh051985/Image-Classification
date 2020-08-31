from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout,Conv2D,MaxPool2D, Flatten
from keras.utils import np_utils
#loading Data Set
(X_train, Y_train), (X_test,y_test)=  mnist.load_data()
# print Dataset shape
print("X_trian Shape", X_train)
print("X_train Shape", X_train.shape)
print("X_test shape", X_test.shape)
print("Y_train shape", Y_train.shape)
print("y_test Shape", y_test.shape)
#Flatting image from 28x28 pixels to 1D 787 pixels
X_train = X_train.reshape(60000,784)
