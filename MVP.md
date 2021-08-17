# MVP

The goal of my project is to build an images classification model that has predictive power for different brands of bags. I am building my data set from web scrapping Farfetch.com and using API from the site. https://www.farfetch.com/plpslice/listing-api/products-facets.
From the data structure, I was able to use a Python wrapper of an API to pull JSON files that can be read directly into a Mongo database (NoSQL) and stored data.


#####  EDA

- database: 428,940 documents stored in MongoDB

- only aiming for bags : 21,050 documents

- only focus on 3 bags brands on the early stage

- Three classes : {'bag Gucci': 0, 'bag Prada': 1, 'bag YSL': 2}
	- Total : 1587 documents
	- Train dataset: Found 1271 files belonging to 3 classes.
	- Validation dataset: Found 316 files belonging to 3 classes.





## app - early stage


<img src="https://github.com/SYNYC/5_Project_Tweets_about_Tesla_Stock/blob/main/charts/date_sentiment.png">




## Next step

Next, I am aiming to build a data engineering pipeline for re-scape data that can process and ingest new products info data, then update and storage to the database properly. The purpose of getting new data is to help the model to evolve and learn new and more current designers styles and collections by updating the new info and image of products. The update timeframe will be weekly and the model will re-run training by monthly.






- rescale the images size to 150 x 150
