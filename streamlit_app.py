import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
def ShowAnimation(name, URL):
    anim=load_lottie_url(URL)
    st_lottie(anim, key = name)
    
st.markdown('# Animations: https://lottiefiles.com/recent') 
st.markdown("### Animate with JSON, SVG, Adobe XD, Figma, and deploy to web, mobile as tiny animation files ")

ShowAnimation("Graph","https://assets6.lottiefiles.com/packages/lf20_4gqhiayj.json")
ShowAnimation("PhoneBot","https://assets9.lottiefiles.com/packages/lf20_zrqthn6o.json")
ShowAnimation("SupportBot","https://assets5.lottiefiles.com/private_files/lf30_cmd8kh2q.json")
ShowAnimation("ChatBot","https://assets8.lottiefiles.com/packages/lf20_j1oeaifz.json")
ShowAnimation("IntelligentMachine","https://assets8.lottiefiles.com/packages/lf20_edouagsj.json")
ShowAnimation("GearAI","https://assets10.lottiefiles.com/packages/lf20_3jkp7dqt.json")
ShowAnimation("ContextGraph","https://assets10.lottiefiles.com/private_files/lf30_vwC61X.json")
ShowAnimation("Yggdrasil","https://assets4.lottiefiles.com/packages/lf20_8q1bhU.json")
ShowAnimation("Studying","https://assets9.lottiefiles.com/packages/lf20_6ft9bypa.json")

