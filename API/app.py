import streamlit as st
import pandas as pd
from datetime import time
from datetime import date
from datetime import timedelta
import requests
import numpy as np
import matplotlib.pyplot as plt



st.markdown("# Ticket Prediction 🎉")
st.sidebar.markdown("# Xintong's small project 🎉")

st.sidebar.markdown("Ticket Price Prediction")


st.markdown('Choose the features and date of the events that you want to go, and I will assist you in making the wise decision!🥳')




event_types = ['Arts & Theatre', 'Sports', 'Music', 'Miscellaneous']

event_segment = st.selectbox('Select Event Genre:', event_types)


event_subsections = {
    'Music': [
        'Reggae', 'Rock', 'Country', 'R&B', 'Pop', 'Dance/Electronic',
        'Latin', 'Other', 'Blues', 'Metal', 'Undefined', 'World',
        'Hip-Hop/Rap', 'Jazz', 'Alternative', 'Folk', 'Religious', 'Classical', 'Holiday'
    ],
    'Arts & Theatre': [
        'Fine Art', 'Magic & Illusion', 'Comedy',
       'Circus & Specialty Acts', 'Miscellaneous Theatre', 'Theatre',
       'Performance Art', 'Dance', 'Spectacular', 'Variety',
       'Classical', "Children's Theatre"
    ],
    'Sports': [
        'Soccer', 'Baseball', 'Equestrian', 'Motorsports/Racing',
       'Football', 'Volleyball', 'Rodeo', 'Basketball', 'Miscellaneous',
       'Golf', 'Lacrosse', 'Martial Arts'
    ],
    'Miscellaneous': [
        'Psychics/Mediums/Hypnotists', 'Undefined', 'Family',
       'Community/Civic', 'Food & Drink', 'Ice Shows',
       'Hobby/Special Interest Expos', 'Fairs & Festivals'
    ]
}

event_subsection = st.selectbox("Select Event Subsection:", event_subsections[event_segment])

state_code = ['NY', 'NV', 'MI', 'WA', 'CA', 'SC', 'TX', 'WI', 'KY', 'IL', 'DC',
       'OH', 'TN', 'MA', 'PA', 'AZ', 'MN', 'GA', 'NJ', 'NC', 'UT', 'MD',
       'ID', 'VA', 'CO', 'AK', 'MO', 'IA', 'FL', 'NE', 'AL', 'OK', 'CT',
       'OR', 'MS', 'IN', 'SD', 'NM', 'LA', 'ME', 'KS', 'MT']

state_city_mapping = {
    'AK': ['Bethel', 'Palmer'],
    'NV': ['Las Vegas', 'Reno', 'Stateline'],
    'MI': ['Grand Rapids', 'Detroit', 'Rochester Hills'],
    'WA': ['Seattle', 'Airway Heights', 'Tacoma', 'Spokane'],
    'ID': ['Lewiston', 'Nampa'],
    'CA': ['San Diego', 'Ontario', 'Los Angeles', 'Lake Elsinore', 'Hollywood', 'Inglewood', 'Santa Cruz', 'San Francisco', 'Ojai', 'Cerritos', 'Long Beach', 'Temecula', 'Santa Clarita', 'Anaheim', 'Coachella', 'Oakland', 'Rohnert Park', 'West Sacramento', 'Sonoma', 'Wheatland'],
    'SC': ['Charleston', 'North Charleston', 'Simpsonville'],
    'TX': ['San Antonio', 'Dallas', 'Houston', 'Fort Worth', 'Grand Prairie', 'Austin', 'Arlington', 'El Paso', 'Laredo'],
    'WI': ['Madison', 'Milwaukee'],
    'KY': ['Louisville'],
    'IL': ['Chicago', 'Hoffman Estates', 'Peoria', 'Country Club Hills'],
    'DC': ['Washington'],
    'OH': ['Columbus', 'Kettering', 'Sylvania', 'Maumee', 'Dayton', 'Cincinnati', 'Huber Heights'],
    'NY': ['New York', 'Bronx', 'Buffalo', 'Fishkill', 'Kingston', 'Saratoga Springs', 'Philadelphia', 'Brooklyn', 'Niagara Falls', 'Poughkeepsie'],
    'MA': ['Boston'],
    'PA': ['Pittsburgh', 'Reading', 'Bethlehem', 'Allentown', 'Jim Thorpe', 'Villanova'],
    'AZ': ['Laveen', 'Tempe', 'Tucson', 'Prescott Valley', 'Phoenix'],
    'MN': ['Minneapolis', 'Prior Lake', 'Duluth', 'Mankato'],
    'IN': ['Bloomington', 'Indianapolis', 'Elkhart'],
    'GA': ['Atlanta', 'Macon', 'Savannah', 'Mableton'],
    'NJ': ['Atlantic City', 'East Rutherford', 'Asbury Park', 'Elizabeth', 'Newark', 'Montclair', 'Red Bank'],
    'NC': ['Raleigh', 'Holly Springs', 'Cary', 'Winston Salem', 'Durham', 'Fayetteville', 'Greensboro'],
    'UT': ['Salt Lake City', 'South Jordan', 'Herriman'],
    'MD': ['Hagerstown', 'Salisbury'],
    'NE': ['Lincoln', 'La Vista', 'Omaha'],
    'VA': ['Vienna', 'Tysons', 'Norfolk', 'Charlottesville', 'Richmond'],
    'CO': ['Denver', 'Colorado Springs'],
    'MO': ['Saint Louis', 'Camdenton', 'Jefferson City', 'Columbia'],
    'IA': ['Des Moines', 'Sioux City'],
    'FL': ['Tampa', 'Fort Lauderdale', 'Orlando', 'Miami', 'Pensacola', 'Tallahassee', 'Ft Lauderdale'],
    'CT': ['Bridgeport', 'Ledyard', 'Uncasville'],
    'LA': ['Winnsboro', 'New Orleans', 'Metairie'],
    'TN': ['Knoxville', 'Memphis', 'Nashville', 'Chattanooga', 'Bristol'],
    'OR': ['Troutdale', 'Salem', 'Portland'],
    'MS': ['Jackson'],
    'OK': ['El Reno', 'Oklahoma City', 'Durant', 'Enid'],
    'NM': ['Albuquerque'],
    'AL': ['Birmingham', 'Huntsville'],
    'SD': ['Deadwood', 'Sioux Falls'],
    'VA': ['Vienna', 'Tysons', 'Norfolk', 'Charlottesville', 'Richmond'],
    'KS': ['Bonner Springs', 'Lawrence'],
    'MT': ['Bozeman'],
    'RI': [],
    'NH': [],
}

#City
state_code = st.selectbox("Which state would you like to see the events:", state_code)
event_city = st.selectbox("Which city would you like to see the event:", state_city_mapping[state_code])


hot = st.selectbox("Is the event hot:", ['Yes','No','Unsure'])

hot = 1 if hot == 'Yes' else 0

from datetime import datetime


start_time = st.slider(
    "When do you want to see the event?",
    value=(datetime(2025,7,22,0,0),datetime(2025,12,31,23,59)),
    min_value=datetime(2025,6,2,0,0),
    format="MM/DD/YY",
)

st.write("Time Range:", start_time)

days_to_event = (start_time[0]-datetime.today()).days

d = st.date_input("When's the on-sale date?", value = 'today',max_value='today')

days_since_sale = (d - datetime.today().date()).days

st.metric(label="Days until the event:", value=f"{days_to_event} Days")


st.metric(label="Days since the sale:", value=f"{days_since_sale} Days")

input_data = {
            "CLASSIFICATION_SEGMENT":event_segment, 
             "CLASSIFICATION_GENRE":event_subsection,
             'HOT_EVENT': hot,
             'VENUE_STATE_CODE':state_code,
             'VENUE_CITY':event_city,
             'time_to_start':days_to_event,
             'time_since_start_sale':days_since_sale
              } 



response = requests.post('https://nanako2001-561457278990.us-west2.run.app/predict_ticket_price', json=input_data, headers = {"content-type":"application/json"})

prediction = response.json()
prediction = list(prediction.values())[0]



st.metric(label="The Predicted Ticket Price for your selected earliest events", value=f"$ {prediction}")


##draw the pictures 

base_input_data = {
    "CLASSIFICATION_SEGMENT": event_segment, 
    "CLASSIFICATION_GENRE": event_subsection,
    "HOT_EVENT": hot,
    "VENUE_STATE_CODE": state_code,
    "VENUE_CITY": event_city,
    "time_since_start_sale": days_since_sale,
    'time_to_start':days_to_event
}

# Build a visualization in the selected date range

price_over_time =[]

days_diff = (start_time[1] - start_time[0]).days

st.markdown(':rainbow[Below is how the ticket price will change over your selected time period:] :tulip: :balloon: :admission_tickets:')


for t in range(0, days_diff+1):
        input_data = base_input_data.copy()
        input_data['time_to_start'] = t+days_to_event
        
        response = requests.post(
            'https://nanako2001-561457278990.us-west2.run.app/predict_ticket_price',
            json=input_data,
            headers={"content-type": "application/json"}
        )
        prediction = response.json()
        prediction = list(prediction.values())[0]
        price_over_time.append({
                'time_period': (start_time[0] + timedelta(days=t)).date(),
                'predicted_price': prediction
            })

price_pic = pd.DataFrame(price_over_time)


st.line_chart(price_pic.set_index('time_period'),
            x_label='Event Start Date',
            y_label='Price',
            color= "#0000FF"
            )




# 列表记录
results = []


# 请求并记录数据
for t in range(int(days_to_event), -2, -1):
    input_data = base_input_data.copy()
    input_data['time_to_start'] = t
    
    response = requests.post(
        'https://nanako2001-561457278990.us-west2.run.app/predict_ticket_price',
        json=input_data,
        headers={"content-type": "application/json"}
    )
    prediction = response.json()
    prediction = list(prediction.values())[0]
    results.append({
            'time_to_start': t,
            'predicted_price': prediction
        })



# Turn that into DataFrame
chart_data = pd.DataFrame(results)

chart_data_sorted = chart_data.sort_values('time_to_start', ascending=False)


#Ticketprice from today to the event_start_date (Earliest)
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')  # 整个画布背景
ax.set_facecolor('black')  

ax.plot(chart_data_sorted['time_to_start'], chart_data_sorted['predicted_price'], marker='o')
ax.set_xlabel('Days to Event (time_to_start)')
ax.set_ylabel('Predicted Price')
ax.set_title('Predicted Price vs Days to Event')
# 设置坐标轴标签、标题的颜色
ax.tick_params(colors='white')    # 坐标刻度颜色
ax.xaxis.label.set_color('white') # x轴label颜色
ax.yaxis.label.set_color('white') # y轴label颜色
ax.title.set_color('white') 

ax.invert_xaxis()  # 👈 反转x轴方向 80到0

#st.pyplot(fig)

if st.button('Click me if you wonder whether you should buy it NOW👈 👀'):
    st.pyplot(fig)
    if chart_data_sorted['predicted_price'].iloc[0] >= chart_data_sorted['predicted_price'].iloc[-1]:
        st.write('No, you probably should wait a little bit. Procrastination actually helps!🎆🥳')
    else:
         st.write('Oops..Buy it now to save money immediately💰‼️‼️')


happy = st.checkbox("Do you agree that I get an A in 418?")

if happy:
    st.write("🥳🥳Great!!Thank you!!🥳🥳")
