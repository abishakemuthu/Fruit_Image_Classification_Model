import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np

st.header('Image Classification Model')

model = load_model("C:\\Users\\Abi\\Documents\\ML Projects\\Image Classification Model\\Image_classification_model.keras")

cat = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon']

image = st.text_input('Enter the Image Name ','Apple.jpg')

image_load = tf.keras.utils.load_img(image,target_size=(180,180))
ima_arr = tf.keras.utils.array_to_img(image_load)
img_bat = tf.expand_dims(ima_arr,0)

pred = model.predict(img_bat)

score = tf.nn.softmax(pred)

st.image(image,width=200)

st.write('Veg/Fruit in image is ' , cat[np.argmax(score)])
st.write('The Accuracy is ' , round(np.max(score)*100,2))