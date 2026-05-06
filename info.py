#flask is more customizable than streamlit  , but streamlit can build basic apps
#how to run streamlit => streamlit run filename.py => in terminal
import time
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


st.title("Project-3 using Streamlit")
st.header("basics")
st.subheader("basics-2")
st.write("this is the normal text")
st.markdown(""" 
### triple hash means third level heading and
 # # is first level important
 these commas used for multi line strings and 
markdown is for list
""")

st.code("""
def fun():
    print9"we can write any language code here
fun();
""")

st.latex('x^2 + y^2 = 0') # used to expres smathematical statement
#DISPLAY ELEMENTS


dt = pd.DataFrame({
 "name" : ["a","b","c","d"],
 "marks":[1,2,3,4],
 "package":[10,28,45,20]
})
st.dataframe(dt)
st.metric("line1","line2",'line3')
st.json({
 "name": ["a", "b", "c", "d"],
 "marks": [1, 2, 3, 4],
 "package": [10, 28, 45, 20]
})

#DISPLAY  MEDIA
# st.image("imagename_path")
# st.video("videoname_path")

#CREATING LAYOUTS
st.sidebar.title("India's Analysis")
st.sidebar.selectbox('select a state')
st.sidebar.selectbox('select Primary Parameter')
st.sidebar.selectbox('select a Secondary Parameter')
st.sidebar.button("Plot")


col1,col2  =st.columns(2)
with col1:
 st.write("col1 content ffffffffffffffffff")
with col1:
 st.write("col2 content fffffffffffffff")

 #show status
st.error("error")
st.success("success")
st.warning("warning")
bar = st.progress(0)
for i in range(0,100):
 time.sleep(0.1)
 bar.progress(i)

 #taking user input
input1 = st.text_input("enter some text")
input2 = st.number_input("enter some text")
input3 = st.date_input("enter some text")
#buttons -. baloons
btn = st.button("button")
if btn:
 st.success("success")
 st.balloons # baloons aate h scrren pr
else:
 st.error("error")

select_  = st.selectbox("select option",["a","b","c","d"])

#file uploader
file = st.file_uploader("upload csv file")
if file is not None:
   st.success("success")
