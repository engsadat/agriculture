import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_excel('2024-08-03_xy_wadiAbha_correct.xlsx')

st.map(df)