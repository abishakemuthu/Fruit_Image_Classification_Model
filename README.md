## Fruit Image Classification

![Deep Learning](https://github.com/user-attachments/assets/04f6b5a6-4c9c-4e2f-aa71-7653834d564f)

## Objective

The objective of this project is to design and implement a deep learning model using sequential convolutional neural networks (CNNs) to accurately classify fruit images. Applied advanced image preprocessing techniques and optimized the model for improved accuracy and performance, achieving high classification precision on diverse fruit datasets.

## Import the Data

Imported the training, testing and validation images and resized them into 180 x 180 for consistant size.

## Visualization of fruit images

![set](https://github.com/user-attachments/assets/c31c0bdc-24b1-419e-8e38-fd772c6d4538)

## Sequential CNN Model

Created a sequential CNN model which will,
- Rescale the image pixel values between 0 to 1.
- Apply convolutional layer which will apply 16 filters to the input.
- Padds the input with 0. So, the width and height of the output will be same.
- Apply ReLU activation function, which introduces non-linearity to the model.
- Apply max pooling layer that reduces the width and height of the feature maps. It takes the maximum value from 2x2 blocks of the input, which helps reduce the amount of computation and extract the most important features.
- Again performs the above steps with 32 filters and 64 filters to extract more complex feature from the data.
- Flattens the 2D feature maps from the convolutional layers into a 1D vector. This is necessary before passing the data into fully connected dense layers.
- Apply Dropout regularization which will randomly drop 20% of the neurons to prevent overfitting by making the model less reliant on specific neurons.
- Set it with 128 neurons, each neuron is connected to all the neurons from the previous layer, which allows the model to combine all the learned features and make decisions.
- Given the length of category, Each neuron in this layer represents a category and the model will predict a probability for each class.
- Used Adam optimizer which will adjust the model’s weights during training to minimize the loss (error).
- Used Sparse Categorical Crossentropy to predict the output which has multiple classes.
- Used accuracy as metrics.

## Training

- Fitted the train data with the validation data which is help to evaluate the model’s performance after each epoch. This helps track the model's performance on unseen data and prevents overfitting.
- I have set the epoch as 25, which will make the model will go through the entire training dataset 25 times. In each epoch, the model will extract more features improving the accuracy and reducung the loss.

- ![graph](https://github.com/user-attachments/assets/6c16eeab-983b-4375-b3cd-3769c6456493)

## Testing and Deployment

- I have tested the model with 5 Fruit images and checked the accuracy.
- Saved the model in Jupiter notebook and Deployed the model with the help of streamlit library in VS Code.

## Tested Images with Accuracy

![Screenshot 2024-10-05 103832](https://github.com/user-attachments/assets/b228c629-25dd-4599-a964-fc13e88d05bd)

![Screenshot 2024-10-05 103606](https://github.com/user-attachments/assets/755b8a68-464f-4a5e-b938-d5def90577a1)

![Screenshot 2024-10-05 103543](https://github.com/user-attachments/assets/d615d519-7eeb-4dab-956d-cf6c620b6fe5)

![Screenshot 2024-10-05 103504](https://github.com/user-attachments/assets/f9bb12bf-7f35-43d4-bbef-9d9571678ccb)

![Screenshot 2024-10-05 103437](https://github.com/user-attachments/assets/3d79cdfc-23eb-4adf-90bb-58bcc4964178)
