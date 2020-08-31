from keras.datasets import mnist
#loading Data Set
(X_train, Y_train), (X_test,y_test)=  mnist.load_data()
# print Dataset shape
print("X_trian Shape", X_train)
print("X_train Shape", X_train.shape)
