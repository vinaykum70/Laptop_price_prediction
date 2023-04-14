import streamlit as st
import pickle
import numpy as np
import pandas as pd


model = pickle.load(open("model.pkl","rb"))

dt = pickle.load(open("dt.pkl","rb"))

st.title("Laptop Price Prediction")

brand = st.selectbox('Brand Name', (dt['Brand Name'].keys()))

os = st.selectbox('Operating System',(dt['OS'].keys()))

ram_type = st.selectbox('RAM Type',(dt['RAM Type'].keys()))

ram_size = st.selectbox('RAM Size',(4,8,16,32))

processor = st.selectbox('Processor',(dt['Processor'].keys()))

warranty = st.selectbox('Warranty',(1,2))

disk_type = st.selectbox('Disk Type',(dt['Disk Type'].keys()))

disk_size = st.selectbox('Disk Size',(32,64,128,256,512,1024,2048))

value = [dt['Brand Name'][brand], dt['OS'][os], dt['RAM Type'][ram_type], int(ram_size), 
        dt['Processor'][processor], int(warranty), dt['Disk Type'][disk_type], int(disk_size) ]

price = model.predict([value])


st.write("\n Approximately Price of the Laptop is : ", int(np.round(price[0])))