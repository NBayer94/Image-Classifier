from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

model = load_model('image_classifier.tf')
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

def predict_image(path):
    img = load_img(path, target_size=(32, 32))
    img = img_to_array(img)/255
    img = img.reshape(1, 32, 32, 3)
    prediction = np.argmax(model.predict(img), axis=-1) [0]
    return class_names[prediction]