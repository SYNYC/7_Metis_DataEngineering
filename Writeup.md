# Bag Hunter

Sabrina Yang


## Abstract

The goal of this project is to use data engineering and deep learning to do image classification on different luxury brands of bags and deploy the model to a web application for the user.

The main function is to identify its brand by the images of the bags, and it can benefit the e-commerce companies such as online retailers and reseller businesses.  

## Design

**0. API web scrapping + MongoDB**
**1. Preprocessing**
**2. Deep Learning**



## Data

This dataset is downloaded from [FARFETCH](https://www.farfetch.com) by web scrapping through API. One of the reasons I chose Farfetch was that their images are high resolution with clear cutout and model wear, and I think it is a good resource to build on the image classification model.

The original dataset has over 400,000 items. Since ¬¬¬¬my project is to focus on bag sections that have 21,516 items with 669 different brands from the database, then I used MongoDB to find the top list of bags brands and pick 5 out of the list – the final data size is 1670 with 5 different brands –  **YSL, Prada, Gucci, Hermes, and LV**.

# EDA image

<img src="https://github.com/SYNYC/7_Metis_DataEngineering/blob/main/img_upload/eda5.png" >



## Methodology


### 0. API web scrapping + MongoDB


    - Data ingestion:  use a Python wrapper of an API to pull JSON files Farfetch.com from Farfetch.com that can be read directly into a Mongo database for data acquisition, cleaning and eda.
      - 1. ingest new data: my code can work and properly update the database weekly by cronjob
      - 2. Database quality control: run it weekly and on only the first page since the renewal items will be added on Page 1 with not too heavy frequency – the pipeline can be run in the balance of  time and database quality

    - Data storage: NoSQL MongoDB: load a series of JSON files with data on product info directly into a MongoDB collection.

**1.Preprocessing**

- Data Directories Setup**

-	setup folders with the notebook to get data from path folders
-	download products images through MongoDB product images URL link

- Images Preprocessing**

using _keras.preprocessing_ & _ImageDataGenerator_

**2. Deep Learning**
-	 Transfer Learning (VGG16)
•	batch size = 32
•	2 Dense layers  -> 3 Dense Layers +
•	epochs = 10  -> 20
•	or epochs = 100  + callbacks.EarlyStopping + callbacks.ReduceLROnPlateau



-	Image Augmentation **

since the dataset is small so I use this method to flip to increase dataset size
•	preprocessing 1: do image dataset train-test-split via data directory
•	preprocessing 2: ImageDataGenerator on training dataset for augmentation(rotation = 40, horizontal flip)

Tried for  8 brand
but image augeta not good - overfit


**3. Pipeline processing framework **


develop reusable code for the whole process and saved the model to reuse/retrain.

**5. Deploy the processing framework as a service**
use the model to apply on streamlit for end-user to identify bags’ brands by uploading the image(supported jpg/ png/ jpeg formats)


**7. Workflow**
<img src="https://github.com/SYNYC/6_Project_ImageClassification/blob/main/charts/workflow.png" >



## Tools


1. **Numpy & Pandas**: data manipulation  
2.**MongoDB** : data storage
3. **keras** :
- image preprocessing
- Transfer Learning package
4. **streamlit**: web app deployment




## Results


### 1. Final model accuracy score
accuracy 0.7838


<img src="https://github.com/SYNYC/6_Project_ImageClassification/blob/main/charts/accuracy_loss.png" >

### 2. Streamlit app screenshot

<img src="https://github.com/SYNYC/6_Project_ImageClassification/blob/main/charts/accuracy_loss.png" >
