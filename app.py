import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import plotly.express as px
import seaborn as sns
import datetime
import requests
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from PIL import Image



######### Create the user interface #########
## Use streamlit for the app

#[theme]

# Primary accent for interactive elements
#primaryColor = '#7792E3'
# Background color for the main content area
#backgroundColor = '#273346'
# Background color for sidebar and most interactive widgets
#secondaryBackgroundColor = '#B9F1C0'
# Color used for almost all text
#textColor = '#FFFFFF'
# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace)
# Default: "sans serif"
#font = "sans serif"

#Constante
Const_Store_nbr = 54
api_token = px.set_mapbox_access_token('pk.eyJ1IjoibXJkYXJhdWpvIiwiYSI6ImNsM3hsY2c2NzAzcHEzYm1oYmliZHc5aXoifQ.1E3p2I8p8bEkHSPJDzUXWQ')
#Const_LocalPath = "/Users/farahboukitab/code/mrdaraujo/business_case_869/business_case_869/data/store-sales-time-series-forecasting/"
Const_LocalPath = 'https://storage.googleapis.com/business-case/Production%20files/'
#Const_LocalPath = "gs://business-case/Production files/"
Const_url_predict_city = 'https://image-bc869-v2-1-ob6evlacjq-ew.a.run.app/predict-city-year'
Const_url_predict_store = 'https://image-bc869-v2-1-ob6evlacjq-ew.a.run.app/predict-store-year'
Const_url_predict_family = 'https://image-bc869-v2-1-ob6evlacjq-ew.a.run.app/predict-family-year'
Const_month_predict = ['1','2','3','4','5','6','7','8','9','10','11','12']

test = "test"

#imageStore = Image.open(Const_LocalPath + 'Favorita logo.png')
# imageLeWagon = Image.open(Const_LocalPath + 'lewagonlogo.png')
# col1, col_, col2 = st.columns([1,4,1])
# with col1:
#     st.image(imageStore, caption="")
# with col_:
#     # Define text, title and header
#     st.header('Business Case -- Le Wagon 869')
#     st.subheader('How to analyse and predict sales in a company with different stores, cities and product types')
#     st.text('Case study: 54 stores in 22 cities in Ecuador for a commercial company')

    #new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
    #st.markdown(new_title, unsafe_allow_html=True)

# with col2:
#    st.image(imageLeWagon, caption="")





# Load csv dataset - Check the cache
# Initialization
#st.write(st.session_state.count)
if 'count' not in st.session_state : #or (st.session_state.last_ticker != ticker) :
    st.session_state.count = 0
    st.write("Executing the getting csv function")
    init = datetime.datetime.now()
    @st.cache()
    def getting_csv():
        # Getting all csv files that are not going to change
        df_heatmap = pd.read_csv(Const_LocalPath + "Heatmap.csv")
        data_train_merge_stores = pd.read_csv(Const_LocalPath + "data_train_merge_stores.csv")
        map_base = pd.read_csv(Const_LocalPath + "map_base.csv")
        sales_city_year = pd.read_csv(Const_LocalPath +"sales_city_year.csv")
        map_base_top_five = pd.read_csv(Const_LocalPath + "map_base_top_five.csv")
        map_base_top_five['year'] = map_base_top_five['year'].astype('string')
        df_stores_city = pd.read_csv(Const_LocalPath + "df_stores_city.csv")
        df_MaxSales_BiggestStore = pd.read_csv(Const_LocalPath + "df_MaxSales_BiggestStore.csv")
        df_MaxSales_BiggestStore['store_nbr'] = df_MaxSales_BiggestStore['store_nbr'].astype('string')
        df_stores_top_five = pd.read_csv(Const_LocalPath + "df_stores_top_five.csv")
        df_stores_top_five['store_nbr'] = df_stores_top_five['store_nbr'].astype('string')
        data_family_peryear = pd.read_csv(Const_LocalPath + "data_family_peryear.csv")
        data_family_peryear['year'] = data_family_peryear['year'].astype('string')
        data_family_allyear = pd.read_csv(Const_LocalPath + "data_family_allyear.csv")
        data_top5family = pd.read_csv(Const_LocalPath + "data_top5family.csv")
        return df_heatmap, data_train_merge_stores,map_base,sales_city_year,map_base_top_five,df_stores_city,df_MaxSales_BiggestStore, df_stores_top_five,data_family_peryear, data_family_allyear, data_top5family
    st.session_state.df_heatmap, st.session_state.data_train_merge_stores,st.session_state.map_base,st.session_state.sales_city_year,st.session_state.map_base_top_five,st.session_state.df_stores_city,st.session_state.df_MaxSales_BiggestStore, st.session_state.df_stores_top_five,st.session_state.data_family_peryear, st.session_state.data_family_allyear, st.session_state.data_top5family = getting_csv()
    finish = datetime.datetime.now()
    st.write(finish-init)

#df_heatmap = pd.read_csv(Const_LocalPath + "Heatmap.csv")
#data_train_merge_stores = pd.read_csv(Const_LocalPath + "data_train_merge_stores.csv")
#map_base = pd.read_csv(Const_LocalPath + "map_base.csv")
#sales_city_year = pd.read_csv(Const_LocalPath +"sales_city_year.csv")
#map_base_top_five = pd.read_csv(Const_LocalPath + "map_base_top_five.csv")
#map_base_top_five['year'] = map_base_top_five['year'].astype('string')
#df_stores_city = pd.read_csv(Const_LocalPath + "df_stores_city.csv")
#df_MaxSales_BiggestStore = pd.read_csv(Const_LocalPath + "df_MaxSales_BiggestStore.csv")
#df_MaxSales_BiggestStore['store_nbr'] = df_MaxSales_BiggestStore['store_nbr'].astype('string')
#df_stores_top_five = pd.read_csv(Const_LocalPath + "df_stores_top_five.csv")
#df_stores_top_five['store_nbr'] = df_stores_top_five['store_nbr'].astype('string')
#data_family_peryear = pd.read_csv(Const_LocalPath + "data_family_peryear.csv")
#data_family_peryear['year'] = data_family_peryear['year'].astype('string')
#data_family_allyear = pd.read_csv(Const_LocalPath + "data_family_allyear.csv")
#data_top5family = pd.read_csv(Const_LocalPath + "data_top5family.csv")

if len(st.session_state) != 0:

    # Create a block on the left - Selection
    # 1st column - Selection of information given by the user

    list_page_name = ['Analysis Page', 'City Prediction', 'Store Prediction', 'Family Prediction']
    selected_page = st.sidebar.selectbox("Select a page", list_page_name)

    with st.sidebar:
        st.header("Please fill up the information")

        #Date selection
        st.subheader('Date selection for analysis')
        date_selection_analysis = st.date_input("Select a date: ",datetime.datetime.strptime('2013-01', '%Y-%m'))
        st.write('Selected date for analysis:', date_selection_analysis)

        st.subheader('Date selection for prediction')
        date_selection_prevision = st.date_input("Select a date: ",datetime.datetime.strptime('2017-01', '%Y-%m'))
        st.write('Selected date for prediction:', date_selection_prevision)

        #City selection
        st.subheader('City selection')
        city_selection = st.selectbox('Select a city: ',np.sort(st.session_state.data_train_merge_stores['city'].unique()))
        st.write('Selected city:', city_selection)

        #Retrieve information from number of store
        array_city_selection_store = np.array(st.session_state.data_train_merge_stores.loc[st.session_state.data_train_merge_stores['city'] == city_selection, 'store_nbr'])
        array_city_selection_store = pd.DataFrame(array_city_selection_store)
        array_city_selection_store = array_city_selection_store.drop_duplicates(subset=0).sort_values(by = 0, ascending=True)
        #array_city_selection_store = np.array(array_city_selection_store)
        st.write ('Your city has ',len(array_city_selection_store),
        ' out of 54 stores')
        percentage = (len(array_city_selection_store)/Const_Store_nbr)*100
        percentage = round(percentage, 2)
        st.write('Your city has ',percentage , '% of stores')

        #Retrieve store list from city and Store selection
        st.subheader('Store selection')
        store_selection = st.selectbox('Select a store from your city: ',array_city_selection_store)
        st.write('Selected store:', store_selection)

        #Family selection
        df_all_family = pd.DataFrame(st.session_state.data_train_merge_stores['family'].unique())
        #df_all_family.columns =['family']
        #df_all_family.index = np.arange(1, len(df_all_family) + 1)
        family_selection = st.multiselect('Select a list of families for analysis: ',df_all_family)
        st.write('Selected list:' )
        st.table(family_selection)

        #Family selection for prediction
        family_prediction_selection = st.selectbox('Select one family for prediction: ',df_all_family)
        st.write('Selected family for prediction: ', family_prediction_selection)

    def main_page ():
        st.header("1) Data visualization")

        # Create a first part for analysis on cities
        with st.expander("1.1) General analysis on sales and cities"):

            #col1, col2 = st.columns(2)

            #with col1:
            st.caption("a) Map with cities and sales")
            px.set_mapbox_access_token('pk.eyJ1IjoibXJkYXJhdWpvIiwiYSI6ImNsM3hsY2c2NzAzcHEzYm1oYmliZHc5aXoifQ.1E3p2I8p8bEkHSPJDzUXWQ')
            df = px.data.election_geojson()
            fig = px.scatter_mapbox(data_frame=st.session_state.sales_city_year, lat="Lat", lon="Lon", color="city", size="sales",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=45, zoom=5, mapbox_style="carto-positron")



            st.write(fig)

            #with col2:
            st.caption("b) Sales for top 5 cities")
            fig = px.bar(st.session_state.map_base_top_five, x='city', y='sales', color='year')
            st.write(fig)

        #                     fig = make_subplots(rows=1, cols=2)
         #       fig.add_trace(
          #          fig2.data[0],
           #         row=1,
            #        col=1,
            #    )
             #   fig.add_trace(
              #      fig2.data[0],
               #     row=1,
                #    col=2,
                #)
                #fig

        #Create a second part for analysis on stores
        with st.expander("1.2) General analysis on sales and stores") :

            st.caption("a) Number on stores on each city")
            fig = px.pie(st.session_state.df_stores_city, values = 'store_nbr', names = 'city')
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.write(fig)

            st.caption("b) Biggest store on each city")
            fig = px.bar(st.session_state.df_MaxSales_BiggestStore, x='store_nbr', y='sales', color = 'city')
            st.write(fig)

            st.caption("c) Sales for top 5 stores")
            fig = px.bar(st.session_state.df_stores_top_five, x='store_nbr', y='sales', color = 'city')
            st.write(fig)

            st.caption("d) Sales for all stores on selected city")
            data_selection_bycity = st.session_state.data_train_merge_stores[st.session_state.data_train_merge_stores['city'] == city_selection]
            data_selection_bycity = pd.DataFrame(data_selection_bycity.groupby(['store_nbr'])['sales'].sum()).reset_index()
            data_selection_bycity['store_nbr'] = data_selection_bycity['store_nbr'].astype('string')
            data_selection_bycity = data_selection_bycity.sort_values('sales',ascending= False)
            if len(array_city_selection_store) > 1 :
                fig = px.bar(data_selection_bycity, x ='store_nbr',y='sales', color = 'store_nbr')
                st.write(fig)
            elif len(array_city_selection_store) == 1 :
                st.write('There is only one store in the city that has sold ',int(data_selection_bycity['sales'].sum()),
                            ' products from 2013 to 2016')

            st.caption("e) Sales on selected store")
            data_selection_bystore = st.session_state.data_train_merge_stores[st.session_state.data_train_merge_stores['store_nbr'] == store_selection]
            data_selection_bystore = data_selection_bystore.groupby(['year'])['sales'].sum().reset_index()
            data_selection_bystore['year'] = data_selection_bystore['year'].astype('string')
            fig = px.line(data_selection_bystore, x ='year',y='sales')
            st.write(fig)

            st.caption("f) Sales on selected store for 12 months")
            st.write("Analysis for year ", date_selection_analysis.year)
            data_selection_bymonth_bystore = st.session_state.data_train_merge_stores[st.session_state.data_train_merge_stores['store_nbr'] == store_selection]
            data_selection_bymonth_bystore = data_selection_bymonth_bystore[data_selection_bymonth_bystore['year'] == date_selection_analysis.year]
            data_selection_bymonth_bystore = data_selection_bymonth_bystore.groupby(['month'])['sales'].sum().reset_index()
            data_selection_bymonth_bystore['month'] = data_selection_bymonth_bystore['month'].astype('string')
            fig = px.line(data_selection_bymonth_bystore, x ='month',y='sales')
            st.write(fig)

        with st.expander("1.3) General analysis on sales and families") :

            st.caption("a) Sales each year for all families")
            fig = plt.figure(figsize=(12,10))
            sns.lineplot(x='year', y='sales', data=st.session_state.data_family_peryear, hue='family')
            plt.xticks(rotation=90)
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
            st.pyplot(fig)

            st.caption("b) Total sales for all families for all years")
            fig = px.bar(data_frame=st.session_state.data_family_allyear, x='family', y='sales', color='family')
            st.write(fig)

            st.caption("c) Sales for top 5 families")
            fig = px.bar(data_frame=st.session_state.data_top5family, x='family', y='sales', color='family')
            st.write(fig)

            st.caption("d) Sales for selected families on all stores")
            family_selection_df = st.session_state.data_family_peryear[st.session_state.data_family_peryear['family'].isin(family_selection)]
            family_selection_df['year'] = family_selection_df['year'].astype('string')
            fig = plt.figure(figsize=(12,10))
            sns.lineplot(x='year', y='sales', data=family_selection_df, hue = 'family')
            plt.xticks(rotation=90)
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
            st.pyplot(fig)

            st.caption("e) Sales for selected families on selected store")
            store_family_selection_df = st.session_state.data_train_merge_stores[st.session_state.data_train_merge_stores['store_nbr']==store_selection]
            store_family_selection_df = store_family_selection_df[store_family_selection_df['family'].isin(family_selection)]
            fig = px.bar(store_family_selection_df, x='family', y='sales', color='family')
            st.write(fig)


    def page2():
        st.markdown("Prediction based on the city")
        st.write("Let's predict the number of sales for the city ", city_selection, " for 12 months of the year ", date_selection_prevision.year)

        def API_City(year, city):
            year_list=[year]*12
            city_list=[city]*12
            params = {
                'year': year_list,
                'month': Const_month_predict,
                'city': city_list
            }
            response = requests.get(Const_url_predict_city, params=params)
            return response.json()

        city_return = pd.DataFrame(API_City(date_selection_prevision.year, city_selection)).reset_index()
        city_return.rename(columns = {'index':'month', 'sales_city_year':'sales'}, inplace = True)
        city_return['month'] = city_return['month'].astype('int')
        city_return = city_return.sort_values(by = 'month', ascending=True)
        st.write("Dataframe Prediction 12 months in year ", date_selection_prevision.year, "for city " , city_selection)
        st.dataframe(city_return)
        fig = px.line(city_return, x ='month',y='sales')
        st.write("Plot Prediction for 12 months in year ", date_selection_prevision.year, "for city " , city_selection)
        st.write(fig)


    def page3():
        st.markdown("Prediction based on the store")
        st.write("Let's predict the number of sales in the city", city_selection,
                 " for the store ", store_selection, " for 12 months of the year ", date_selection_prevision.year)

        def API_Store(year, city, store_nbr):
            year_list=[year]*12
            city_list=[city]*12
            store_list=[store_nbr]*12

            params = {
                'year': year_list,
                'month': Const_month_predict,
                'city': city_list,
                'store_nbr': store_list
            }
            response = requests.get(Const_url_predict_store, params=params)
            return response.json()

        store_return = pd.DataFrame(API_Store(date_selection_prevision.year, city_selection, store_selection)).reset_index()
        store_return.rename(columns = {'index':'month', 'sales_store_year':'sales'}, inplace = True)
        store_return['month'] = store_return['month'].astype('int')
        store_return = store_return.sort_values(by = 'month', ascending=True)
        st.write("Dataframe Prediction 12 months in year ", date_selection_prevision.year, "for city " , city_selection, " and store ",
                 store_selection)
        st.dataframe(store_return)
        fig = px.line(store_return, x ='month',y='sales')
        st.write("Plot Prediction for 12 months in year ", date_selection_prevision.year, "for city " , city_selection, " and store ",
                 store_selection)
        st.write(fig)


    def page4():
        st.markdown("Prediction based on store and family")
        st.write("Let's predict the number of sales in the city ", city_selection, " for the store ", store_selection,
                 " for 12 months of the year ", date_selection_prevision.year,
                    "for the family ", family_prediction_selection)

        def API_Family(year, city, store_nbr, family):
            year_list=[year]*12
            city_list=[city]*12
            store_list=[store_nbr]*12
            family_list = [family]*12

            params = {
                'year': year_list,
                'month': Const_month_predict,
                'city': city_list,
                'store_nbr': store_list,
                'family': family_list
            }
            response = requests.get(Const_url_predict_family, params=params)
            return response.json()

        family_return = pd.DataFrame(API_Family(date_selection_prevision.year, city_selection, store_selection, family_prediction_selection)).reset_index()
        family_return.rename(columns = {'index':'month', 'sales_family_year':'sales'}, inplace = True)
        family_return['month'] = family_return['month'].astype('int')
        family_return = family_return.sort_values(by = 'month', ascending=True)
        st.write("Dataframe Prediction 12 months in year ", date_selection_prevision.year, "for city " , city_selection, " and store ",
                 store_selection, " and family ", family_prediction_selection)
        st.dataframe(family_return)
        fig = px.line(family_return, x ='month',y='sales')
        st.write("Plot Prediction for 12 months in year ", date_selection_prevision.year, "for city " , city_selection, " and store ",
                 store_selection, " and family ", family_prediction_selection)
        st.write(fig)







    #Code to have different page on streamlit
    page_names_to_funcs = {
        "Analysis Page" : main_page,
        "City Prediction": page2,
        "Store Prediction": page3,
        "Family Prediction": page4
    }

    page_names_to_funcs[selected_page]()

#Session States
st.session_state.count += 1
st.write('Count = ', st.session_state.count)
