import streamlit as st
from helpers.streamlit_helper import streamlit_session,load_lottie_animation
from  PIL import Image
import base64
import plotly.express as px
import pytesseract
from PIL import Image as PImage


def get_text(image):
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    return pytesseract.image_to_string(image)


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
        st.write('lottie')
        #load_lottie_animation('lottie_jsons\scanning_image.json')
    st.write('Instructions')
    st.write('Upload an Image to proceed')
    col1,col2=st.columns(2)
    with col1:
        img_file = st.file_uploader("Please choose an image file")

    if st.button('Start Scanning'):
        image = Image.open(img_file)
        st.image(image)
        text_val=get_text(image)
        st.code(text_val)
        st.balloons()
    st.write('Contact Us:')
    col1,col2=st.columns(2)
    with col1:
        names=['Ganapathy Subamaniam Sundar','Kapileshvar A P','Rajat Kumar','Hetal Prajapati']
        for name in names:
            st.write(name)
    with col2:
        emails=['c0908063@mylambton.ca','kapileshvarap@gmail.com','c0912858@mylambton.ca','c0908005@mylambton.ca','c0911591@mylambton.ca']
        st.write('Email')
        for email in emails:
            st.code(email)
        #url='https://www.linkedin.com/in/ganapathy-subramaniam-sundar-b08aa222b/'
        #     st.write('Connect with me in [linkedIn](%s)'%url)
        # page_bg_img = '''
        #             <style>
        #             body {
        #             background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
        #             background-size: cover;
        #             }
        #             </style>
        #             '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

ui()
