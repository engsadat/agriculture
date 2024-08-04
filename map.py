import pandas as pd
import streamlit as st

# Sample data
data = {
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060],
}
df = pd.read_excel('xy2.xlsx')

# Display the map with the DataFrame
st.map(df, use_container_width=True)
