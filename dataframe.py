import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split


def extract_patient_id(x):
    # split into a list
    a = x.split('_')
    # the id is the first index in the list
    patient_id = a[0]

    return patient_id


def extract_x_axis(x):
    # split into a list
    a = x.split('_')
    # the id is the first index in the list
    x_axis = a[2]

    return x_axis.replace('x', '')


def extract_y_axis(x):
    # split into a list
    a = x.split('_')
    # the id is the first index in the list
    y_axis = a[3]

    return y_axis.replace('y', '')


def extract_target(x):
    # split into a list
    a = x.split('_')
    # the target is part of the string in index 4
    b = a[4]
    # the ytarget i.e. 1 or 2 is the 5th index of the string --> class1
    target = b[5]

    return target


image_list = os.listdir(
    os.getcwd()+'/Breast Histopathology Images Dataset/raw_images/')
df_data = pd.DataFrame(image_list, columns=['image_id'])

# create a new column called 'patient_id'
df_data['patient_id'] = df_data['image_id'].apply(extract_patient_id)
# create a new column called 'x_axis'
df_data['x_axis'] = df_data['image_id'].apply(extract_x_axis)
# create a new column called 'y_axis'
df_data['y_axis'] = df_data['image_id'].apply(extract_y_axis)
# create a new column called 'target'
df_data['target'] = df_data['image_id'].apply(extract_target)

df_data.to_csv(os.getcwd()+'/breast_Histopathology_images_dataframe.csv')

SAMPLE_SIZE = 78786
IMAGE_SIZE = 50

# take a sample of the majority class 0 (total = 198738)
df_0 = df_data[df_data['target'] == '0'].sample(SAMPLE_SIZE, random_state=101)
# take a sample of class 1 (total = 78786)
df_1 = df_data[df_data['target'] == '1'].sample(SAMPLE_SIZE, random_state=101)

# concat the two dataframes
df_data = pd.concat([df_0, df_1], axis=0).reset_index(drop=True)

df_data.to_csv(
    os.getcwd()+'/breast_Histopathology_images_dataframe_balanced.csv')

df_train, df_val = train_test_split(
    df_data, test_size=0.10, random_state=101, stratify=df_data['target'])


# create a path to 'base_dir' to which we will join the names of the new folders
datasetDir = 'Breast Histopathology Images Dataset/'
rawDatasetDir = 'Breast Histopathology Images Dataset/raw_images/'

# train_dir
train_dir = os.path.join(datasetDir, 'train_dir')
os.mkdir(train_dir)

# val_dir
val_dir = os.path.join(datasetDir, 'val_dir')
os.mkdir(val_dir)


# [CREATE FOLDERS INSIDE THE TRAIN AND VALIDATION FOLDERS]
# Inside each folder we create seperate folders for each class

# create new folders inside train_dir
a_no_idc = os.path.join(train_dir, 'a_no_idc')
os.mkdir(a_no_idc)
b_has_idc = os.path.join(train_dir, 'b_has_idc')
os.mkdir(b_has_idc)


# create new folders inside val_dir
a_no_idc = os.path.join(val_dir, 'a_no_idc')
os.mkdir(a_no_idc)
b_has_idc = os.path.join(val_dir, 'b_has_idc')
os.mkdir(b_has_idc)

df_data.set_index('image_id', inplace=True)

# Get a list of train and val images
train_list = list(df_train['image_id'])
val_list = list(df_val['image_id'])


# Transfer the train images

for image in train_list:

    # the id in the csv file does not have the .tif extension therefore we add it here
    fname = image
    # get the label for a certain image
    target = df_data.loc[image, 'target']

    # these must match the folder names
    if target == '0':
        label = 'a_no_idc'
    if target == '1':
        label = 'b_has_idc'

    # source path to image
    src = os.path.join(rawDatasetDir, fname)
    # destination path to image
    dst = os.path.join(train_dir, label, fname)
    # move the image from the source to the destination
    shutil.move(src, dst)


# Transfer the val images

for image in val_list:

    # the id in the csv file does not have the .tif extension therefore we add it here
    fname = image
    # get the label for a certain image
    target = df_data.loc[image, 'target']

    # these must match the folder names
    if target == '0':
        label = 'a_no_idc'
    if target == '1':
        label = 'b_has_idc'

    # source path to image
    src = os.path.join(rawDatasetDir, fname)
    # destination path to image
    dst = os.path.join(val_dir, label, fname)
    # move the image from the source to the destination
    shutil.move(src, dst)
