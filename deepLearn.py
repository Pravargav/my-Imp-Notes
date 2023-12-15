import os
import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from sklearn.model_selection import train_test_split

##"C:\Users\dell\ml1\Images\agricultural"
##"C:\Users\dell\ml1\Images\airplane"...etc.
data = []
labels = []
paths= ['agricultural','airplane','baseballdiamond','beach','buildings','chaparral','denseresidential','forest','freeway','golfcourse','harbor','intersection','mediumresidential','mobilehomepark','overpass','parkinglot','river','runway','sparseresidential','storagetanks','tenniscourt']
classes = 21
cur_path = os.getcwd()

for i in range(classes):
    path = os.path.join(cur_path,'Images/',paths[i])
    images = os.listdir(path)

    for a in images:
        try:
            image_path = os.path.join(path, a)
            image = Image.open(image_path)
            image = image.resize((64, 64))
            image = np.array(image)
            data.append(image)
            labels.append(i)
        except Exception as e:
            print(e)

data = np.array(data)
labels = np.array(labels)

# Normalize the pixel values
data = data.astype('float32')/255.0


#############################################################################

# One-hot encoding of labels
from tensorflow.python.keras.utils import np_utils
labels = np_utils.to_categorical(labels)

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

model = Sequential()

model.add(Conv2D(32, (2, 2), input_shape=(64, 64, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (2, 2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(21))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test), batch_size=64)

# Evaluate the model on the test data
score = model.evaluate(X_test, y_test, batch_size=64)

print("Test Loss:", score[0])
print("Test Accuracy:", score[1])
