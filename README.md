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

## Structure

There is a backend API, an interactive front end published through Google run using Streamlit and Flask framework. 
- **API** folder: Building API and Predictive Model like `server.py` and `predict.py`.
- **APP** folder: Building APP interface using Streamlit. 
- **EDA_and_Model**: Process of model training and light EDA. Some explorations on the European Ticketmaster market. 
- **images** folder: EDA pictures.
- **slides**: Slides for presentations.



