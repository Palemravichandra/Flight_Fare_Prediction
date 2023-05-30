import streamlit as st
import pandas as pd
import pickle
#import sklearn
import datetime

# lpoading the model to the app
model = pickle.load(open("flight_rf.pkl", "rb"))

st.markdown("<h1 style='text-align: center; color:#0000FF;'>FLIGHT FARE PREDICTION APP</h1>", unsafe_allow_html=True)
col1,col2,col3=st.columns(3)
with col1:
    st.subheader(':violet[DEPARTURE]')
    date_dep = st.date_input("Select Departure Date")

    dep_time = st.time_input('Select Departure Time', value=datetime.time(14, 00))
    # st.write(time.hour,time.minute)
    # st.write(date_dep)
    # year,month,date=dep.year,dep.month,dep.day
    # st.write(year,month,date)
    # hours = st.slider('select start hours', 0, 24,1)
    # minute=st.slider('select start minutes', 0, 60,1)
    # date_dep=datetime(dep.year,dep.month,dep.day, hours, minute)
    # st.write(date_dep)
    Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
    # st.write("Journey Date : ",Journey_day, Journey_month)

    # Departure
    Dep_hour = int(dep_time.hour)
    Dep_min = int(dep_time.minute)
    # st.write("Departure : ",Dep_hour, Dep_min)

    st.subheader(':violet[SOURCE]')
    data = ['Delhi', 'Kolkata', 'Banglore', 'Mumbai', 'Chennai']
    Source = st.selectbox('Select source', data)
    if (Source == 'Delhi'):
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    elif (Source == 'Kolkata'):
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0
        s_Chennai = 0

    elif (Source == 'Mumbai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1
        s_Chennai = 0

    elif (Source == 'Chennai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 1

    else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

with col2:
    st.subheader(':violet[ARRIVAL]')
    date_arr =st.date_input("Select Arrival Date")
    arr_time = st.time_input('Select Arrival Time', value=datetime.time(00, 00))
    #st.write(arr_time.hour,arr_time.minute)
    Arrival_hour = int(arr_time.hour)
    Arrival_min = int(arr_time.minute)
    #st.write("Arrival : ", Arrival_hour, Arrival_min)

    # Duration
    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_min - Dep_min)
    #st.write("Duration : ", dur_hour, dur_min)


    st.subheader(':violet[DESTINATION]')
    data = ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad']
    destination=st.selectbox('Select Destination', data)
    if (destination== 'Cochin'):
        d_Cochin = 1
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (destination == 'Delhi'):
        d_Cochin = 0
        d_Delhi = 1
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (destination== 'New_Delhi'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (destination == 'Hyderabad'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0

    elif (destination== 'Kolkata'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1

    else:
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0



with col3:
    st.subheader(':violet[AIRLINES]')
    data=['Jet Airways','IndiGo','Air India','Multiple carriers','SpiceJet','Vistara',
          'Air Asia','GoAir','Multiple carriers Premium economy','Vistara Premium economy',
          'Jet Airways Business']
    airline=st.selectbox('Select Airlines',data)
    if (airline == 'Jet Airways'):
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'IndiGo'):
        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Air India'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Multiple carriers'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'SpiceJet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Vistara'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 1
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'GoAir'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 1
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Multiple carriers Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Jet Airways Business'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 1
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline == 'Vistara Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 1
        Trujet = 0

    elif (airline == 'Trujet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 1

    else:
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    # Total Stops
    #st.button("First button")
    
    st.markdown("****")
    st.text("")
    st.text("")
    #st.button("Second button")
    st.subheader(':violet[STOPS]')
    data=['0','1','2','3','4']
    Total_stops = int(st.selectbox('Select No.of Stops',data))
    # print(Total_stops)
    #st.markdown("******")
submit=st.button('SUBMIT')
if submit:
    prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])

    output=round(prediction[0],2)
    st.write('## :green[PREDICTED FLIGHT FARE IS:] ', output)
st.write( f'<h5 style="color:rgb(0, 153, 153,0.35);">App Created by RAVI CHANDRA PALEM </h5>', unsafe_allow_html=True )



