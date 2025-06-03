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


