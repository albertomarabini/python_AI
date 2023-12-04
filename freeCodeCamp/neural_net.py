# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# downloading the crazy dataset
fashion_mnist = keras.datasets.fashion_mnist  # load dataset        
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()  # split into tetsing and training

train_images.shape  # 60,000 images, each 28x28 pixels

train_images[0,23,23]  # let's have a look at one pixel
# print(train_images)

train_labels[:10]  # let's have a look at the first 10 training labels

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# plt.figure()
# plt.imshow(train_images[3])
# plt.colorbar()
# plt.grid(False)
# plt.show()

# Preprocessing: reduce the values from 0-255 to 0-1
train_images = train_images / 255.0
test_images = test_images / 255.0

#################################################################
# Building the model
#################################################################
# Layer 1: This is our input layer and it will conist of 784 neurons. 
# We use the flatten layer with an input shape of (28,28) to denote that our 
# input should come in in that shape. The flatten means that our layer will 
# reshape the shape (28,28) array into a vector of 784 neurons so that each 
# pixel will be associated with one neuron.

# Layer 2: This is our first and only hidden layer. The "dense" denotes that 
# this layer will be fully connected and each neuron from the previous layer 
# connects to each neuron of this layer. It has 128 neurons and uses the rectify 
# linear unit activation function.

# Layer 3: This is our output later and is also a dense layer. It has 10 neurons
# that we will look at to determine our models output. Each neuron represnts the 
# probabillity of a given image being one of the 10 different classes. 
# The activation function "softmax" is used on this layer to calculate a 
# probabillity distribution for each class. This means the value of any neuron 
# in this layer will be between 0 and 1, where 1 represents a high probabillity 
# of the image being that class.

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # input layer (1)
    keras.layers.Dense(128, activation='relu'),  # hidden layer (2)
    keras.layers.Dense(10, activation='softmax') # output layer (3)
])

# The last step in building the model is to define the loss function, optimizer and metrics we would like to track.
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#################################################################
# Training the model
#################################################################
model.fit(train_images, train_labels, epochs=10)  # we pass the data, labels and epochs and watch the magic!

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=1) 

print('Test accuracy:', test_acc)

#################################################################
# Making predictions
#################################################################

# predictions = model.predict(test_images)
# print(predictions[0])
# print(np.argmax(predictions[0]))
# print(test_labels[0])

COLOR = 'white'
plt.rcParams['text.color'] = COLOR
plt.rcParams['axes.labelcolor'] = COLOR

def predict(model, image, correct_label):
  class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
  prediction = model.predict(np.array([image]))
  predicted_class = class_names[np.argmax(prediction)]

  show_image(image, class_names[correct_label], predicted_class)


def show_image(img, label, guess):
  print("Excpected: " + label)
  print("Guess: " + guess)
  plt.figure()
  plt.imshow(img, cmap=plt.cm.binary)
  plt.colorbar()
  plt.grid(False)
  plt.show()


def get_number():
  while True:
    num = input("Pick a number: ")
    if num.isdigit():
      num = int(num)
      if 0 <= num <= 1000:
        return int(num)
    else:
      print("Try again...")

while True:
    num = get_number()
    image = test_images[num]
    label = test_labels[num]
    predict(model, image, label)