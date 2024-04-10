import streamlit as st
from streamlit_lottie import st_lottie
import json 

def load_lottie_animation(lottie_json_path):
    with open(lottie_json_path,'r') as lottie_json:
        st_lottie(json.load(lottie_json))

class streamlit_session:
    def __init__(self,buttons):
        self.buttons=buttons
        for btn in self.buttons:
            self.add_to_session_state(btn,False)
    def callback(self,button_name):
        st.session_state[button_name]=True

    def add_to_session_state(self,key,value):
        if key not in st.session_state.keys():
            st.session_state[key]=value

        

   
