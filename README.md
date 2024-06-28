
# Brain Tumor Detection and Classification using CNN
Overview

This software project aims to detect and classify brain tumors from medical images using Convolutional Neural Networks (CNNs).

 The CNN model is trained on a dataset of brain MRI images labeled with different types of tumor and non-tumor classes. 
 
 Once trained, the model can accurately classify new brain MRI images into these classes, aiding in medical diagnosis and treatment planning.



## Salient Features

Detection and classification of brain tumors from MRI images

Utilization of deep learning techniques, specifically CNNs, for image classification

Accurate prediction of tumor presence and type from input MRI scans
Variables Used

X: Input images (brain MRI scans)

y: Labels (tumor or non-tumor) corresponding to input images

It also helps us to distinguish between the types of Brain Tumors which could be present.
## Requirements

Hardware

CPU/GPU: A computer with a capable CPU or GPU for training the CNN model efficiently

Memory: Sufficient RAM to handle large datasets and model training

Storage: Adequate disk space for storing datasets and model checkpoints

Software:

Operating System: Compatible with Windows, macOS, or Linux

Python: Python 3.x with necessary libraries (NumPy, TensorFlow/Keras, Matplotlib, etc.)

TensorFlow/Keras: Deep learning framework for building and training CNN models

Other Python libraries: Matplotlib for visualization, scikit-learn for evaluation metrics, etc.

## Installation

Clone or download the project repository from [GitHub URL].

Install Python 3.x on your system if not already installed.

Install required Python dependencies using pip:

Copy code


```bash
  pip install -r requirements.txt
```
    
## Usage


Prepare your brain MRI images dataset and organize it into appropriate directories (e.g., train, validation, test).

We have assests folder In which the Datasets are provided.

Train the CNN model using the provided training script 
 
 or

 Here we have trained model as

 brain_tumor.h5
## Acknowledgments

This project utilizes the following libraries and frameworks:

TensorFlow/Keras: Deep learning framework for building and training CNN models

NumPy: Numerical computing library for efficient array operations

Matplotlib: Visualization library for creating plots and charts


## How to run this Project

Step 1: Clone the repository or download the project

Step 2: Open the terminal and Install all the dependencies using below code

```
pip install -r requirements.txt
```

Step 3: Once the Installation Complete use the below code

``` 
python app.py
```

This will open the a local development server 

orelse 
you can follow this link in your browser

```
http://127.0.0.1:5000
```
## What it is?

Brain Tumor Test uses the concept of Transfer Learning which enables us to use the weights and biases of some of the famous CNN architectures which decreases the amount of computational time significantly.

I've used the EfficientNetB1 architecture for this task.
## Dataset

The dataset contains a total of 10000 images of MRI Scanned clear images of patients with and without brain tumors. There are 3 major types of tumors which we're dealing with in this dataset:

Meningioma Tumor

Glioma Tumor

Pituitary Tumor

 Along with this, we also train the model on MRI Scanned images of patients who do not have a brain tumor.
 
The dataset is present on Kaggle and you can check it out by clicking on this link here
## Technology stack

Programming Language: Python

Scripting Languages: HTML, CSS

Packages: Tensorflow, Scikit-learn, OpenCV, Gunicorn, WTForms, Numpy, Pandas, Joblib, Flask Bootstrap

Backend Framework: Flask