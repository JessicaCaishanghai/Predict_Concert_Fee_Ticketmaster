import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score



result = pd.read_csv('result.csv')

result['HOT_EVENT'] = result['HOT_EVENT'].astype(int) 
result['average_price'] = result[['min_price','max_price']].mean(axis=1)

features = [
    'CLASSIFICATION_SEGMENT', 
    'CLASSIFICATION_GENRE',
    'HOT_EVENT',
    'VENUE_CITY', 
    'VENUE_STATE_CODE', 
    'time_to_start',# how long it takes until the event kicks off
    'time_since_start_sale' # how long has it been since the start sale
]
X = result[features]
y = result['average_price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

categorical_features = ['CLASSIFICATION_SEGMENT', 'CLASSIFICATION_GENRE', 'HOT_EVENT', 'VENUE_CITY', 'VENUE_STATE_CODE']#'VENUE_ZIP_CODE']

for col in categorical_features:
    X_train[col] = X_train[col].astype(str).fillna('missing')
    X_test[col] = X_test[col].astype(str).fillna('missing')

model = CatBoostRegressor(
    iterations=100,
    learning_rate=0.1,
    depth=6,
    cat_features=categorical_features,
    verbose=100
)

model.fit(X_train, y_train)



def predict(dict_values, features=features, model=model):
    x = pd.DataFrame([{col: dict_values[col] for col in features}])
    y_pred = model.predict(x)[0]
    return y_pred