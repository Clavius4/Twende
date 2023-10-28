import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import matplotlib.cm as cm
from tensorflow.keras.layers.experimental import preprocessing
from tensorflow import keras
from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from tensorflow.keras.optimizers import Adam

# Title of the app
st.title("Twende an AI model for predicting cost of an event")


text1 = st.text_input("Event name", value="")

text2 = st.text_input("Location", value="")

text3 = st.text_input("Venue cost", value="")

text4 = st.text_input("Number of Facilitators", value="")

text5 = st.text_input("Equipments Cost", value="")

text6 = st.text_input("Food and Beverage Cost", value="")

text7 = st.text_input("Accommodations Cost", value="")

text8 = st.text_input("Marketing and Advertising Cost", value="")

text9 = st.text_input("Duration(days)", value="")

text10 = st.text_input("Transportation&Communication Cost", value="")

text11 = st.text_input("Guest of honor Cost", value="")
text12 = st.text_input("Staff&Volunteer Expenses", value="")
text13 = st.text_input("Insurance Cost", value="")

text14 = st.text_input("Miscellaneous Expenses", value="")

if st.button("Process"):
#         "Arusha","Dar-es-salaam","Dodoma","Geita","Iringa","Kagera","Katavi","Kigoma","Kilimanjaro","Manyara","Mbeya","Morogoro","Mwanza","Pwani","Rukwa","Singida","Songea","Tabora","Tanga","Zanzibar"
        # Create a dictionary to store the input values "Dar es Salaam Startup","Pitch Night Tanzania", "Pitch Night Tanzania","STEM Education and Innovation Conference","STEM for Girls Workshop","Tanzania Entrepreneurship Summit","Tanzania Fashion Week","Tanzania Food Festival","Tanzania Science Fair","Tanzania Tech Summit","The Education Summit","The Innovation Week","Twende Build It","Twende CCB","Twende Cultural Week","Twende Environmental Expo","Twende Farmers week","Twende Jamii Tech Incubation Program","Twende STEM Outreach","Twende kumasi"
         data = {"Event name":[text1],
                "Location":[text2],
                "Venue cost": [text3],
                "Number of Facilitators": [text4],
                "Equipments Cost": [text5],
                "Food and Beverage Cost": [text6],
                "Accommodations Cost": [text7],
                "Marketing and Advertising Cost": [text8],
                "Duration(days)": [text9],
                "Transportation&Communication Cost": [text10],
                "Guest of honor Cost": [text11],
                "Staff&Volunteer Expenses": [text12],
                "Insurance Cost":[text13],
                "Miscellaneous Expenses": [text14]}
        
         data_frame = pd.DataFrame(data)
         data_frame['Event name'] = pd.factorize(data_frame['Event name'])[0]
         data_frame['Location'] = pd.factorize(data_frame['Location'])[0]
               
         loaded_model = tf.keras.models.load_model('Twende/assets')
         data_frame=np.array(data_frame).astype('float32')
     
#         # make predictions on new data
         predict = loaded_model.predict(data_frame)
        
         string = "Estimated Cost is: "
         number=  predict[0][0]
         result = f"{string}{number} TSH"   
         st.write(f"**{result}**") 
  
             
    
