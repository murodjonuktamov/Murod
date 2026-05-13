import streamlit as st
import pandas as pd
import numpy as np

# Sahifa sarlavhasi
st.set_page_config(page_title="Mening Birinchi Ilovam", page_icon="🚀")

st.title("Xush kelibsiz! 👋")
st.write("Bu mening Streamlit orqali yaratilgan birinchi dasturim.")

# Oddiy jadval yaratish
st.header("Tasodifiy ma'lumotlar jadvali")
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A ustun', 'B ustun', 'C ustun']
)
st.dataframe(data)

# Grafika chizish
st.header("Grafik ko'rinishi")
st.line_chart(data)

# Foydalanuvchi bilan aloqa
ismlar = st.text_input("Ismingizni kiriting:")
if ismlar:
    st.success(f"Salom, {ismlar}! Ilova muvaffaqiyatli ishlamoqda.")
