#flask is more customizable than streamlit  , but streamlit can build basic apps
#how to run streamlit => streamlit run filename.py => in terminal
import time
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

#python
data = pd.read_csv("./Dataset/India data .csv")
state_list = list(sorted(data['State name'].unique()))
state_list.insert(0,'Overall India')
primary_col =sorted(['Female Literacy Rate',
 'Female_SC',
 'Female_ST',
 'Female_Workers',
 'Graduate_Education','Male Literacy Rate',
 'Male_SC',
 'Male_ST', 'Households_with_Internet','Housholds_with_Electric_Lighting',
 'Male_Workers' , 'Literacy Rate', 'Illiterate_Education','Age not stated',
 'Age_Group_0_29',
 'Age_Group_30_49',
 'Age_Group_50',
 'Agricultural_Workers'])
#primary_col.insert(0,'Nothing')
secondary_col = sorted( [
  'Agricultural_Workers',
 'Below_Primary_Education',
 'Buddhists',
 'Christians',
 'Condition_of_occupied_census_houses_Dilapidated_Households',
 'Cultivator_Workers',
  'Households_with_Bicycle',
 'Households_with_Car_Jeep_Van',
 'Households_with_Computer',
 'SC',
 'ST', 'Jains',
 'Secondary_Education',
 'Sikhs','Muslims'
 'Households_with_Radio_Transistor','Urban_Households',
 'Workers'
 'Households_with_Scooter_Motorcycle_Moped',
 'Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car',
 'Households_with_Telephone_Mobile_Phone',
 'Households_with_Telephone_Mobile_Phone_Both',
 'Households_with_Telephone_Mobile_Phone_Landline_only',
 'Households_with_Telephone_Mobile_Phone_Mobile_only',
 'Households_with_Television',
 'Households_with_separate_kitchen_Cooking_inside_house','Location_of_drinking_water_source_Away_Households',
 'Location_of_drinking_water_source_Near_the_premises_Households',
 'Location_of_drinking_water_source_Within_the_premises_Households',
])
#secondary_col.insert(0,'Nothing')

#DISPLAY  MEDIA
# st.image("imagename_path")
# st.video("videoname_path")

#CREATING LAYOUTS
st.sidebar.title("India's Analysis")
state_select = st.sidebar.selectbox('select a state',state_list)
primary_select = st.sidebar.selectbox('select Primary Parameter',primary_col)
secondary_select = st.sidebar.selectbox('select a Secondary Parameter',secondary_col)
plot = st.sidebar.button("Plot")
st.text("Size represents primary Parameter")
st.text("Colorrepresents secondary Parameter")
if plot:
 if state_select=='Overall India':
  fig = px.scatter_mapbox(data,lon ="Longitude",lat="Latitude",zoom=3,mapbox_style="carto-positron",
                          width=800, height=600,size =primary_select,color = secondary_select,size_max=20)
  st.plotly_chart(fig , use_container_width=True)
 else:
  dt = data[data['State name']==state_select]
  fig = px.scatter_mapbox(dt, lon="Longitude", lat="Latitude", zoom=3,size =primary_select, width=800,
                          height=600,color = secondary_select, mapbox_style="carto-positron",size_max=20)
  st.plotly_chart(fig , use_container_width=True)


# st
#  #show status
# st.error("error")
# st.success("success")
# st.warning("warning")
# bar = st.progress(0)
# for i in range(0,100):
#  time.sleep(0.1)
#  bar.progress(i)
#
#  #taking user input
# input1 = st.text_input("enter some text")
# input2 = st.number_input("enter some text")
# input3 = st.date_input("enter some text")
# #buttons -. baloons
# btn = st.button("button")
# if btn:
#  st.success("success")
#  st.balloons # baloons aate h scrren pr
# else:
#  st.error("error")
#
# select_  = st.selectbox("select option",["a","b","c","d"])
#
# #file uploader
# file = st.file_uploader("upload csv file")
# if file is not None:
#    st.success("success")
