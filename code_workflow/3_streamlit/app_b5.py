import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import cv2

import keras
from keras.models import load_model
from scipy.spatial import distance

from skimage.transform import resize
import time

import matplotlib.pyplot as plt


import pymongo

# start on terminal
# streamlit run app.py


################
##    Model   ##
################


# Load the model
model = load_model('/Users/sabrina/Metis/Projects/7_Project_Engineering/code/2_modeling/models/5_brands/ff_bag_1_v1.h5')
# Load the cascade
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


############################
##   Animation & Ballon   ##
############################



progress_bar = st.progress(0)
status_text = st.empty()
#status_text.text('Done!')
st.balloons()

################
##   Title    ##
################

# Designing the interface

image = Image.open('/Users/sabrina/Metis/Projects/7_Project_Engineering/img/ppt/farfect_1.jpeg')


col1, col2, col3= st.beta_columns([80,2,8])
with col1:
    st.image(image)
    st.write("")
with col2:
    st.title('Bag Hunter')
    st.subheader('An image classification app to predict bags brand based on Farfetch.com bi-weekly update database')
    #st.write('A simple image classification web app to predict Cat-Dog-Wildlife faces with sounds effect ON')
    st.write("")
with col3:
    st.write("")




st.title("Bag Hunter is at your service")
st.subheader('⬇  Show me your bag    ⬇')
#st.write("An image classification app to predict bag's brand based on Farfetch.com weekly update database")
st.write("5 brands available now - ** Gucci, Hermès, Louis Vuitton, Prada, YSL** - more brands coming soon! ")




#st.sidebar.<widget>
    #a = st.sidebar.radio('R:',[1,2])

################
##    Image   ##
################


def import_and_predict(image_data, model):

        size = (150,150)    #
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(150, 150),    interpolation=cv2.INTER_CUBIC))/255.

        img_reshape = img_resize[np.newaxis,...]

        prediction = model.predict(img_reshape)

        return prediction

#############################


#############################
# st.write(" Bag Hunter is at your service. Show me your bag ")
uploaded_file = st.file_uploader(" ", type=['jpg','png','jpeg'])  #put your bag here


if uploaded_file is not None:

    u_img = Image.open(uploaded_file)
    #st.success("Success")
    st.image(u_img, 'Uploaded Image', use_column_width=True)
    #show.image(u_img, 'Uploaded Image', use_column_width=True)
    #st.image(image, use_column_width=True)

    prediction = import_and_predict(u_img, model)

    if np.argmax(prediction) == 0:
        Gucci = '<p style="color:Blue; font-size: 30px;">Gucci Bag</p>'
        st.markdown(Gucci, unsafe_allow_html=True)

    elif np.argmax(prediction) == 1:
        Hermès = '<p style="color:Blue; font-size: 30px;">Hermès Bag</p>'
        st.markdown(Hermès, unsafe_allow_html=True)

    elif np.argmax(prediction) == 2:
        LV = '<p style="color:Blue; font-size: 30px;">LV Bag</p>'
        st.markdown(LV, unsafe_allow_html=True)

    elif np.argmax(prediction) == 3:
        Prada = '<p style="color:Blue; font-size: 30px;">Prada Bag</p>'
        st.markdown(Prada, unsafe_allow_html=True)

    else:
        YSL = '<p style="color:Blue; font-size: 30px;">YSL Bag</p>'
        st.markdown(YSL, unsafe_allow_html=True)


    #st.text("Probability (0: Cat, 1: Dog, 2: Wildlife)")
    prob = '<p style=" color:Black; font-size: 20px;">Probability</p>'  # (0: Cat, 1: Dog, 2: Wildlife)  #font-family:sans-serif;
    st.markdown(prob, unsafe_allow_html=True)

    #st.write(("Gucci  "), round(prediction[0][0], 7))
    #st.write(("Hermès "),round(prediction[0][1], 7))
    #st.write(("LV     "),round(prediction[0][2], 7))
    #st.write(("Prada  "),round(prediction[0][3], 7))
    #st.write(("YSL    "),round(prediction[0][4], 7))



###################################
##   Clickable Graph             ##
###################################


    fig, ax = plt.subplots()

    #ax.hist(data['PRICE'])
    #ax.set_title('Distribution of House Prices in $100,000s')
    height = [prediction[0][0], prediction[0][1], prediction[0][2], prediction[0][3], prediction[0][4]]
    bars = ('Gucci','Hermès','LV','Prada', 'YSL')
    x_pos = np.arange(len(bars))



    #ax.bar(x_pos, height, color=['red', 'green', 'blue', 'orange', 'yellow'])
    ax.bar(x_pos, height, color=['cyan', 'orange', 'brown', 'olive', 'gray'])
    #ax.set_xticklabels(bars, minor =False)
    ax.set_xticks(x_pos) #, bars)
    ax.set_xticklabels(['Gucci','Hermès','LV','Prada', 'YSL'])

    show_graph = st.checkbox('Show Graph', value=True)

    if show_graph:
        st.pyplot(fig)




#########################
##   Update Database   ##
#########################


# Initialize connection.
client = pymongo.MongoClient()

# Pull data from the collection.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def get_data():
    db = client.fashion
    items = db.product.find({'shortDescription': {'$regex' : "bag"}}, {'_id':0, 'id':1, 'shortDescription':1, 'images.cutOut':1})
    items = list(items)  # make hashable for st.cache
    return items

items = get_data()

# Print results.
for item in items:
    st.write(f"{item['id']} has a :{item['shortDescription']}:")
