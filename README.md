# Bangkit-Final-Project-IDC

Dataset source :  ['Breast Histopathology Images'] (https://www.kaggle.com/paultimothymooney/breast-histopathology-images)

## Dataset

    The data contains 279 folder from Breast Cancer patient. The total images in this dataset is 277,524 with 50 x 50 pixels RGB and we use 70% (around 194,266) images for training and 30% (83,258)for testing.
Our target is to predict wether it contains IDC or not. 

## Model

    In this model we use Convolutional Neural Network (CNN). We use Convolution 2D with ReLU activation, Max Pooling 2D, Batch Normalization, Dropout, Flatten and the last one we use 2 Dense layer with the last one using sigmoid activation. On the without improvement moodel we stack 3 times consist Convolution 2D 3 times and then continued with Max Pooling 2D and then dropout. On the improved CNN we stack Convolution 2D with ReLU activation, Max Pooling 2D, Batch Normalization 3 times, and then we use Dropout on 0.3, after that we add Flatten and some Dense layer with the last Dense activation sigmoid. We use Stochastic Gradient Descent (SGD) optimizers with 0.001 learning rate and binary crossentropy for the loss function. We also use scheduled learning rate when the accuracy don't improved after an epoch, and checkpoint to saved the best accuracy when training the model.

## Result

Accuracy : 0.84
Validation Accuracy : 0.84

## 
