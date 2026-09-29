# 🚲 Bike Sharing Demand Prediction

Machine learning project for predicting bike rental demand using the Kaggle Bike Sharing Demand dataset.

## Project Objective

The objective is to predict the total number of bike rentals (`count`) based on:

* Weather conditions
* Temperature
* Humidity
* Windspeed
* Season
* Holiday
* Working day
* Date and time information

## Dataset

**Source:** Kaggle Bike Sharing Demand Competition

Dataset size:

* 10,886 records
* 12 original columns

## Feature Engineering

The `datetime` column is converted into:

* Year
* Month
* Day
* Hour

The following columns are removed:

```text
datetime
casual
registered
```

Final model features:

```text
season
holiday
workingday
weather
temp
atemp
humidity
windspeed
year
month
day
hour
```

## Model

The final prototype uses:

```text
GradientBoostingRegressor
```

Parameters:

```text
n_estimators = 300
learning_rate = 0.1
max_depth = 7
random_state = 42
```

Train/test split:

```text
80% training
20% testing
random_state = 42
```

Preprocessing:

```text
StandardScaler
```

## Notebook Performance

The provided notebook reports:

```text
Training R²: 99.31%
Testing R² : 95.38%
```

The application provides an interactive interface for entering bike-sharing conditions and receiving predicted rental demand.

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

## Disclaimer

The prediction is a machine-learning estimate based on the dataset and model used in the project. It should not be interpreted as a guaranteed real-world rental count.
