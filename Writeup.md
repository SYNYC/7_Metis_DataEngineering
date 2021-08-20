# Bag Hunter

Sabrina Yang


## Abstract

The goal of this project is to use data engineering and deep learning to do image classification on different luxury brands of bags and deploy the model to a web application for the user.

The main function is to identify its brand by the images of the bags, and it can benefit the e-commerce companies such as online retailers and reseller businesses.  

## Design

0. API web scrapping + MongoDB
1. Preprocessing
2. Deep Learning
3. Pipeline processing framework to auto renew database and retrain the model
4. Deploy the processing framework as an app service

## Data

This dataset is downloaded from [FARFETCH](https://www.farfetch.com) by web scrapping through API. One of the reasons I chose Farfetch was that their images are high resolution with clear cutout and model wear, and I think it is a good resource to build on the image classification model.

The original website dataset has over 400,000 items downloaded in MongoDB.
The goal of my project is to focus on bag sections which have 21,516 items with 669 different brands from the database, and I used MongoDB to find the top list of bags brands and pick 5 out of the list – the final data size is 1670 with 5 different brands –  **YSL, Prada, Gucci, Hermes, and LV**.

#### EDA image

<img src="https://github.com/SYNYC/7_Metis_DataEngineering/blob/main/img_upload/eda5.png" >





## Methodology


**0. API web scrapping + MongoDB**


- __Data ingestion__:  
use a Python wrapper of an API to pull JSON files from Farfetch.com that can be read directly into a Mongo database for data acquisition, cleaning and eda.
  - a. ingest new data: the code can work and properly update the database 
  - b. Database quality control: run it bi-weekly and on only the first page since the renewal items will be added on Page 1 with not too heavy frequency – the pipeline can be run in the balance of time and database quality

- __Data storage__: 
MongoDB is NoSQL database, which is suitable to load a series of JSON files with data on product info directly into a MongoDB collection.

**1. Preprocessing**

- __Data Directories Setup__: setup folders with the notebook to get data from path folders. Directly download products images through MongoDB product images URL link

- __Images Preprocessing__: using _keras.preprocessing_ & _ImageDataGenerator_

**2. Deep Learning**

-	 __Transfer Learning (VGG16)__ : 
batch size = 32, added 3 Dense Layers, epochs = 20, and tried epochs = 100  + callbacks.EarlyStopping + callbacks.ReduceLROnPlateau

-	__Image Augmentation__: 
since the dataset is small so I use this method to flip to increase dataset size(rotation = 40, horizontal flip), however, the test accuracy score is higher than the training score which shows overfitting, so I didn’t use this approach to continue my training. 


- __Multi classification__: 
I tried to increase the classes number as 3,5,6 and 8 different brands to classify, and the accuracy scores are around 70-80%, but since the data size is small and given Image Augmentation had an overfit issue in my case, I decided to take 5 different brands model as the final deployment. 




**3. Pipeline processing framework to auto renew database and retrain model**

- develop reusable python code for the whole process and saved the model to reuse/retrain
- set cron job to command API to renew MongoDB data bi-weekly
- as above, after collecting the new feeding data for every 3 months, the deep learning model is set to connect the database and retrain the model to renew quarterly/seasonally 



**4. Deploy the processing framework as an app service**


- use the model to apply on streamlit for end-user to identify bags’ brands by uploading the image(supported jpg/ png/ jpeg formats)


**Workflow**
<img src="https://github.com/SYNYC/7_Metis_DataEngineering/blob/main/img_upload/workflow_.png" >



## Tools


1. **Numpy & Pandas**: data manipulation  
2. **MongoDB** : data storage
3. **keras** : transfer Learning package & image preprocessing
4. **streamlit**: web app deployment




## Results


### 1. Final model accuracy score
accuracy 0.7838


<img src="https://github.com/SYNYC/6_Project_ImageClassification/blob/main/charts/accuracy_loss.png" >

### 2. Streamlit app screenshot

<img src="https://github.com/SYNYC/7_Metis_DataEngineering/blob/main/img_upload/app_demo_all.png" >
