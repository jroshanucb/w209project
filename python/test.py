from flask import Flask,jsonify,request
import json
import pandas as pd
import numpy as np
import os

# from sklearn.cluster import KMeans
pd.set_option('display.float_format', lambda x: '{:.3f}'.format(x)) #limit floats output to 3
pd.set_option('display.max_columns', None) #display all columns in data frame
pd.set_option('display.max_rows', None)
import seaborn as sns
sns.set_context('talk')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# %matplotlib inline
# import googlemaps
from datetime import datetime
import math
from k_means_constrained import KMeansConstrained
import pyodbc 
# Get the file from front-end submission
# file = request.files['file']
# path = os.path.join(r'C:\Users\Sam.Shih\Desktop\SQL\For SQL\upload', file.filename)
# file.save(path)
# print('Successful upload:',file.filename)
# rawdatatable = pd.read_excel(path,sheet_name=1)

# Read the table from local storage
# path_local = r'.\excel\Store Master.xlsx'
# rawdatatable = pd.read_excel(path_local,sheet_name=1)
# rawdatatable.head()
# rawdatatable = pd.read_csv(r"..\csv\Berkeley_1000.csv")
# rawdatatable = pd.read_csv("../csv/Berkeley_1000.csv")
# rawdatatable = pd.read_csv(r'./Berkeley_1000.csv',encoding="ISO-8859-1")
# rawdatatable1 = pd.read_csv(r'./Berkeley_1000.csv')
rawdatatable = pd.read_csv(r'C:\IIIfinalproject\final project\python\Berkeley_1000.csv',header=None)
rawdatatable.columns = ['Latitude','Longitude','NUMBER','STREET','UNIT','CITY','DISTRICT','REGION','POSTCODE','ID','HASH']
print(rawdatatable)

# # Number of clusters (Number of working days)
# Target_Num_Cluster = 22
# print('Expected number of clusters:',Target_Num_Cluster)
# X_features = rawdatatable[['Longitude','Latitude']]

# # Size constraint K-means
# clf = KMeansConstrained(
# n_clusters=Target_Num_Cluster,
# size_min=11,
# size_max=13,
# random_state=0
# )
# clf.fit_predict(X_features)


# # Get the labels of each store
# Label_frame = pd.DataFrame(clf.labels_)
# # Get the number of store which allocate to certain clusters
# for i in range(Target_Num_Cluster):
#     print('Cluster',i,":",clf.labels_[clf.labels_==i].shape[0],'stores')

# Storeinfo = rawdatatable[['Storecode','Storename','Store_Address']]
# clustering_X_features = pd.concat([Storeinfo,X_features,Label_frame], axis=1)
# clustering_X_features = clustering_X_features.rename(columns={0 : 'Clusters'})
# clustering_X_features.head()

# dataset=[]
# for i in range(Target_Num_Cluster):
#     dataset.append({
#     'Clusters':i,
#     'datas':[]
#     })
#     clusters = clustering_X_features[clustering_X_features['Clusters']==i]
#     cluster_len = len(clusters)
    
#     for j in range(cluster_len):
#         LatLngObj = {'lat':clusters.iloc[j,:][3],'lng':clusters.iloc[j,:][4]}
#         dataset[i]['datas'].append({
#             'Storecode':clusters.iloc[j,:][0],
#             'Storename':clusters.iloc[j,:][1],
#             'Store_Address':clusters.iloc[j,:][2],
#             'Longitude':clusters.iloc[j,:][3],
#             'Latitude':clusters.iloc[j,:][4],
#             'LatLng':LatLngObj
#         })
#     # print(dataset)