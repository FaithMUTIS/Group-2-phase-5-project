# Car Valuation Project
## Table of Contents
- [Car Valuation Project](#car-valuation-project)
  - [Table of Contents](#table-of-contents)
  - [1. Business Understanding](#1-business-understanding)
    - [Project Overview](#project-overview)
    - [Business Problem](#business-problem)
    - [Objectives](#objectives)
    - [Stakeholders](#stakeholders)
  - [2. Data Understanding](#2-data-understanding)
    - [Data Overview](#data-overview)
    - [Sources and Collection](#sources-and-collection)
    - [Data Description](#data-description)
    - [Data Exploration](#data-exploration)
  - [3. Data Preprocessing](#3-data-preprocessing)
    - [Data Cleaning](#data-cleaning)
    - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
    - [Feature Engineering](#feature-engineering)
    - [Correlation Analysis](#correlation-analysis)
    - [Feature Scaling](#feature-scaling)
    - [Feature Selection](#feature-selection)
  - [4. Modeling](#4-modeling)
    - [Regression and Ensemble Techniques](#regression-and-ensemble-techniques)
  - [5. Evaluation and Recommendations](#5-evaluation-and-recommendations)
    - [Evaluation Metrics](#evaluation-metrics)
    - [Recommendations](#recommendations)
  - [6. Model Deployment](#6-model-deployment)
    - [Deployment Strategy](#deployment-strategy)
    - [Model Deployment Steps](#model-deployment-steps)
  - [Installation and Usage](#installation-and-usage)
    - [Clone the Repository](#clone-the-repository)

---

## 1. Business Understanding

### Project Overview
The Car Valuation System aims to develop a data-driven model that accurately estimates or predicts the market value of used cars based on various features such as make, model, age, mileage, fuel type, and more. By applying data science and  machine learning techniques, the system will provide a solution for determining the value of used cars, which is valuable for sellers, buyers, car dealerships, and financial institutions.
### Business Problem
The primary goal of this project is to develop a strong reliable predictive model for car valuation that the stakeholders can trust for accurate pricing estimates, thereby reducing uncertainties and developing informed decision-making.
The price of used cars is influenced by several factors including car's age, condition, location, and demand for specific models. This can create challenges for stakeholders in that:
- Buyers: They may overpay for a car due to lack of enough information about its true market value.
- Sellers: They may price their vehicles too low, leading to loss of potential profit.
- Dealerships: They need an efficient way to assess car values for pricing and providing fair trade-in offers.
- Financial Institutions: They rely on accurate car valuations for loan approvals and insurance policies.

### Objectives
- **1**: Build a machine learning model to predict the market value of a car based on car-specific features.
- **2**:Include data from different cities to ensure the model accounts for different regional pricing variations.
- **3**:Evaluate and validate the model using standard regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R²) score to ensure the accuracy and reliability of the predictions.
- **4**: Provide recommendations for businesses on price optimization and market strategies.
- **5**: Deploy the model in a way that businesses can use it to get real-time pricing predictions.

### Stakeholders
- **Primary Stakeholders**:
  - **Car Dealerships**: Need accurate pricing tools for evaluating the worth of cars in their inventory.
  - **Used-Car Marketplaces**: Require automated systems to offer fair pricing for both buyers and sellers.
  - **Financial Institutions and Insurance Companies**: Organizations that provide car loans or insurance policies and require accurate car valuations for underwriting and risk assessment.
- **Secondary Stakeholders**:
  - **Car Buyers and Sellers**: Benefit from transparent and competitive pricing.
  - **Automotive Analysts**: Interested in understanding pricing trends and factors that influence car value.

---

## 2. Data Understanding

### Data Overview
We aim to build this System by utilizing a dataset that comprises of car data from various regions and cities in India like Ahmedabad, Bangalore, Chennai, Gurgaon, Hyderabad, Jaipur, Kolkata, Mumbai, and Pune.

### Sources and Collection
The dataset used for this car valuation system project was sourced from Cardekho(http://Cardekho.com), a leading automotive website that provides detailed information on car listings, specifications, pricing, and more.
Web scraping was done in observance with the site's terms of service, and the data was structured into a CSV file for easy access and manipulation.

### Data Description
The dataset includes the following features:

- `Brand`: The manufacturer or brand of the vehicle (e.g., Toyota, Ford).
- `Make_Year`: The year the vehicle was manufactured.
- `Fuel`: The type of fuel the vehicle uses (e.g., Petrol, Diesel, Electric).
- `KMs_Driven`: The total kilometers driven by the vehicle.
- `Engine_Displacement`: The engine capacity measured in liters or cubic centimeters (cc).
- `No_Of_Owner`: The number of previous owners the vehicle has had.
- `Transmission`: Type of transmission (e.g., Manual, Automatic).
- `Mileage`: The distance the vehicle can travel per unit of fuel (usually measured in km/l).
- `Max_Power`: The maximum power output of the engine (measured in horsepower or kilowatts).
- `Torque`: The twisting force produced by the engine (measured in Nm).
- `Seats`: The number of seats in the vehicle.
- `Color`: The color of the vehicle.
- `Gear_Box`: The type of gearbox (could be automatic or manual).
- `Drive_Type`: The drivetrain configuration (e.g., Front-Wheel Drive, Rear-Wheel Drive, All-Wheel Drive).
- `Steering_Type`: The type of steering system (e.g., Power Steering, Manual Steering).
- `Front_Brake_Type`: The type of brakes used on the front wheels (e.g., Disc, Drum).
- `Rear_Brake_Type`: The type of brakes used on the rear wheels (e.g., Disc, Drum).
- `Acceleration`: The time taken to accelerate from 0 to 100 km/h (measured in seconds).
- `Price`: The selling price of the vehicle(The Target Variable).
### Data Exploration
During the exploration phase, the following key patterns and observations were made:
- Car age, mileage, and condition are highly correlated with the price.
- Certain brands and models tend to have higher market values.
- There are some missing values in features like `engine_size` and `mileage`, which need to be addressed.

---

## 3. Data Preprocessing

### Data Cleaning
The dataset was cleaned to ensure that it was ready for modeling. This included:
- **Handling Missing Values**: Columns with missing values, such as `Acceleration`,`Rear_Brake_Type`,`Front_Brake_Type`, `Steering_Type`, `Drive_Type` and `No_Of_Owners`, were either imputed with the mean/median or mode 
- **Outlier Detection**: Extreme outliers in `Gear_Box`, `No_Of_Owner`, `Engine_Displacement`,`Max_Power`, `Seats`, `Price`, `Mileage`, `KMS_Driven` and a few in `Make_Year` and `Acceleration` and  were identified and handled. We did not handle `Price` since outliers might indicate high luxury cars.

### Exploratory Data Analysis (EDA)
Exploratory Data Analysis was performed to identify trends, correlations, and patterns within the data:
- **Univariate Analysis**: Distribution of individual features (e.g., price, mileage, and age) was examined to understand their impact.
- **Bivariate Analysis**: Relationships between the target variable (`price`) and other features were explored. Correlations between car attributes (e.g., age and mileage) and price were analyzed.

### Feature Engineering
New features were created to better capture the relationship between car attributes and the target variable:

### Correlation Analysis
Correlation analysis was performed to identify multicollinearity and the most important features that influence price:
- Strong positive correlation was found between `mileage` and `price`.
- `Condition` was another significant categorical feature that influences price, especially for cars in good or excellent condition.

### Feature Scaling
To ensure all features are on the same scale, numerical features  were standardized using `StandardScaler` from scikit-learn.

### Feature Selection
Feature selection was carried out to retain only the most relevant features:
- **SelectKBest**: Statistical tests were applied to select the most influential features for the model. This ensured that the model was not overfitted by irrelevant features.
  
---

## 4. Modeling

### Regression and Ensemble Techniques

Different types of models were implemented to predict the car prices:

- **Linear Regression**: 
  - The linear regression model was implemented as a baseline to understand the linear relationships between features and car prices. 
  - Linear Regression Evaluation Results:
    Mean Squared Error (MSE): 249462455102.7223
    Root Mean Squared Error (RMSE): 499462.1658371356
    R-squared: 0.6407968427069457 explaining 64.1% variability in car prices by the predictors. This is a decent result but shows room for improvement.
    Mean Absolute Error (MAE): 262972.3722601558
- **Decision Trees**:
  - Decision Tree Regressor Evaluation Results:
    Mean Squared Error (MSE): 174933708732.1922
    Root Mean Squared Error (RMSE): 418250.7725422539
    R-squared: 0.7481114323688011, explaining 74.8% variability in car prices by the predictors
    Mean Absolute Error (MAE): 160572.32644790708

- **Random Forest Regressor**:
  - An ensemble learning model was used to improve predictions. The Random Forest model performed better than linear regression by capturing non-linear patterns and interactions between multiple features.
  - Hyperparameter tuning was conducted to optimize the model’s performance.
  - Random Forest Regressor Evaluation Results:
    Mean Squared Error (MSE): 128568690257.09554
    Root Mean Squared Error (RMSE): 358564.76438308257
    R-squared: 0.8148728254503678, explaining 81.4% variability in car prices by the predictors
    Mean Absolute Error (MAE): 137983.14488881442

- **Gradient Boosting Regressor**:
  - Gradient Boosting Regressor Evaluation Results
    Mean Squared Error (MSE): 128268327432.82712
    Root Mean Squared Error (RMSE): 358145.6790648564
    R-squared: 0.8153053204916205, xplaining 81.5% variability in car prices by the predictors
    Mean Absolute Error (MAE): 140197.4860353186


---

## 5. Evaluation and Recommendations

### Evaluation Metrics
To assess the performance of the models, the following metrics were used:
- **Mean Absolute Error (MAE)**: Measures the average magnitude of errors in the predictions.
- **Mean Squared Error (MSE)**: Penalizes larger errors and provides a sense of model performance.
- **R-squared**: Indicates how well the model fits the data.

The **Gradient Boosting Regressor** and **Random Forest Regressor** outperformed **Decision Trees** but **Linear Regression** was the weakest model with a lower MAE, MSE, and R-squared value.

### Recommendations
Based on the findings from the model evaluation:
- **Dynamic Pricing Model**: Businesses can use the Gradient Boosting model to set real-time dynamic prices, adjusting for features like mileage, age, and condition.
- **Price Optimization**: The model can be used to recommend price adjustments, ensuring that cars are priced competitively in the market while maximizing profits.
- **Market Insights**: The model can help identify which car features (e.g., brand, engine size, condition) most influence pricing, allowing businesses to better understand market demand.

---

## 6. Model Deployment

### Deployment Strategy
The trained Random Forest model can be deployed as a web application using Streamlit which provides a user-friendly interface where users can input car details (such as make, model, mileage, etc.) and get an estimated price in real-time. Streamlit is ideal for deploying machine learning models for quick prototypes and demonstrations without the need to build an extensive web framework.

### Model Deployment Steps
1. **Convert the model into a serialized format and save it**:('gb_model.joblib').
2. **Install Streamlit**:Install Streamlit and other dependencies like joblib.
3. **Build the Streamlit App**: Create a streamlit_app.py file. This file will contain the code to load the Gradient Boosting model and create a user interface for input.
4. **Run the Streamlit App Locally**: After you’ve written the app, you can run it locally by executing the following command in your terminal: (streamlit run app.py)
5. **Deploy the Streamlit Application**: After you've tested the app locally and are happy with it, you can deploy it using Streamlit Sharing, Heroku, or AWS.
---

## Installation and Usage

### Clone the Repository

```bash
git clone <https://github.com/FaithMUTIS/Group-2-phase-5-project>
