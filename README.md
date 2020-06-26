# Bangkit-Final-Project-IDC

Dataset source :  ['Breast Histopathology Images'](https://www.kaggle.com/paultimothymooney/breast-histopathology-images)

## Project Description
This project is about make an classification piece of breast histopathology images for get know if the image contain Invasive Ductal Carcinoma (IDC) or not in breast area. Basicly this project to analyze the image for early detection for Breast Cancer because IDC is the most common subtype of all breast cancers. The detection is using Breast histopathology images size of 50x50 Pixel and after processed prediction on client side, it'll result is the image contain IDC or normal with percentege probability of the prediction.

## Reason

Why we choose to do this project are beacuse of some reasons :
    - Breast cancer has the second highest mortality rate after Lung & Bronchial cancer
    - Images are acquired by histopathology
    - Manual detection is a tedious, tiring task and most likely to comprise human error
    - Computational in histopathology image can help Pathology job to do early detection
    - Malignant tumors are cancerous and should be treated as soon as possible to reduce and prevent further complications
 More detail explantion in [Presentation Slide](https://raw.githubusercontent.com/BangkitProjectYOG4/Bangkit-Final-Project-IDC/3bd4b93368f59b4ca0260bf0814ea406183f5c1f/Presentation%20and%20Reserch%20Papers%20review/Bangkit%20Final%20Project%20Presentation%20.pdf)

## Dataset

The data contains 279 folder from Breast Cancer patient. The total images in this dataset is 277,524 with 50 x 50 pixels RGB and we use 70% (around 194,266) images for training and 30% (83,258)for testing.
Our target is to predict wether it contains IDC or not. 

## Model

In this model we use Convolutional Neural Network (CNN). We use Convolution 2D with ReLU activation, Max Pooling 2D, Batch Normalization, Dropout, Flatten and the last one we use 2 Dense layer with the last one using sigmoid activation. On the without improvement moodel we stack 3 times consist Convolution 2D 3 times and then continued with Max Pooling 2D and then dropout. On the improved CNN we stack Convolution 2D with ReLU activation, Max Pooling 2D, Batch Normalization 3 times, and then we use Dropout on 0.3, after that we add Flatten and some Dense layer with the last Dense activation sigmoid. We use Stochastic Gradient Descent (SGD) optimizers with 0.001 learning rate and binary crossentropy for the loss function. We also use scheduled learning rate when the accuracy don't improved after an epoch, and checkpoint to saved the best accuracy when training the model.

## Improvment

The baseline model is created using 3 Base CNN Layers with each layer contain 3 times Conv2D layers then MaxPooling and Dropout 30% then contiune using Flatten and 2 neural network Layers with softmax activation for Output. this baseline model got 94% training accuracy and 88% Validation accuracy.
Notebook Before Improvement[Link Notebook](https://github.com/BangkitProjectYOG4/Bangkit-Final-Project-IDC/notebook/brefore_improvement/part-1-breast-cancer-analyzer-web-app.ipynb)

After we tried some chaning such as add BatchNormalization, activation, learning rate, and epoch. we got model with both 84% on training and validation accuracy which is seems good model with less gap in train and validation accuracy. We also got faster training and execution prediction time that save more compuational rescouces.
Notebook Before Improvement[Link Notebook](https://github.com/BangkitProjectYOG4/Bangkit-Final-Project-IDC/notebook/after_improvement/Breast_Cancer%20.ipynb)

## Result

- Accuracy : 0.84
- Validation Accuracy : 0.84

[Model](https://github.com/BangkitProjectYOG4/Bangkit-Final-Project-IDC/models)
There's 2 version model : 
- original model h5 and pb format
- converted model to Tensorflow.Js for Javascript format

## Bug and Lesson
- Sometime, there's a execution problem for rounding the probability value when try to predict multiple image at the same time.
- There's no grey area result for this classification, so the result only can be either normal or IDC.

Note : 
- this project and prediction is still on development and still can't be using for diagnosis or analzyer Breast Cancer basis
 
