#for ml model
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



#from data import save_uploaded_file, load_data


#for data vizualization
import altair as alt
import plotly.express as px

input_file_path = 'incident_sla-2324-onwards_715.csv'
#incident_sla-051524-1850
#incident_sla-2324-onwards_715
#incident_230630_240111

loaded_model = pickle.load(open('new_trained_model.pkl', 'rb'))

input_data = pd.read_csv(input_file_path, encoding='latin1').apply(lambda x: x.astype(str)).rename(columns={'problem_id.u_component': 'problem_component', 'inc_short_description': 'short_description'})


    # Fit the model and obtain topics and probabilities
docs_processing = input_data['short_description']
topics, probs = loaded_model.fit_transform(docs_processing)


    # Get topic information
result = loaded_model.get_topic_info()

print(result)