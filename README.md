# CAR VALUATION SYSTEM
![alt text](download.jpg)

PROJECT OVERVIEW

The Car Valuation System aims to modernize vehicle pricing for insurance companies and
auto resellers by employing a machine learning-based solution for accurate, objective, and
data-driven market appraisals. Traditional valuation methods are labor-intensive,
subjective, and inconsistent, leading to inefficiencies and dissatisfaction among
stakeholders. This project seeks to streamline the process through technology, improving
precision and operational efficiency

AIM OF THE PROJECT

To develop a machine-learning-powered system that predicts a car’s market value based on
its attributes, enhancing pricing accuracy and operational efficiency.

Data Understanding

We have sourced historical car sales data, including:

Car Details: make, model, year, fuel type, engine size, transmission, body type
Condition Indicators: mileage, service history, accident history, condition ratings
Market Information: location, seasonal factors, regional pricing trends
Pricing: original sale price, resale values

BUSINESS UNDERSTANDING

Accurate car valuation is critical for insurance companies and car resellers. Insurance firms
require precise appraisals to set premiums and calculate claim settlements, while resellers
rely on competitive pricing for profitability. Current methods often lack reliability and
consistency. The proposed system leverages historical car data, including attributes like
make, model, mileage, and condition, to train machine learning models such as linear
regression, decision trees, and gradient boosting. The solution offers real-time,
user-friendly appraisals, improving decision-making, operational efficiency, and
stakeholder trust.

TOOLS AND TECHNOLOGIES

The tools, libraries and frameworks used include:

Python
Pandas, NumPy, Scikit-learn, XGBoost
Matplotlib, Seaborn (for visualization)
Jupyter Notebook/Google Colab

APPROACH

We used the following steps;

Data Preprocessing: Cleaning and encoding data, handling missing values.
Exploratory Data Analysis (EDA): Key insights, trends, and correlations.
Feature Engineering: Feature selection, scaling, etc.
Model Development: Algorithms tested and chosen were Lasso, Ridge, Decision Tree Regressor, KNeighbors Regressor, Random Forest Regressor and Gradient Boosting Regressor.
Evaluation: Metrics used, such as RMSE, MAE, or R².

RESULTS

Linear Regression
Cross Validation Scores:

At cross fold 2: 31.75%

At cross fold 3: 22.17%

At cross fold 4: 33.19%

At cross fold 5: 32.37%

At cross fold 6: 35.37%

At cross fold 7: 38.98%

At cross fold 8: 31.73%

At cross fold 9: 36.10%

Test Accuracy: 61.55%

Errors:

Mean Absolute Error: 255,396.15

Mean Squared Error: 226,024,833,248.27

Root Mean Square Error: 475,420.69

Lasso Regression
R2 Score: 61.55%

Cross Validation Score: 38.98%

Errors:

Mean Absolute Error: 255,395.27

Mean Squared Error: 226,024,642,723.29

Root Mean Square Error: 475,420.49

Ridge Regression
R2 Score: 61.55%

Cross Validation Score: 39.00%

Errors:

Mean Absolute Error: 255,351.13

Mean Squared Error: 226,011,758,603.91

Root Mean Square Error: 475,406.94

Decision Tree Regressor
R2 Score: 61.25%

Cross Validation Score: 52.51%

Errors:

Mean Absolute Error: 169,328.45

Mean Squared Error: 227,773,198,341.73

Root Mean Square Error: 477,255.90

KNeighbors Regressor
R2 Score: 62.89%

Cross Validation Score: 59.11%

Errors:

Mean Absolute Error: 208,719.79

Mean Squared Error: 218,155,178,740.23

Root Mean Square Error: 467,070.85

RandomForest Regressor
R2 Score: 84.49%

Cross Validation Score: 75.31%

Errors:

Mean Absolute Error: 119,682.14

Mean Squared Error: 91,158,903,129.48

Root Mean Square Error: 301,925.33

GradientBoosting Regressor
R2 Score: 84.49%

Cross Validation Score: 73.64%

Errors:

Mean Absolute Error: 119,682.14

Mean Squared Error: 91,158,903,129.48

Root Mean Square Error: 301,925.33

Conclusion
From the results, it is evident that the RandomForest Regressor and GradientBoosting Regressor models outperform the other models in terms of R2 score and cross-validation score. Both models achieved an R2 score of approximately 84.49% and cross-validation scores of 75.31% and 73.64%, respectively. However, the errors, particularly the Mean Absolute Error and Root Mean Square Error, are still relatively high, indicating that there is room for improvement in the model's accuracy.

The KNeighbors Regressor also showed a decent performance with an R2 score of 62.89% and a cross-validation score of 59.11%. The Decision Tree Regressor had a lower R2 score of 61.25% but a higher cross-validation score of 52.51% compared to the linear models.

The linear models, including Linear Regression, Lasso Regression, and Ridge Regression, had similar R2 scores around 61.55% but lower cross-validation scores, indicating that they may not generalize well to unseen data.

Overall, ensemble techniques like RandomForest and GradientBoosting Regressors provide better performance and should be considered for further tuning and optimization to improve model accuracy.
