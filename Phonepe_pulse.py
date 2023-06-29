# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:19:20 2023

@author: 91809
"""

#print(csv_file)

import streamlit as st
import pandas as pd
import json
import mysql.connector as con
import plotly.express as px


# To create the title and markdown options
st.title(":blue[Phonepe Pulse]")
st.markdown(":blue[Welcome to the Phonepe Pulse!!!PhonePe Pulse is a feature offered by PhonePe, which is one of the leading digital payment platforms in India. PhonePe Pulse provides users with insights and data related to their digital transactions and payment activities.]")
mydb = con.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Sep@2809",
    database="phonepe"
    )

mycursor = mydb.cursor(buffered=True)           


with st.sidebar:
    selected = st.selectbox("Select a page",["Top Performers","Explore Data"])
if selected =="Top Performers":
    st.markdown("##:violet[Top 10 performers]")
    Type = st.sidebar.selectbox("**Type**",("Transactions","Users"))
    if Type =="Transactions":
        Data_segmentation=st.sidebar.selectbox("**Data segmentation**",("State","District","Pincode"),key = "Data segmentation_selectbox")
        col1,col2= st.columns([1,1.5],gap="large")
        with col1:
            Year =st.slider("**Select the year**",min_value=2018,max_value=2022)
            Quarter= st.selectbox("**Select the Quarter",('1','2','3','4'),key='qgwe2' )
            
        with col2:
            st.write(
                """
                Using this pie chart,we will get know about the top three insights in transactions like State,District and Pincode.
                """
                )
            
            
        if Data_segmentation=="State":
               mycursor.execute(f"select state,sum(Transaction_count) as Total_Transactions_Count,sum(Transaction_amount) as Total_amount from agg_trans_sql where year = {Year} and quarter = {Quarter} group by state order by Total_amount desc limit 10")
               df = pd .DataFrame(mycursor.fetchall(),columns=['State','Transactions_Count','Total_Amount'])
               
               fig = px.pie(df,values='Transactions_Count',
                            names = 'State',
                            title="Top 10 Phonepe transaction according to States",
                            color_discrete_sequence= px.colors.sequential.Magenta,
                            hover_data = ['Total_Amount'],
                            labels = {'Total_Amount':'Total Amount'})
               
               fig.update_traces(textposition='inside',textinfo='percent+label')
               st.plotly_chart(fig,use_container_width=True)
        if Data_segmentation=="District":
               mycursor.execute(f"SELECT district,sum(Transaction_count) as Total_Count,sum(Transaction_amount) as Total_amount from map_trans_sql WHERE year ={Year} and quarter ={Quarter} GROUP BY district,state ORDER BY Total_amount DESC LIMIT 10")
               df = pd.DataFrame(mycursor.fetchall(),columns= ['District','Transactions_Count','Total_Amount'])
               
               fig = px.pie(df,values= 'Total_Amount',
                            names= 'District',
                            title='Top 10 Phonepe Transactions according to Districts',
                            color_discrete_sequence=px.colors.sequential.Magenta,
                            hover_data=['Transactions_Count'],
                            labels= {'Transactions_Count':'Transactions_Count'})
               
               
               fig.update_traces(textposition='inside',textinfo='percent+label')
               st.plotly_chart(fig,use_container_width=True)
               
        if Data_segmentation=="Pincode":
              
               mycursor.execute(f"select pincode, sum(Transaction_count) as Total_Transactions_Count,sum(Transaction_amount) as Total_amount from top_trans_sql where year ={Year} and quarter = {Quarter} group by pincode order by Total_amount desc limit 10")
               df = pd.DataFrame(mycursor.fetchall(),columns=['Pincode','Transactions_Count','Total_Amount'])
               fig = px.pie(df,values='Total_Amount',
                            names= 'Pincode',
                            title = 'Top Phonepe Transactions according to pincode',
                            color_discrete_sequence=px.colors.sequential.Magenta,
                            hover_data=['Transactions_Count'],
                            labels= {'Transactions_Count':'Transactions_Count'})
               fig.update_traces(textposition='inside',textinfo='percent+label')
               st.plotly_chart(fig,use_container_width=True)
               
               
    if Type=="Users":
       Data_segmentation=st.sidebar.selectbox("**Data segmentation**",("Brands","Registered_User","Appopeners"),key="Data segmentation_selectbox")
       col1,col2 = st.columns([1,1.5],gap='large')
       with col1:
           Year = st.slider("**Select the Year**",min_value=2018,max_value=2022)
           Quarter = st.selectbox('**Select the Quarter**',('1','2','3','4'),key='quat')
           
       with col2:
           st.write(
               """
               By accessing this donut chart, we will get to know about the top three insights in Users like Brands,Registered User, and Appopeners .
               """
               
               )
       if Data_segmentation == "Brands":
            
            mycursor.execute(f"select Brand,sum(Brand_count) as Total_Count,avg(Brand_percentage)*100 as Avg_Percentage from agg_user_sql where Year ={Year} and Quarter ={Quarter} group by Brand order by Total_Count desc limit 10")
            df = pd.DataFrame (mycursor.fetchall(),columns=['Brand','Total_Users','Avg_Percentage'])
            st.write(df)
            fig= px.pie(df,
                        values='Total_Users',
                        names='Brand',
                        title='Top 10 Phonepe users according to Brands',
                        hole=0.5,
                        color = 'Avg_Percentage'
                        )
            st.plotly_chart(fig,use_container_width=True)
             
       if Data_segmentation=="Registered_User":
           mycursor.execute(f"select district,sum(Registered_User) as Total_Registered_Users from map_user_sql where Year= {Year} and quarter={Quarter} group by District order by Total_Registered_Users desc limit 10")
           df= pd.DataFrame(mycursor.fetchall(),columns=['District','Total_Registered_Users'])
           st.write(df)
           fig= px.pie(df,
                       title='Top 10 Phonepe users according to Districts',
                       values = "Total_Registered_Users",
                       names= "District",
                       hole = 0.5,
                       color= 'Total_Registered_Users')
           st.plotly_chart(fig,use_container_width=True)
           
       if Data_segmentation=="Appopeners":
           mycursor.execute(f"SELECT state,SUM(App_opening) AS Total_Appopeners FROM map_user_sql WHERE year ={Year} AND quarter = {Quarter} AND App_opening > 0 GROUP BY  state ORDER BY Total_Appopeners DESC limit 10")
           df=pd.DataFrame(mycursor.fetchall(),columns=['State','Total_Appopeners'])
           st.write(df)
           fig=px.pie(df,
                      values='Total_Appopeners',
                      names='State',
                      title='Top 10 Phonepe users according to Appopeners',
                      hole=0.5,
                      color='Total_Appopeners')
           st.plotly_chart(fig,use_container_width=True)
           
           
#Explore the data
if selected=="Explore Data":
   st.markdown("##:violet[Exploring the Data]")
   Type = st.sidebar.selectbox("**Type**",("Analysis of Transactions","Users"))  
   if Type=="Analysis of Transactions":
       col1,col2=st.columns([1,1.5],gap="large")
       with col1:
                    
                    Year = st.slider("**Select the Year**",min_value=2018,max_value=2022)
                    Quarter=st.selectbox('**Select the Quarter',('1','2','3','4'),key='qgwe2')
       with col2:
           st.write(
               """
               In this page we will get the insights of transactions count According to District,Transaction Types vs Total Transactions amount and Geomap visualization to show  the state based data according to Transaction count and TRransaction amount.
               """
               )
       st.markdown("##:violet[**Transaction Count According To District**]")
       selected_state= st.selectbox("**please select any State to visualize**",
                              ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                              'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                              'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                              'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                              'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                              'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),index=22,key="state_to selectbox")
       mycursor.execute(f"select State,District,year,quarter,sum(transaction_count) as Total_Transactions_Count from map_trans_sql where year ={Year} and quarter = {Quarter} and State = '{selected_state}' group by State,District,year,quarter order by state,district")
       
       df1=pd.DataFrame(mycursor.fetchall(),columns=['State','District','Year','Quarter','Total_Transactions_count'])
       
       
       fig=px.bar(df1,
                  title='Transaction Count According To District',
                  x="District",
                  y="Total_Transactions_count",
                  orientation='v',
                  color='Total_Transactions_count',
                  color_continuous_scale=px.colors.sequential.Magenta)
                  
       st.plotly_chart(fig,use_container_width=True)
       st.markdown("##:violet[payment type]")
       selected_state=st.selectbox("**please select any state to visualize**",
                              ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                              'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                              'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                              'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                              'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                              'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),key="state_selectbox")
       Type = st.selectbox('**Please select the values to visualize**',('Transaction_count','Transaction_amount'))
       if Type =="Transaction_count":
                  mycursor.execute(f"select Transaction_type,sum(Transaction_count) as Total_Transactions_count from agg_trans_sql where year = {Year} and quarter ={Quarter} group by transaction_type order by Transaction_type")
                  df=pd.DataFrame(mycursor.fetchall(),columns=['Transaction_type','Total_Transactions_count'])

                  fig = px.bar(df,
                               title= 'Transaction Types vs Total_Transactions_count',
                               x='Transaction_type',
                               y='Total_Transactions_count',
                               orientation='v',
                               color='Transaction_type',
                               color_continuous_scale=px.colors.sequential.Magenta)
                  st.plotly_chart(fig,use_container_width=False) 
                  
       if Type=="Transaction_amount":
                 mycursor.execute(f"select Transaction_type, sum(Transaction_amount) as Total_Transaction_amount from agg_trans_sql where year={Year} and quarter={Quarter} group by transaction_type order by Transaction_type")
                 df=pd.DataFrame(mycursor.fetchall(),columns=['Transaction_type','Total_Transactions_amount'])
                 fig=px.bar(df,
                            title='Tranasction Types vs Total_Transactions_amount',
                            x='Transaction_type',
                            y='Total_Transactions_amount',
                            orientation='v',
                            color='Transaction_type',
                            color_continuous_scale=px.colors.sequential.Magenta)
                 st.plotly_chart(fig,use_container_width=False)
                 
       #Map

       india= json.load(open("C:\Guvi\Data science\Projects\india_state_geo.json","r"))


       select1 = st.selectbox("Select a any one",["Transaction count","Transaction amount"])
       st.markdown(":violet[This map used to show the state based data according to Transaction count Transaction amount]")
       mycursor.execute(f"select State, sum(Transaction_count) as Total_Transaction_count,sum(Transaction_amount) as Total_Transaction_amount from map_trans_sql where year={Year} and quarter= {Quarter} group by State order by State")
       df1 = pd.DataFrame(mycursor.fetchall(),columns=['State','Total_Transaction_count','Total_Transaction_amount'])
       State_name="C:\Guvi\Data science\Projects\India States-UTs.csv"
       data=pd.read_csv(State_name)
       df1.State=data
       if select1=="Transaction amount":
           fig1 = px.choropleth(df1,geojson=india,
                featureidkey='properties.ST_NM',
                locations = 'State',
                color ='Total_Transaction_amount',
                color_continuous_scale='Aggrnyl')
                  
           fig1.update_geos(fitbounds='locations',visible=False)
           st.plotly_chart(fig1,use_container_width=True)
                              
       if select1=="Transaction count":
           fig2=px.choropleth(df1,geojson=india,
                featureidkey='properties.ST_NM',
                locations='State',
                color='Total_Transaction_count',
                color_continuous_scale='Aggrnyl')
           
           fig2.update_geos(fitbounds="locations",visible=False)
           st.plotly_chart(fig2,use_container_width=True)                
            
            
   if Type=="Users":
      Data_segmentation=st.sidebar.selectbox("**Data segmentation**",("Registered Users","Analysis of country"),key="Data_selectbox")
      col1,col2=st.columns([1,1.5],gap="large")
      with col1:
          Year = st.slider("**Select the Year**",min_value=2018,max_value=2022)
          Quarter=st.selectbox("**Select the Quarter**",('1234'),key='quart')
      if Data_segmentation=="Registered Users":
               st.markdown("##:violet[Total Numbers of Registered Users According to Districts")
               selected_state=st.selectbox("**Select any state to fetch the data**",
                              ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                              'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                              'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                              'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                              'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                              'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),index=1)
               mycursor.execute(f"select State,year,quarter,District,sum(Registered_user) as Total_Registered_Users from map_user_sql where year={Year} and quarter ={Quarter} and state = '{selected_state}' group by State,District,year,quarter order by state,district")
               df=pd.DataFrame(mycursor.fetchall(),columns=['State','year','quarter','District','Total_Registered_Users'])
               fig = px.bar(df,
                            x="District",
                            y="Total_Registered_Users",
                            orientation='v',
                            color="Total_Registered_Users",
                            color_continuous_scale=px.colors.sequential.Magenta)
               st.plotly_chart(fig,use_container_width=True)
      india1 = json.load(open("C:\Guvi\Data science\Projects\india_state_geo.json","r"))
      if Data_segmentation=="Analysis of country":
               st.markdown(":violet[This geomap used to show the state based data according to Registered users and App_Openers]")
               mycursor.execute(f"select State,sum(Registered_user) as Registered_Users, sum(app_opening) as App_Opens from  map_user_sql where year={Year} and quarter ={Quarter} group by state")
               df1=pd.DataFrame(mycursor.fetchall(),columns=["State","Registered_Users","App_Opens"])
               State_name="C:\Guvi\Data science\Projects\India States-UTs.csv"
               data=pd.read_csv(State_name)
               df1.State=data
               fig=px.choropleth(df1,
                      geojson=india1,
                      featureidkey="properties.ST_NM",
                      locations="State",
                      color="Registered_Users",
                      hover_data=["State","Registered_Users","App_Opens"],
                      color_continuous_scale={
                          })
               fig.update_geos(fitbounds="locations",visible=False)
               fig.update_layout(height=600,width=800)
               st.plotly_chart(fig,use_container_width=False,key='choropleth_chart')
        
            
            
            
            
            
            
            
            
            
            
            
            
            