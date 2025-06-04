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

The Ticketmaster Ticket Price Prediction App is **a web-based application** designed to predict the price of event tickets using historical event data. It leverages a machine learning model trained on a variety of event features to help users decide the optimal time to purchase tickets. The data utilized was obtained via Ticketmaster API and selenium.

The dataset used for training includes the following features:

**Classification Segment**: The broad category of the event, such as Arts & Theatre, Sports, Music, or Miscellaneous.

Classification Genre: A more specific sub-category based on the segment (e.g., Fine Art under Arts & Theatre).

Hot Event: A binary indicator of whether the event is categorized as a "hot" or highly demanded event.

Venue City: The city where the event takes place.

Venue State Code: The two-letter state code of the venue's location.

Time to Start: The number of days remaining until the event starts.

## Methodology

Catboosting was used to fit the model. Catboost regressor is especially utilized. 

Given the nature of the dataset, which contains multiple categorical variables such as event segment, genre, venue city, and state code, CatBoost’s native handling of categorical features allowed for an efficient and accurate modeling process without the need for extensive feature engineering like one-hot encoding.

### ✨Model Details

The feature importance of this catboosting model. 

| Feature                   | Importance   |
|----------------------------|--------------|
| time_since_start_sale      | 34.390829    |
| CLASSIFICATION_SEGMENT     | 17.299283    |
| CLASSIFICATION_GENRE       | 14.636876    |
| time_to_start              | 14.476071    |
| VENUE_STATE_CODE           | 12.818305    |
| VENUE_CITY                 | 4.824313     |
| HOT_EVENT                  | 1.554324     |


### 📈 Model Performance

- **Mean Squared Error (MSE)**: 2849.67
- **R-squared (R²)**: 0.5340




## Light EDA

This is the summary of the dataset that contain 818 rows with 84 columns. Only 7 columns were chosen to fit the model.

| #   | Column                  | Non-Null Count | Dtype    |
|-----|--------------------------|---------------|----------|
| 0   | CLASSIFICATION_SEGMENT    | 818           | object   |
| 1   | CLASSIFICATION_GENRE      | 812           | object   |
| 2   | HOT_EVENT                 | 818           | int64    |
| 3   | VENUE_CITY                | 818           | object   |
| 4   | VENUE_STATE_CODE          | 818           | object   |
| 5   | time_to_start             | 815           | float64  |
| 6   | time_since_start_sale     | 814           | float64  |



### Average price by event segment

![Figure1](https://github.com/JessicaCaishanghai/Predict_Concert_Fee_Ticketmaster/blob/main/images/group_average.png)


### Average Price by States

We can see how affordable to buy tickets across different states in United States.

![Figure2](https://github.com/JessicaCaishanghai/Predict_Concert_Fee_Ticketmaster/blob/main/images/States.png)

### Price trend 

Knowing when to buy the tickets is important. This picture shows how the ticket price of a hot pop music concert in Los Angeles will change when the events start tomorrow or 80 days later.

![Figure3](https://github.com/JessicaCaishanghai/Predict_Concert_Fee_Ticketmaster/blob/main/images/TimeSeries1.png)



## Results

You can see the model in action via visiting the streamlit app. As a user, you can enter your favourite kind of events and all the dates that you are available by the slider. You can also choose where you intend to see the events: Los Angeles or New York. Those predictors help output the ticket price for the earliest available date, and it will later generate a visualization of the price in your available date range. To utilize this, you can look at [here](https://app-561457278990.us-west2.run.app). Moreover, if it isn't running anymore, you can choose to see my slides for final presentation. [presentation](https://github.com/JessicaCaishanghai/Predict_Concert_Fee_Ticketmaster/blob/main/slides/418Final%20Where%E2%80%99s%20the%20best%20seats_%20%20Predicting%20Concert%20Prices%20To%20Assist%20Decision%20(2).pdf).




## Structure

There is a backend API, an interactive front end published through Google run using Streamlit and Flask framework. 
The **API** folder: Building API and Predictive Model like `server.py` and `predict.py`.
The **APP** folder: Building APP interface using Streamlit. 
The **EDA_and_Model**: Process of model training and light EDA. Some explorations on the European Ticketmaster market. 
The **images** folder: EDA pictures.
The **slides**: Slides for presentations.



