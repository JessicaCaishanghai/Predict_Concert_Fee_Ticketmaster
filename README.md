# Predict_Concert_Fee_Ticketmaster

This is a project to predict whether concert tickets price is good using Ticketmaster API, Selenium and flask.

You can access the Streamlit app hosted on Google Cloud Run [here](https://app-561457278990.us-west2.run.app)


Test input for terminal:
```
curl -H "Content-Type: application/json" -X POST -d '{"CLASSIFICATION_SEGMENT":"Arts & Theatre","CLASSIFICATION_GENRE":"Magic & Illusion","HOT_EVENT":"0","VENUE_CITY":"Las Vegas","VENUE_STATE_CODE":"NV","time_to_start":"85.0","time_since_start_sale":"-146.0"}' "https://nanako2001-561457278990.us-west2.run.app/predict_ticket_price"
```
Expected output:
```
{"predict ticket price":91.64586428080075}
```


## Background

The Ticketmaster Ticket Price Prediction App is a web-based application designed to predict the price of event tickets using historical event data. It leverages a machine learning model trained on a variety of event features to help users decide the optimal time to purchase tickets.

The data utilized was obtained via Ticketmaster API and selenium.

The dataset used for training includes the following features:

Classification Segment: The broad category of the event, such as Arts & Theatre, Sports, Music, or Miscellaneous.

Classification Genre: A more specific sub-category based on the segment (e.g., Fine Art under Arts & Theatre).

Hot Event: A binary indicator of whether the event is categorized as a "hot" or highly demanded event.

Venue City: The city where the event takes place.

Venue State Code: The two-letter state code of the venue's location.

Time to Start: The number of days remaining until the event starts.

## Methodology

Catboosting was used to fit the model. Catboost regressor is especially utilized. 

Given the nature of the dataset, which contains multiple categorical variables such as event segment, genre, venue city, and state code, CatBoost’s native handling of categorical features allowed for an efficient and accurate modeling process without the need for extensive feature engineering like one-hot encoding.

## Light EDA

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 818 entries, 0 to 817
Data columns (total 7 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   CLASSIFICATION_SEGMENT  818 non-null    object 
 1   CLASSIFICATION_GENRE    812 non-null    object 
 2   HOT_EVENT               818 non-null    int64  
 3   VENUE_CITY              818 non-null    object 
 4   VENUE_STATE_CODE        818 non-null    object 
 5   time_to_start           815 non-null    float64
 6   time_since_start_sale   814 non-null    float64
dtypes: float64(2), int64(1), object(4)
memory usage: 44.9+ KB



## Results

You can see the model in action via visiting the streamlit app. As a user, you can enter your favourite kind of events and all the dates that you are available by the slider. You can also choose where you intend to see the events: Los Angeles or New York. Those predictors help output the ticket price for the earliest available date, and it will later generate a visualization of the price in your available date range. To utilize this, you can look at [here](https://app-561457278990.us-west2.run.app). Moreover, if it isn't running anymore, you can choose to see my slides for final presentation. [presentation](https://github.com/JessicaCaishanghai/Predict_Concert_Fee_Ticketmaster/blob/main/slides/418Final%20Where%E2%80%99s%20the%20best%20seats_%20%20Predicting%20Concert%20Prices%20To%20Assist%20Decision%20(2).pdf).

