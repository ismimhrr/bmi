import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Tentukan URL untuk file animasi Lottie
url = "https://assets5.lottiefiles.com/packages/lf20_zdtmnqvo.json"

# Muat file animasi Lottie dari URL
response = requests.get(url)
animation = response.json()

# Tampilkan animasi Lottie dan teks di sampingnya
st.markdown(
    """
    <style>
    .lottie-text-container {
        display: flex;
        align-items: center;
    }
    .lottie-container {
        width: 50%;
        height: auto;
        margin-right: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class='lottie-text-container'>
        <div class='lottie-container'>
            {st_lottie(animation)}
        </div>
        <div>
            <h2>Judul teks</h2>
            <p>Deskripsi teks</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
