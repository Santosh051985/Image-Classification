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
X_test = X_test.reshape(10000,784)
Y_train= Y_train.astype('float32')
y_test = y_test.astype('float32')
# Building a linear stack of layers with the sequential model
model = Sequential()
# Hidden layer
model.add(Dense(100,input_shape=(784,),activation='relu'))
# OutPut Layer
model.add(Dense(10,activation ='softmax'))
# looking at model summary
model.summary()
# compiling the sequential model
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
# training the model for 10 epochs
model.fit(X_train, Y_train, batch_size=128, epochs=10, validation_data=(X_test, y_test))
