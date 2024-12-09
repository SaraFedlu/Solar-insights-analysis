import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../data/processed/final_dataset_benin.csv')

# Title
st.title('Interactive Data Dashboard')

# Data Size Slider
data_size = st.slider('Select data size', min_value=10, max_value=100, value=50)
st.write(f"Displaying {data_size} rows of data")
st.write(data.head(data_size))

# Select Plot Type
plot_type = st.selectbox('Select plot type', ['Scatter Plot', 'Line Plot'])
if plot_type == 'Scatter Plot':
    st.subheader('Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(data['GHI'], data['Tamb'])
    ax.set_xlabel('GHI')
    ax.set_ylabel('Tamb')
    st.pyplot(fig)
elif plot_type == 'Line Plot':
    st.subheader('Line Plot')
    st.line_chart(data['GHI'])