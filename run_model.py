import os
import streamlit as st 
import pickle

#install ff in terminal 
# !pip install openpyxl
# pandas need openpyxl to read excel file, if your file is in excel
# !pip install pandas
# !pip install sentence-transformers
# !pip install bertopic
# !pip install ipython
# !pip install streamlit
# may take around 30 seconds. will output requirement already satisfied or installed successfully when final


import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from bertopic import BERTopic
from umap import UMAP
from sklearn.cluster import KMeans
from sklearn import svm 
from hdbscan import HDBSCAN
from sklearn.feature_extraction.text import CountVectorizer
from torch import bfloat16
import transformers
import requests
import time
import pickle



# Calling the model
def process_model(input_file_path):
    # Load the file path

    input_data = input_file_path
    
    loaded_model = pickle.load(open('wms_incidents_model.pkl', 'rb'))
    
    # Fit the model and obtain topics and probabilities
    docs_processing = input_data['short_description']
    topics, probs = loaded_model.fit_transform(docs_processing)

    # Get topic information
    result = loaded_model.get_topic_info()

    # Save the model
    # pickle.dump(loaded_model, open('wms_incidents_model.pkl', 'wb'))

    return topics, probs, result


def main():

    st.set_page_config(
        page_title="WMS Incident Analysis Clustering",
        page_icon = ":computer:",
        layout='wide'
    )

    st.sidebar.subheader("📥 Upload a CSV file")
    st.sidebar.markdown(":green[*Please ensure the first row has the column names.*]")
    uploaded_file = st.sidebar.file_uploader("", accept_multiple_files=False, type="csv")

    # Main page content
    st.title("Incident Clustering App")

    if uploaded_file: 
        file_df = pd.read_csv(uploaded_file, encoding='latin1').apply(lambda x: x.astype(str)).rename(columns={'problem_id.u_component': 'problem_component', 'inc_short_description': 'short_description'})
        if st.sidebar.button("Run Model"):
            # Spinner loader
                with st.spinner("Operation in progress. Please wait."):
                    # Process the model
                    topics, probs, result = process_model(file_df)

                # Display the result
                st.write(result)
    
                
if __name__ == "__main__":
    main()