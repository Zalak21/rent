import pandas as pd
import numpy as np
import streamlit as st
import base64
import pickle
import bz2
import _pickle as cPickle
rf = bz2.BZ2File('Regressor.pbz2', 'rb')
rf = cPickle.load(rf)

def predict_rent_price(bathrooms, bedrooms, longitude, latitude):
    prediction = rf.predict([[bathrooms, bedrooms, longitude, latitude]])
    return round(prediction[0], 2)
def main():
    st.title("Rent price predictor")
    bedrooms = st.selectbox(label = "Choose the number of bedrooms", options = [0,  1,  2, 3, 4, 5 , 6, 7, 8])
    bathrooms = st.selectbox(label = "Choose the number of bathrooms", options = [0,  1,  2, 3, 4, 5 , 6, 7, 8, 9, 10])
    longitude = st.slider("Longitude", min_value= -74.10, max_value= -73.67, step= 0.01)
    latitude = st.slider("Latitude", min_value= 40.55, max_value= 40.94, step= 0.01)
    result = ""
    with open('rent.jpg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    if st.button("Predict"):
        result= predict_rent_price(bathrooms, bedrooms, longitude, latitude)
    st.success('The price for this apartment is $ {}'.format(result))
if __name__ == '__main__':
    main()