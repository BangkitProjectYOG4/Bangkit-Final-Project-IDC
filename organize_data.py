import os
import shutil


originalDataDir = 'D:/Dataset/7415_10564_bundle_archive/IDC_regular_ps50_idx5/'

datasetDir = 'Breast Histopathology Images Dataset/'
raw_datasetDir = 'Breast Histopathology Images Dataset/raw_images/'
os.mkdir(datasetDir)
os.mkdir(raw_datasetDir)

patient_list = os.listdir(originalDataDir)

for patient in patient_list:
    path_0 = originalDataDir + str(patient) + '/0'
    path_1 = originalDataDir + str(patient) + '/1'

    # create a list of all files in folder 0
    file_list_0 = os.listdir(path_0)
    # create a list of list all file in folder 1
    file_list_1 = os.listdir(path_1)

    # move the 0 images to dataset Directory
    for fname in file_list_0:
        # source path to image
        src = os.path.join(path_0, fname)
        # destination path to image
        dst = os.path.join(raw_datasetDir, fname)
        # copy the image from the source to the destination
        shutil.copyfile(src, dst)

    # move the 1 images to dataset Directory
    for fname in file_list_1:

        # source path to image
        src = os.path.join(path_1, fname)
        # destination path to image
        dst = os.path.join(raw_datasetDir, fname)
        # copy the image from the source to the destination
        shutil.copyfile(src, dst)
