import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_excel('2024-08-03_xy_wadiAbha_correct.xlsx')

st.map(data=df, latitude=lat, longitude=lon, color=None, size=None, zoom=None, use_container_width=True)
