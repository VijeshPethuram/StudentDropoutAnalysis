# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:08:53 2023

@author: Vijesh Pethuram K
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('dataset.csv')
df=df.iloc[:1000]
#df['Target'].replace('Enrolled','Graduate',inplace=True)
st.title("Welcome to Dropout Analysis 📈")
# Calculate the dropout rate

#dropouts=df['Target'].value_counts()['Dropout']
#dropout_rate = dropouts/1000;
# Calculate the number of dropouts, enrolled students, and graduates
#dropout_count = df['Target'].value_counts()['Dropout']
#enrolled_count = df['Target'].value_counts()['Enrolled']
#graduate_count = df['Target'].value_counts()['Graduate']

# Calculate the percentage of dropouts, enrolled students, and graduates
#dropout_percentage = dropout_count / (dropout_count + enrolled_count + graduate_count) * 100
#enrolled_percentage = enrolled_count / (dropout_count + enrolled_count + graduate_count) * 100
#graduate_percentage = graduate_count / (dropout_count + enrolled_count + graduate_count) * 100

st.subheader("\tDropout Analysis based on Age Groups 📈")
st.subheader("")
x = df['Target']
y = df['Age at enrollment']

plt.bar(x,y)

plt.xlabel('Status')
plt.ylabel('Age')

plt.title('Dropout by Age Groups')

st.pyplot(plt.gcf())

st.markdown("------")


st.header("Customized Student Dropout Analysis 📈")
st.subheader("")
st.dataframe(df)
colum=list(df.columns)
target=st.selectbox('Choose a target: ',colum)
col2=colum.copy()
col2.remove(target)
x_var=st.selectbox('Choose a X variable: ',col2)
y_var=st.selectbox('Choose a Y variable: ',col2)

fig=px.scatter(df,x=x_var,y=y_var,color=target)
st.plotly_chart(fig)


