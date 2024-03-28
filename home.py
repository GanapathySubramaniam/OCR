import streamlit as st
from helpers.streamlit_helper import streamlit_session,load_lottie_animation
from  PIL import Image
import base64
import plotly.express as px

df = px.data.iris()

@st.cache_data 
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("wallpaper3.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 210%;
background-position: top left;
background-repeat: repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
def ui():
    buttons=[]
    session_obj=streamlit_session(buttons)
    col1,col2 =st.columns(2)
    with col1:
        st.header('Welcome to the CogniVix')
        st.write('The app which gives life to textual images!')
    with col2:
        load_lottie_animation('lottie_jsons\scanning_image.json')
    st.write('Instructions')
    st.write('Upload an Image to proceed')
    col1,col2=st.columns(2)
    with col1:
        img_file = st.file_uploader("Please choose an image file")
        #temperature=st.slider('Temperature',min_value=0.0,max_value=1.0,step=0.05,value=0.5)
    if st.button('Start Scanning'):
        #st.code('Your function goes here')
        #image = Image.open(img_file)
        #st.image(image)
        text_val=your_function(image_var) # this function should return the text
        st.code(text_val)
        st.balloons()
    st.write('Contact Us:')
    col1,col2=st.columns(2)
    with col1:
        st.write(f'Ganapathy Subamaniam Sundar')
    with col2:
        st.write('Email')
        st.code('ganapathysubramaniam1999@gmail.com')
        url='https://www.linkedin.com/in/ganapathy-subramaniam-sundar-b08aa222b/'
        st.write('Connect with me in [linkedIn](%s)'%url)
    page_bg_img = '''
                <style>
                body {
                background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
                background-size: cover;
                }
                </style>
                '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

ui()
