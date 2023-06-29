# Phonepe Pulse Data Visualization and Exploration:A User-Friendly Tool Using Streamlit and Plotly
## Problem Statement:
   The Phonepe pulse Github repository contains a large amount of data related to
various metrics and statistics. The goal is to extract this data and process it to obtain
insights and information that can be visualized in a user-friendly manner.

## The solution must include the following steps:
1. Extract data from the Phonepe pulse Github repository through scripting and
clone it..
2. Transform the data into a suitable format and perform any necessary cleaning
and pre-processing steps.
3. Insert the transformed data into a MySQL database for efficient storage and
retrieval.
4. Create a live geo visualization dashboard using Streamlit and Plotly in Python
to display the data in an interactive and visually appealing manner.
5. Fetch the data from the MySQL database to display in the dashboard.
6. Provide at least 10 different dropdown options for users to select different
facts and figures to display on the dashboard.

The solution must be secure, efficient, and user-friendly. The dashboard must be
easily accessible and provide valuable insights and information about the data in the
Phonepe pulse Github repository.
## Introduction about Phonepe Pulse:
The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data.
When PhonePe started 5 years back, we were constantly looking for definitive data sources on digital payments in India. Some of the questions we were seeking answers to were - How are consumers truly using digital payments? What are the top cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes?
This year as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments in India.
PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.

## Details about library's and modules used in this project:
### OS :
After importing the os module, you can use its functions and attributes by prefixing them with os.. 

### Json :
JavaScript Object Notation (JSON) is a standardized format commonly used to transfer data as text that can be sent over a network. It's used by lots of APIs and Databases, and it's easy for both humans and machines to read. JSON represents objects as name/value pairs, just like a Python dictionary.

### pandas:
Pandas is an open-source library that is made mainly for working with relational or labeled data both easily and intuitively. It provides various data structures and operations for manipulating numerical data and time series. This library is built on top of the NumPy library. Pandas is fast and it has high performance & productivity for users.
### MYSQL:
MySQL is a widely used relational database management system (RDBMS).MySQL is free and open-source.
MySQL is ideal for both small and large applications.
### Streamlit:
Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. It is a Python-based library specifically designed for machine learning engineers.

### Plotly:
Plotly provides online graphing, analytics, and statistics tools for individuals and collaboration, as well as scientific graphing libraries for Python, R, MATLAB, Perl, Julia, Arduino, JavaScript and REST.

## Explanation about Phonepe_pulse API:
### Import necessary libraries and modules:
~~~ python
import os
import json
import pandas as pd
import streamlit as st
import pandas as pd
import json
import mysql.connector as con
import plotly.express as px
~~~

### 1.Data Extraction:
Clone the phonepe pulse github repository and extract the all needed data from the repository.Transform the data into necessary format using data cleaning and preprocessing methods.
Create the dataframe and convert the data into csv format.

### 2.MYSQL data conversion:
Store the data in MYSQL server for better access and usage of dataframe.Following code will be helps to create the MYSQL data base.
~~~python
import mysql.connector as con
mydb = con.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Sep@2809"
    )

mycursor = mydb.cursor(buffered=True)

mycursor.execute("CREATE DATABASE IF NOT EXISTS Phonepe")
mycursor.execute("USE Phonepe")
~~~

### 3.Dashboard creation:
Using Streamlit and Plotly libraries in python to create the Phonepe_Pulse dashboard from extracted data of MYSQL database.
Using of MYSQL database will be easily accessible for data's.

Some examples of data visualizasion using Phonepe_pulse dashboard:

![Bar chart 2](https://github.com/dineshdilip2/Phonepe_pulse/assets/119442550/6b4aa49b-47fe-4a7a-8c86-76aac1e5411a)

![Pie Chart](https://github.com/dineshdilip2/Phonepe_pulse/assets/119442550/6ef8b83c-134e-4337-8d11-8f7166832ee6)

![Pie chart 2](https://github.com/dineshdilip2/Phonepe_pulse/assets/119442550/211832c0-b1fc-4161-983c-93e1171f2d6d)


