import os
import streamlit as st 
import pickle
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

# Note: Make sure that you have installed "requirements.txt"



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
        page_title="Incident Clustering Analysis Tool",
        page_icon = ":computer:",
        layout='wide'
    )

    st.sidebar.info("**Hello!** Welcome to the Incident Clustering Analysis Tool - ICAT! This tool was created as an aid to improve problem management of SNOW incident tickets! Get started by uploading a CSV file!",  icon="👋")

    st.sidebar.divider()

    st.sidebar.subheader("📥 Upload a CSV file")

    uploaded_file = st.sidebar.file_uploader(
        ":green[*Please ensure that the file is in **CSV** format and the first row has column names.*]", type="csv")


    # Main page content
    st.header(":computer: Incident Clustering Analysis Tool", divider = 'gray')
   
    # Processing the file
    if uploaded_file: 
        file_df = pd.read_csv(uploaded_file, encoding='latin1').apply(lambda x: x.astype(str)).rename(columns={'problem_id.u_component': 'problem_component', 'inc_short_description': 'short_description'})
        
        if st.sidebar.button("Run Model"):

                with st.status(":orange[**Analyzing data...**]", expanded=True) as status:
                    st.caption("*Preparing data...*")
                    time.sleep(2)
                    st.caption("*Loading Model...*")
                    time.sleep(1)
                    st.caption("*Clustering data...*")
                    topics, probs, result = process_model(file_df)
                    status.update(
                    label=":green[**Analysis Complete!**]", state="complete", expanded=False
                    )

                
                # Display the result
                st.write(result)
    
                
if __name__ == "__main__":
    main()