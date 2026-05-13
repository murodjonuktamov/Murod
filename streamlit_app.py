import streamlit as st
import ee
import geemap.foliumap as geemap

st.set_page_config(layout="wide")
st.title("Google Earth Engine + Streamlit Xaritasi 🌍")

# GEE xizmatiga ulanish (Avtomatlashtirilgan)
try:
    ee.Initialize()
except Exception as e:
    st.error("GEE autentifikatsiya xatosi. 'Secrets' qismini tekshiring.")

# Xarita yaratish
m = geemap.Map(center=[41.31, 69.24], zoom=6) # Toshkent markazi

# GEE ma'lumotlar to'plamini qo'shish (Masalan: ESA Yer qoplami)
dataset = ee.ImageCollection("ESA/WorldCover/v100").first()
visualization = {'bands': ['Map']}
m.addLayer(dataset, visualization, 'Yer qoplami (ESA)')

# Xaritani Streamlit'da ko'rsatish
m.to_streamlit(height=700)
