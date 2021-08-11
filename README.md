# Data Engineering Project Proposal

### Question/Need 
To use cloud computing and big data pipelines to create a Fashion/E-commerce Products Recommendation System based on the product images given.   


#### Data Description
The data of product information will be web scraping from ASOS.com by using Rapid API to collect images and labels, etc. Next, I'll create a database to store the images data on MongoDB or Google Cloud.
I plan to start with one specific category (as Top) to built up my model. For modeling, I'll take the images data vectorized, then reduce dimensionality by using PCA and find its own clusters (similar patterns/materials), then make it to a predict function to take a new image input to identify the item categorise and find the minimum cosine similarity from the database images in order to recommend the similar items to the buyers online. If necessary, I'll use Google Cloud Platform and Google Colab for a more efficient way to deal with big data.

It will be an end-to-end project, I aim to set up the pipeline for the whole process and deploy it into a web application for end-users.


#### Tools
- data collection: Rapid API
- database management: MongoDB
- cloud computing: Google Cloud Platform & Google Colab
- unsupervised learning: PCA & Clustering
- (image classification: Deep Learning keras)
- app deployment: streamlit



#### MVP
- pipeline setup to get the baseline model running
