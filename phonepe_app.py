
import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="PhonePe", page_icon=":phone:", 
                   layout="wide")

st.title(":phone: PhonePe Data Analysis")

st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

selected = option_menu( None,["Home", "Geospatial Analysis", "Visualization"], 
                        icons=['phone-fill', 'map-fill', "bar-chart-fill"], 
                        menu_icon="cast", 
                        default_index=0,
                        orientation="horizontal",
                        styles={"container": {"padding": "0!important", "background-color": "orange"},
                                "icon": {"color": "red", "font-size": "1.5rem"}, 
                                "nav-link": {"font-size": "1.25rem", "text-align": "left", "margin":"0px", "--hover-color": "#6F8FAF", "background-color": "orange"},
                                "nav-link-selected": {"background-color": "green"}}) 

#---------------------------------HOME PAGE---------------------------------#

if selected == "Home": 

    tab1, tab2, tab3 = st.tabs(["About PhonePe", "About PhonePe-Plus","Overview of Analysis"])

    with tab1: # About PhonePe

        st.subheader("About PhonePe")

        st.markdown("""PhonePe is an advanced service offered by PhonePe, a leading fintech company in India known for its digital payments app. PhonePe Plus provides users with a comprehensive suite of financial services and features designed to enhance their experience and facilitate various financial transactions.""")
        st.markdown('<iframe width="700" height="394" src="https://www.youtube.com/embed/c_1H6vivsiA" title="Introducing PhonePe Pulse" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.markdown("""### Key Features of PhonePe:

1. **Comprehensive Financial Services**:
   - **Payments**: PhonePe Plus allows users to make seamless and secure payments through multiple methods such as UPI, debit/credit cards, and PhonePe Wallet.
   - **Insurance**: Users can explore and purchase various insurance products, including health, motor, and travel insurance.
   - **Investments**: The platform offers investment options in mutual funds, gold, and other financial instruments.

2. **PhonePe Switch**:
   - **Integrated Apps**: Users can access and use their favorite apps, like booking flights, ordering food, or buying groceries, without needing to download them separately.

3. **PhonePe Pulse**:
   - **Data Insights**: Provides users with insights into financial trends and transaction data, updated quarterly to reflect the latest information.

4. **Security**:
   - **Best-in-Class Security**: PhonePe Plus incorporates advanced security measures to protect user data and transactions, minimizing the risk of fraud.

5. **Merchant Solutions**:
   - **Payment Gateway**: Businesses can use PhonePe's payment gateway to process online payments efficiently.
   - **POS Machine and SmartSpeaker**: Tools for offline merchants to accept digital payments easily.
   - **Advertising and Marketing**: Businesses can advertise on PhonePe to reach a larger audience.

6. **Indus Appstore**:
   - **Localized Experience**: An Android-based app store that caters to the specific needs of Indian users, offering apps in multiple Indian languages and supporting third-party payment gateways without commissions.

PhonePe Plus aims to provide a holistic financial ecosystem, empowering users with a variety of services on a single platform, while maintaining a high level of security and user convenience【89†source】【90†source】. """)

    with tab2:

        st.subheader("About PhonePe-Plus")

        st.markdown("""The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data.

When PhonePe started 5 years back, we were constantly looking for definitive data sources on digital payments in India. Some of the questions we were seeking answers to were - How are consumers truly using digital payments? What are the top cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes?
This year as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments in India.

This year, as we crossed 2000 Cr. transactions and 30 Crore registered users, we thought as India's largest digital payments platform with 46% UPI market share, we have a ring-side view of how India sends, spends, manages and grows its money. So it was time to demystify and share the what, why and how of digital payments in India.

PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.""")
        
        st.markdown('<iframe width="700" height="394" src="https://www.youtube.com/embed/Yy03rjSUIB8" title="PhonePe Pulse 2.0 - Here&#39;s what is new" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>', unsafe_allow_html=True)


    with tab3: # Overview of Analysis
        st.subheader("Overview of Analysis")

        st.markdown("""# Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly

# PhonePe Pulse Data Visualization Capstone Project

## Project Overview

This capstone project aims to develop a comprehensive solution for extracting, transforming, storing, and visualizing data from the PhonePe Pulse GitHub repository. The objective is to create a live geo-visualization dashboard that presents valuable insights and statistics in an interactive and user-friendly manner.

## Problem Statement

The PhonePe Pulse GitHub repository contains extensive data related to various metrics and statistics. The goal is to process this data to derive insights that can be effectively visualized. The solution involves the following steps:

1. Extract data from the PhonePe Pulse GitHub repository using scripting.
2. Transform the data into a suitable format and perform necessary cleaning and pre-processing.
3. Store the transformed data in a MySQL database for efficient retrieval.
4. Develop a live geo-visualization dashboard using Streamlit and Plotly in Python.
5. Retrieve data from the MySQL database to display on the dashboard.
6. Provide at least 10 different dropdown options for users to explore various facts and figures on the dashboard.

## Solution Approach

### Step 1: Data Extraction

- Clone the PhonePe Pulse GitHub repository using scripting.
- Store the extracted data in formats such as CSV or JSON for further processing.

### Step 2: Data Transformation

- Use Python and libraries like Pandas to clean and preprocess the data.
- Handle missing values and transform the data into a format suitable for analysis and visualization.

### Step 3: Database Insertion

- Utilize the `mysql-connector-python` library to connect to a MySQL database.
- Insert the transformed data into the database using SQL commands.

### Step 4: Dashboard Creation

- Develop an interactive dashboard using Streamlit and Plotly libraries in Python.
- Use Plotly's geo map functions to display data on a map.
- Incorporate multiple dropdown options in Streamlit for users to select different facts and figures to display.

### Step 5: Data Retrieval

- Connect to the MySQL database using the `mysql-connector-python` library.
- Fetch data into a Pandas DataFrame and update the dashboard dynamically.

### Step 6: Deployment

- Ensure the solution is secure, efficient, and user-friendly.
- Thoroughly test the solution and deploy the dashboard publicly for user access.

## Results

The final deliverable will be a live geo-visualization dashboard that:
- Displays insights and statistics from the PhonePe Pulse GitHub repository interactively.
- Provides at least 10 different dropdown options for exploring various metrics.
- Ensures efficient data retrieval through a MySQL database.
- Is accessible from a web browser, allowing easy navigation and exploration of data.

## Repository Structure

```plaintext
.
├── data
│   ├── raw
│   ├── processed
│   └── transformed
├── scripts
│   ├── data_extraction.py
│   ├── data_transformation.py
│   ├── db_insertion.py
│   ├── data_retrieval.py
│   └── dashboard.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Getting Started

### Prerequisites

- Python 3.8+
- MySQL Database
- Git

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/PhonePe/pulse.git
   cd phonepe-pulse-data-visualization
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   ```sql
   CREATE DATABASE phonepe_pulse;
   ```

### Running the Scripts

1. **Data Extraction:**
   ```sh
   python scripts/data_extraction.py
   ```

2. **Data Transformation:**
   ```sh
   python scripts/data_transformation.py
   ```

3. **Database Insertion:**
   ```sh
   python scripts/db_insertion.py
   ```

4. **Run the Dashboard:**
   ```sh
   streamlit run scripts/dashboard.py
   ```

## Usage

- Access the dashboard via your web browser at the local host address provided by Streamlit.
- Use the dropdown options to explore various insights and statistics from the PhonePe Pulse data.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PhonePe Pulse](https://github.com/PhonePe/pulse) for providing the data.
- Contributors and the open-source community for their valuable tools and libraries.


 """)

# Load the dataframes
# Transaction dataframes
df_agg_transaction = pd.read_csv("https://raw.githubusercontent.com/VivekS-DS/Phonepe-Pulse-Data-Visualization-and-Exploration-/main/data/df_agg_transaction.csv")
df_top_transact_dist = pd.read_csv("https://raw.githubusercontent.com/VivekS-DS/Phonepe-Pulse-Data-Visualization-and-Exploration-/main/data/df_top_tranc_district.csv")
df_top_transact_pincode = pd.read_csv("https://raw.githubusercontent.com/VivekS-DS/Phonepe-Pulse-Data-Visualization-and-Exploration-/main/data/df_top_tranc_pincode.csv")

# User dataframes
df_agg_users = pd.read_csv("https://raw.githubusercontent.com/VivekS-DS/Phonepe-Pulse-Data-Visualization-and-Exploration-/main/data/df_agg_user.csv")
df_map_user = pd.read_csv("https://raw.githubusercontent.com/VivekS-DS/Phonepe-Pulse-Data-Visualization-and-Exploration-/main/data/df_map_user_hover.csv")



#-----------------------------------Geospatial Analysis-----------------------------------#        
if selected == "Geospatial Analysis":

    st.subheader("Geospatial Analysis")
    
    st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)
    
    # Load the geojson file
    with open('india_states.json') as f:
        geojson = json.load(f)
    
    state_list = {}
    for i in range(len(geojson['features'])):
        state_name = geojson['features'][i]['properties']['ST_NM']
        state_list[state_name] = i

    # Create a sidebar
    with st.sidebar:
        st.sidebar.header("Geospatial Analysis")
        st.markdown("""Select the area to be analyzed:""")

        state = st.selectbox('Select state',  ['All']+df_agg_transaction['state'].unique().tolist())

        #category = st.selectbox('Select category', ('Insurance', 'Transaction', 'User'))
        year = st.selectbox('Select year', (2018, 2019, 2020, 2021, 2022, 2023,2024))
        quarter = st.selectbox('Select quarter', ('Q1', 'Q2', 'Q3', 'Q4'))

#-----------------------------------Geospatial Analysis-----------------------------------#
    tab1, tab2 = st.tabs(["Transaction","User"])

    

    with tab1:
        st.header("Transaction")
        
        if state == 'All':
                        
                user_tran_value_all = df_agg_transaction[(df_agg_transaction['year'] == year) &
                                                    (df_agg_transaction['quarter'] == quarter)].groupby('state').sum()['total_amount'].reset_index()
                
                fig = px.choropleth_mapbox(user_tran_value_all, geojson=geojson, locations='state', color='total_amount',
                                featureidkey='properties.ST_NM',
                                color_continuous_scale=px.colors.sequential.Rainbow,
                                mapbox_style="carto-positron",
                                range_color=[1000000, 1000000000000],
                                zoom=3, center = {"lat": 23.07279, "lon": 78.8163}, #23.07279400079414, 78.8163004748913
                                opacity=0.5, 
                                labels={'total_amount':'Total Amount', 'count':'Count'}
                                )
                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                st.plotly_chart(fig, use_container_width=True, height=200)

        else:
                state_code = state_list[state]
                multi_polygon_state = ['Andaman and Nicobar Islands','Tamil Nadu', 'Uttar Pradesh', 'West Bengal', 'Andra Pradesh', 'Maharashtra']
                if state in multi_polygon_state:
                    if state == 'Tamil Nadu':
                        mean_latitude = 11.1271
                        mean_longitude = 78.6569
                    elif state == 'Uttar Pradesh':
                        mean_latitude = 26.8467
                        mean_longitude = 80.9462
                    elif state == 'West Bengal':
                        mean_latitude = 22.5726
                        mean_longitude = 88.3639
                    elif state == 'Andra Pradesh':
                        mean_latitude = 15.9129
                        mean_longitude = 79.7400
                    elif state == 'Maharashtra':
                        mean_latitude = 19.7515
                        mean_longitude = 75.7139
                    elif state == 'Andaman and Nicobar Islands':
                        mean_latitude = 11.7403
                        mean_longitude = 92.6586

                    fig = px.choropleth_mapbox(df_agg_transaction, geojson=geojson['features'][state_code], locations='state', color='total_amount',
                                            featureidkey='properties.ST_NM',
                                            color_continuous_scale=px.colors.sequential.Rainbow,
                                            mapbox_style="carto-positron",
                                            range_color=[100000, 1000000000],
                                            zoom=5, 
                                            center = {"lat": mean_latitude, "lon": mean_longitude}, 
                                            opacity=0.5, 
                                            labels={'total_amount':'Total Amount', 'count':'Count'},
                                            )
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    st.plotly_chart(fig, use_container_width=True, height=200) 

                else:
                    
                    coordinates = geojson['features'][state_code]['geometry']['coordinates']
                    # Extract the coordinates
                    latitudes = [coord[1] for coord in coordinates[0]]
                    longitudes = [coord[0] for coord in coordinates[0]]

                    # Calculate the mean latitude and longitude
                    mean_latitude = float(sum(latitudes) / len(latitudes))
                    mean_longitude = float(sum(longitudes) / len(longitudes))

                    fig = px.choropleth_mapbox(df_agg_transaction, geojson=geojson['features'][state_code], locations='state', color='total_amount',
                                            featureidkey='properties.ST_NM',
                                            color_continuous_scale=px.colors.sequential.Rainbow,
                                            mapbox_style="carto-positron",
                                            range_color=[100000, 1000000000],
                                            zoom=5, 
                                            center = {"lat": mean_latitude, "lon": mean_longitude}, #23.07279400079414, 78.8163004748913
                                            opacity=0.5, 
                                            labels={'total_amount':'Total Amount', 'count':'Count'},
                                            )
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    st.plotly_chart(fig, use_container_width=True, height=200)


        col1, col2 = st.columns(2)

        with col1: # table
            if state == 'All':
                tran_value_all = df_agg_transaction[(df_agg_transaction['year'] == year) &
                                                    (df_agg_transaction['quarter'] == quarter)].groupby('payment_type').sum()['total_amount'].reset_index()
                tran_value_all = tran_value_all.sort_values(by='total_amount', ascending=False).reset_index(drop=True)
                    
                st.table(tran_value_all)

            else:
                tran_value_state = df_agg_transaction[(df_agg_transaction['state'] == state) &
                                                    (df_agg_transaction['year'] == year) &
                                                    (df_agg_transaction['quarter'] == quarter)].groupby('payment_type').sum()['total_amount'].reset_index()
                tran_value_state = tran_value_state.sort_values(by='total_amount', ascending=False).reset_index(drop=True)
                st.write(tran_value_state)


        with col2: # Donut Chart
            
            if state == 'All':
                tran_value_all = df_agg_transaction[(df_agg_transaction['year'] == year) &
                                                (df_agg_transaction['quarter'] == quarter)].groupby('payment_type').sum()['total_amount']
                
                colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
                # Use `hole` to create a donut-like pie chart
                fig = go.Figure(data=[go.Pie(labels=list(tran_value_all.index), 
                                            values=list(tran_value_all.values), 
                                            hole=.5)])
                
                fig.update_traces(hoverinfo='label+value',
                                textinfo='percent', 
                                textfont_size=16,
                                marker=dict(colors=colors, 
                                            line=dict(color='#000000', width=.5)))
                
                st.plotly_chart(fig, use_container_width=True, height=200)

            else:
                tran_value_state = df_agg_transaction[(df_agg_transaction['state'] == state) &
                                                      (df_agg_transaction['year'] == year) &
                                                      (df_agg_transaction['quarter'] == quarter)].groupby('payment_type').sum()['total_amount']
                
                colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
                # Use `hole` to create a donut-like pie chart
                fig = go.Figure(data=[go.Pie(labels=list(tran_value_state.index), 
                                            values=list(tran_value_state.values), 
                                            hole=.5)])
                
                fig.update_traces(hoverinfo='label+value',
                                textinfo='percent', 
                                textfont_size=16,
                                marker=dict(colors=colors, 
                                            line=dict(color='#000000', width=.5)))
                
                st.plotly_chart(fig, use_container_width=True, height=200)

        

# Top 10 Transaction (District Wise and Pincode Wise)
       
        st.subheader("Top 10 Transaction (District Wise)")
        if state == 'All':
            top_tran_dist = df_top_transact_dist[(df_top_transact_dist['year'] == year) &
                                                     (df_top_transact_dist['quarter'] == quarter)].groupby('district')['amount'].sum()
                
            top_tran_dist = top_tran_dist.nlargest(10).reset_index()
            
            fig = px.bar(top_tran_dist, y='amount', x='district', text='amount')
            fig.update_traces(texttemplate='%{y:.0f}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', width=800, height=600)
            st.plotly_chart(fig, use_container_width=True, height=200)
            
            st.table(pd.DataFrame(top_tran_dist, index=range(0, len(top_tran_dist)))) #top_tran_dist

        else:
            top_tran_dist = df_top_transact_dist[(df_top_transact_dist['state'] == state) &
                                                     (df_top_transact_dist['year'] == year) &
                                                     (df_top_transact_dist['quarter'] == quarter)].groupby('district')['amount'].sum()
                
            top_tran_dist = top_tran_dist.nlargest(10).reset_index()
                
            fig = px.bar(top_tran_dist, y='amount', x='district', text='amount')
            fig.update_traces(texttemplate='%{y:.0f}', textposition='outside')
            fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', width=800, height=600)
            st.plotly_chart(fig, use_container_width=True, height=200)
                
            st.table(pd.DataFrame(top_tran_dist, index=range(0, len(top_tran_dist))))

        # Top 10 Transaction (Pincode Wise)
        st.subheader("Pincode")

        df_top_transact_pincode['pincode'] = df_top_transact_pincode['pincode'].astype(str)
        df_top_transact_pincode['pincode'] = df_top_transact_pincode['pincode'].str[:6]

        if state == 'All':
            top_tran_pincode = df_top_transact_pincode[(df_top_transact_pincode['year'] == year) &
                            (df_top_transact_pincode['quarter'] == quarter)].groupby('pincode')['amount'].sum()
                
            top_tran_pincode = top_tran_pincode.nlargest(10).reset_index()
            
            st.table(pd.DataFrame(top_tran_pincode, index=range(0, len(top_tran_pincode), 1)))

        else:
            top_tran_pincode = df_top_transact_pincode[(df_top_transact_pincode['state'] == state) &
                            (df_top_transact_pincode['year'] == year) &
                            (df_top_transact_pincode['quarter'] == quarter)].groupby('pincode')['amount'].sum()
                
            top_tran_pincode = top_tran_pincode.nlargest(10).reset_index()
            st.table(pd.DataFrame(top_tran_pincode, index=range(0, len(top_tran_pincode), 1)))
                

    with tab2: # User
        st.header("User")

        st.subheader("User Mobile Brand Analysis")
        if state == 'All':
            top_agg_user_all = df_agg_users[(df_agg_users['year'] == year) &
                                            (df_agg_users['quarter'] == quarter)].groupby('Brand').sum()['user_count']

            top_agg_user_all = top_agg_user_all.to_frame().reset_index()

            for index in range(len(top_agg_user_all)):
                top_agg_user_all.at[index, 'Percentage'] = top_agg_user_all.at[index, 'user_count']/top_agg_user_all['user_count'].sum()*100

            if len(top_agg_user_all) == 0 or top_agg_user_all is None:
                st.error(f'No data available for the selected {year}')

            else:
                fig = px.treemap(top_agg_user_all,
                    path=['Brand'],
                    values='Percentage',
                    color='Percentage',
                    color_continuous_scale='blackbody',
                    
                    hover_data={'Percentage':  ':.2f'},
                    hover_name='Brand',
                    #title=f'PhonePe App Users by Mobile Brands in {state}'
                        )
                fig.update_layout(uniformtext=dict(minsize=10, mode='hide'),
                                        width=800, height=600, margin = dict(t=50, l=25, r=25, b=25),
                                        title = {'text': f"PhonePe App Users by Mobile Brands in {state}",
                                                'y':1,'x':0.5,'xanchor': 'center','yanchor': 'top'})


                fig.update_traces(marker=dict(cornerradius=5), textinfo="label")
                st.plotly_chart(fig, use_container_width=True)


        else:
            top_agg_user = df_agg_users[(df_agg_users['state'] == state) &
                            (df_agg_users['year'] == year) &
                            (df_agg_users['quarter'] == quarter)].groupby('Brand').sum()['user_count']

            top_agg_user = top_agg_user.to_frame().reset_index()

            for index in range(len(top_agg_user)):
                top_agg_user.at[index, 'Percentage'] = top_agg_user.at[index, 'user_count']/top_agg_user['user_count'].sum()*100
            
            if len(top_agg_user) == 0 or top_agg_user is None:
                st.error(f'No data available for the selected {state} and {year}')

            else:
                fig = px.treemap(top_agg_user,
                            path=['Brand'],
                            values='Percentage',
                            color='Percentage',
                            color_continuous_scale='blackbody',
                            
                            hover_data={'Percentage':  ':.2f'},
                            hover_name='Brand',
                            #title=f'PhonePe App Users by Mobile Brands in {state}'
                                )
                fig.update_layout(uniformtext=dict(minsize=10, mode='hide'),
                                    width=800, height=600, margin = dict(t=50, l=25, r=25, b=25),
                                    title = {'text': f"PhonePe App Users by Mobile Brands in {state}",
                                            'y':1,'x':0.5,'xanchor': 'center','yanchor': 'top'})


                fig.update_traces(marker=dict(cornerradius=5), textinfo="label")
                st.plotly_chart(fig, use_container_width=True)

        st.subheader("Registered Users Analysis")

        type = st.selectbox('Select type', ('reg_user','app_open'))
        
        if state == 'All':
            top_reg_user = df_map_user[(df_map_user['year'] == year) &
                                       (df_map_user['quarter'] == quarter)  
                                       ].groupby(['state','district','latitude','longitude']).sum()[[type]]

            top_reg_user = top_reg_user.reset_index()

            center_latitude_all = top_reg_user['latitude'].median()
            center_longitude_all = top_reg_user['longitude'].median()

            fig = px.scatter_mapbox(top_reg_user, 
                                    lat="latitude", 
                                    lon="longitude", 
                                    hover_name="district",
                                    size=type, 
                                    color=type,
                                    color_continuous_scale=px.colors.sequential.Rainbow,
                                    title=f"PhonePe App Registered Users in {state}")



            fig.update_layout(mapbox_style="open-street-map",
                            mapbox_center = {"lat": center_latitude_all, "lon": center_longitude_all},
                            mapbox_zoom=3.4, 
                            geo=dict(scope = 'asia' ), 
                            width=800, height=600, margin = dict(t=50, l=25, r=5, b=25),
                            
                            title = {'text': f"PhonePe App Registered Users in {state}",
                                    'y':.95,'x':0.5,'xanchor': 'center','yanchor': 'top'})
            
            st.plotly_chart(fig, use_container_width=True)

            top_reg_user = top_reg_user[['district', type]].sort_values(by=type, ascending=False).reset_index(drop=True)

            st.table(top_reg_user.head(10))

        else:

            top_reg_user = df_map_user[
                            (df_map_user['state'] == state) &
                            (df_map_user['year'] == year) &
                            (df_map_user['quarter'] == quarter)  
                            ].groupby(['state','district','latitude','longitude']).sum()[[type]]

            top_reg_user = top_reg_user.reset_index()

            center_latitude = top_reg_user[top_reg_user['state'] == state]['latitude'].median()
            center_longitude = top_reg_user[top_reg_user['state'] == state]['longitude'].median()

            fig = px.scatter_mapbox(top_reg_user, 
                                    lat="latitude", 
                                    lon="longitude", 
                                    hover_name="district",
                                    size=type, 
                                    color=type,
                                    color_continuous_scale=px.colors.sequential.Rainbow,
                                    title=f"PhonePe App Registered Users in {state}")



            fig.update_layout(mapbox_style="open-street-map",
                            mapbox_center = {"lat": center_latitude, "lon": center_longitude},
                            mapbox_zoom=6, 
                            geo=dict(scope = 'asia' ), 
                            width=800, height=600, margin = dict(t=50, l=25, r=5, b=25),
                            
                            title = {'text': f"PhonePe App Registered Users in {state}",
                                    'y':.95,'x':0.5,'xanchor': 'center','yanchor': 'top'})
            
            st.plotly_chart(fig, use_container_width=True)

            top_reg_user = top_reg_user[['district', type]].sort_values(by=type, ascending=False).reset_index(drop=True)

            st.table(top_reg_user.head(10))
            

#----------------------------------------Trend Visualization----------------------------------------#

if selected == "Visualization":

    st.header("Trend Visualization") 

    
    # Create a sidebar
    with st.sidebar:
        st.sidebar.header("Geospatial Analysis")
        st.markdown("""Select the area to be analyzed:""")

        state = st.selectbox('Select state',  ['All']+df_agg_transaction['state'].unique().tolist())

        
        year = st.selectbox('Select year', (2018, 2019, 2020, 2021, 2022, 2023,2024))
        #quarters = st.selectbox('Select quarter', ('Q1', 'Q2', 'Q3', 'Q4'))

    if state == 'All': 
        agg_trans_barplot = df_agg_transaction[
            #(df_agg_transaction['state'] == state) &
                    (df_agg_transaction['year'] == year)
                    ].groupby(['quarter','payment_type']).sum()['total_amount'].reset_index()

        fig = px.bar(agg_trans_barplot, x='quarter', y='total_amount',
                title=f"Aggregated Transaction Amount Spent on PhonePe in India in {year} by Payment Type",
                color='payment_type', text_auto='.0f',
                labels={'total_amount':'Total Amount',
                        'quarter':'Quarter',
                        'payment_type':'Payment Type'}, height=600)

        st.plotly_chart(fig, use_container_width=True)
    else:
        agg_trans_barplot = df_agg_transaction[(df_agg_transaction['state'] == state) &
                    (df_agg_transaction['year'] == year)
                    ].groupby(['quarter','payment_type']).sum()['total_amount'].reset_index()

        fig = px.bar(agg_trans_barplot, x='quarter', y='total_amount',
                title=f"Aggregated Transactions done on PhonePe in the state of {state} during {year}",
                color='payment_type', text_auto='.0f',
                labels={'total_amount':'Total Amount',
                        'quarter':'Quarter',
                        'payment_type':'Payment Type'}, height=600)

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("District wise Trend")
        top_tran_dist_trend =df_top_transact_dist[(df_top_transact_dist['state'] == state) &
                    (df_top_transact_dist['year'] == year) 
                    ].groupby(['quarter','district']).sum()['amount'].reset_index()
        
        fig = px.bar(top_tran_dist_trend, x='quarter', y='amount',
                title=f"Top District wise Transactions done on PhonePe in the state of {state} during {year}",
                color='district', text_auto='.0f',
                labels={'total_amount':'Total Amount',
                        'quarter':'Quarter',
                        'payment_type':'Payment Type'}, height=600)

        st.plotly_chart(fig, use_container_width=True)


        st.subheader("PhonePe App Registered Users Trend")

        
    
        top_reg_user = df_map_user[(df_map_user['state'] == state) & 
                                   (df_map_user['year'] == year)
                                   ].groupby(['year', 'quarter','state','district']).sum()[['reg_user']]

        top_reg_user = top_reg_user.sort_values(by='reg_user', ascending=False).reset_index()

        top_reg_user = top_reg_user.nlargest(40, 'reg_user')


        fig = px.histogram(top_reg_user, x='district', y='reg_user',
                title=f"PhonePe Total Registered Users District wise in the state of {state} during {year}",
                color='quarter', text_auto='.0f',
                labels={'reg_user':'Registered Users',
                        'quarter':'Quarter',
                        'payment_type':'Payment Type'}, height=600)

        st.plotly_chart(fig, use_container_width=True)
    
#----------------------------------------End----------------------------------------#