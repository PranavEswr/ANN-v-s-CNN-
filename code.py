***** Library *****
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as ply
from tensorflow.keras import datasets, layers, models 

***** Load Data *****
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

***** Normalize the Train and Test Images *****
x_train = x_train/255
x_test = x_test/255

***** 2D Array to 1D Array ***** #To use sparse categorical cross entropy as loss function
y_train = y_train.reshape(-1, )
y_test = y_test.reshape(-1, )

***** Create the ANN model *****
ann = models.Sequential([
    layers.Flatten(input_shape=(32,32,3)), 
    layers.Dense(2000, activation='relu'), 
    layers.Dense(500, activation='relu'), 
    layers.Dense(10, activation='softmax')])

***** Fit and Compile the Model *****
ann.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics='accuracy')
ann.fit(x_train, y_train, epochs=10)

***** Evaluate on Test Data *****
ann.evaluate(x_test, y_test)

***** Confusion Matrix/ Classification Report *****
from sklearn.metrics import confusion_matrix, classification_report
y_pred = ann.predict(x_test)
y_pred_classes = [np.argmax(element) for element in y_pred]
print("classification report: \n", classification_report(y_test, y_pred_classes))


***** Create the CNN Model ***** #Replace ANN model with CNN to check the performance
cnn = models.Sequential([
    layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(32,32,3)), 
    layers.MaxPool2D(2,2), 
    
    layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'), 
    layers.MaxPool2D(2,2), 

    layers.Flatten(), 
    layers.Dense(100, activation='relu'), 
    layers.Dense(10, activation='softmax')])
