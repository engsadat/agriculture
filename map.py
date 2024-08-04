import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_excel('xy.xlsx')

st.map(latitude=latitude, longitude = longitude, use_container_width=True)
