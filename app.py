import streamlit as st
from helper import streamlit_session,load_lottie_animation
from  PIL import Image
import base64
import plotly.express as px
import pytesseract
from PIL import Image as PImage
import time
from collections import Counter


def generate_data(data):
    for i in data:
        yield f"{i}"
        time.sleep(0.05)  # Simulate some processing time



def read_image(img_file):
    return Image.open(img_file)

def get_text(image):
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    return str(pytesseract.image_to_string(image))


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
        load_lottie_animation('./lottie_jsons/scanning_image.json')
    st.write('Instructions')
    st.write('Upload an Image to proceed')
    col1,col2=st.columns(2)
    with col1:
        img_file = st.file_uploader("Please choose an image file")

    if st.button('Start Scanning'):
        image = read_image(img_file)
        st.image(image)
        text_val=get_text(image)
        with st.expander("Expand me!"):
            st.write_stream(generate_data(text_val))
            if st.download_button(
                            label="Download",
                            data=text_val,
                            file_name='my_data.txt',
                            mime='text/plain'
                            ):
                st.write('Thanks for downloading!!')
        
    st.write('Contact Us:')
    col1,col2=st.columns(2)
    with col1:
        names=['Ganapathy Subamaniam Sundar','Kapileshvar A P','Ritish Madaan','Rajat Kumar','Hetal Prajapati']
        emails=['c0908063@mylambton.ca','kapileshvarap@gmail.com','c0912858@mylambton.ca','c0908005@mylambton.ca','c0911591@mylambton.ca']

        for name,email in zip(names,emails):
            st.write(name)
            st.code(f'{email}')
        #url='https://www.linkedin.com/in/ganapathy-subramaniam-sundar-b08aa222b/'
        #     st.write('Connect with me in [linkedIn](%s)'%url)
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
