# Data Engineering Project Proposal


#### Question/Need 
To use cloud computing and big data pipelines to create a Fashion/E-commerce Products Recommendation System based on the product images given.   


#### Data Description
The data of product infomation will be web scraping from ASOS.com by using Rapid API to collect images and labels, etc. Next, I'll create a database to storage the images data on MongoDB or Google Cloud.
I plan to start with one specific catergory (as Top) to built up my model. For modeling, I'll take the images data vectorized, then reduce dimensionality by using PCA and find its own clusters (similar patterns/materials), then make it to a predict funstion to take a new image input to identify the item catergorie and find its minimun cosine similarity from the database images in order to recommned the similar items to the buyers online. It will be an end-to-end project, I aim to set up the pipeline for the whole process and deloy it into a web application for end users. 



#### Tools
- data collection: Rapid API
- database management: MongoDB
- cloud computing: Google Cloud Platform & Google Colab
- unsupervised learning: PCA & Clustering
- (image classification : Deep Learning keras)
- app deployment: streamlit



#### MVP
- pipeline setup to get the baseline model running

