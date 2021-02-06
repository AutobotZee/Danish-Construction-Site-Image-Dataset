# Danish-Construction-Site-Image-Dataset
Construction industry posses an interesting application are for the Computer Vision task of object detection. This data set was developed from capturing images from construction sites in denmark's Technical University of Denmark, Lyngby campus. The dataset contains classes annotated in Yolo1,1 format.

The Weights are provided in the link below along with the dataset.

The link for Downloading the Dataset:
https://drive.google.com/drive/folders/1xz1QVWeqc8bx4wgBXsdpdUI-NW9dVzVL?usp=sharing

## Prequisite.
Annotations are performed using [cvat](https://github.com/openvinotoolkit/cvat) annotation tool. Additional data annotation can be performed using the same tool.
framework used for training is Darknet avaialble on [Darknet](https://github.com/AlexeyAB/darknet) which is also a original Yolov4 driectory. 

## Image Data with annotation
The Data set is split into 5 main folders. Images are annotated in Yolo1.1 format and 
1. **Real_images**: Sensor Images from camera.
2. **Obj_train_data**: Web Images scraped form [idt tool](https://github.com/deliton/idt)
3. **Batch_web_img**: A selected bag of web images of 200 Images
4. **rft**: Test images from a rooftop renovation project. Made for testing on trained models.
5. **HD_test**: High resolution Images for checking model accuracy.

While using the folders make sure you have all this folder in your **\data** folder while deploying it on default darknet environmnet.


## data and obj files 
The data files contains configurations for running the model configurations on differet training dataset and validation set.

1. To train data on sensor images only use obj.data
2. To train data on sensor and web images only use obj_itr2.data

## Model testing
xval.txt and rft_1.txt files are files that hold data indexing for testing of Images.
To use data that is form the same pool of images used during training configure the .data filees with
xval.txt . To check the performance of data on a unseen datase from a different environment use rft_1.txt

## Uning Pre-Trainined models for demo
The pretrainned models can be used to detect objects in stream and images from construction site
The default class data is shown in obj.names file.
Configuration files can be used from cfg folder to load desireed model network with huper parameters.
Pre trained weights are given in the link below.

Weights for Yolov4 model [yolov4](https://drive.google.com/file/d/1Gtz_zl7HYYr6fv4F4RWYyTY0rkvHONMb/view?usp=sharing)

Weights for Yolov4-tiny model [yolov4-tiny](https://drive.google.com/file/d/13NUCCp65LDONRDFy2DRf_gkXvq4DLfW-/view?usp=sharing)

Weights for Yolov4-tiny-3l model [yolov4-tiny-3l](https://drive.google.com/file/d/1P1i_-4Pia5IWZoFdfjUM8DclNPuhmWI2/view?usp=sharing)
