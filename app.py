import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

with st.sidebar :
    selected = option_menu ('LUAS BIDANG DATAR',
    ['Hitung Luas Layang-Layang',
     'Hitung Luas Trapesium'],
    default_index=0)

if (selected == 'Hitung Luas Layang-Layang') :
    st.title('Luas Layang-Layang')

    Diagonal1 = st.number_input ("Masukkan Nilai Diagonal ke Satu", 0)
    Diagonal2 = st.number_input ("Masukkan Nilai Diagonal ke Dua", 0)
    Hitung = st.button ('Hitung')

    if Hitung :
        Luas = 0.5 * Diagonal1 * Diagonal2
        st.write ("Hasil Luas Layang-Layang = ", Luas)

if (selected == 'Hitung Luas Trapesium') :
    st.title('Luas Trapesium')

    Sisi1 = st.number_input ("Masukkan Nilai Sisi ke Satu", 0)
    Sisi2 = st.number_input ("Masukkan Nilai Sisi ke Dua", 0)
    Tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
    Hitung = st.button ('Hitung')

    if Hitung :
        luas = 0.5 * (Sisi1 + Sisi2) * Tinggi
        st.write ("Hasil Luas Trapesium = ", luas)