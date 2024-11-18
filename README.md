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

Mean Squared error (MSE):  249,462,455,102.72
Root Mean Squared Error (RSME): 499,462.17
R-Squared (R2): 0.641
Mean Absolute error (MAE): 262,972.37
Analysis:  R-Squared is 0.641, which suggests the model explains about 64.1% of the variability in car prices is explained by the predictors. This is a decent result but shows room for improvement. The MSE and RSME are quite large, indicating that the models predictios have a significant deviation from the true values.

DecisionTree Regressor
Mean Squared Error: 174,933,708,732
Root Mean Squared Error 418,250.77
R-Squared: 0.748
Mean Absolute Error: 160,572.33
Analysis:  The R-Squared value of 0.748 indicates that the model explains about 74.8% of the variance in the target variable, which is an improvement over Linear Regression.
The RSME and MSE are still large, but much lower than the linear Regression suggesting better prediction accuracy and smaller errors.
The MAE is much lower than Linear Regression, indicating more accurate predictions on average.

RandomForest Regressor
Mean Squared Error 128,568,690,257
Root Mean Squared Error 358,564.76
R-Squared 0.815
Mean Absolute Error 137,983.14
Analysis:  The R-Squared value of 0.815 shows that the model explains about 81.5% of the variance, which is a significant improvement over both Linear Regression and Decision Trees.
The Random Forest Regressor shows even lower MSE and RSME compared to both Linear Regression and Decision Tree models, suggesting that it has the smallest average prediction error in its predictions.

Conclusion
From the results, it is evident that the RandomForest Regressor and GradientBoosting Regressor models outperform the other models in terms of R2 score and cross-validation score. Both models achieved an R2 score of approximately 84.49% and cross-validation scores of 75.31% and 73.64%, respectively. However, the errors, particularly the Mean Absolute Error and Root Mean Square Error, are still relatively high, indicating that there is room for improvement in the model's accuracy.

The KNeighbors Regressor also showed a decent performance with an R2 score of 62.89% and a cross-validation score of 59.11%. The Decision Tree Regressor had a lower R2 score of 61.25% but a higher cross-validation score of 52.51% compared to the linear models.

The linear models, including Linear Regression, Lasso Regression, and Ridge Regression, had similar R2 scores around 61.55% but lower cross-validation scores, indicating that they may not generalize well to unseen data.

Overall, ensemble techniques like RandomForest and GradientBoosting Regressors provide better performance and should be considered for further tuning and optimization to improve model accuracy.
