# Electric Motor Temperature Analysis


## Project Overview

This project involves the analysis of a dataset using Python's pandas, numpy, matplotlib, seaborn, and scikit-learn libraries. The primary goal is to perform exploratory data analysis (EDA) on the provided dataset, preprocess the data, and train a linear regression model for predictive analysis.

## Steps Performed

### Data Loading and Preprocessing
- Load the dataset 'measures_v2.csv' using pandas.
- Drop the 'profile_id' column from the dataset.
- Split the data into features (X) and target variable (y).
- Standardize the features using scikit-learn's StandardScaler.
- Standardize the target variable.

### Univariate Analysis
- Generate histograms for each feature and the target variable.
- Generate box plots for each feature and the target variable.

### Multivariate Analysis
- Create a pair plot for a subset of the dataset.

### Correlation Heatmap
- Calculate the correlation matrix of features and the target variable.
- Generate a correlation heatmap using seaborn.

### Model Training and Evaluation
- Split the standardized data into training and testing sets.
- Initialize a LinearRegression model.
- Train the model on the training data.
- Print the R^2 score of the model on the test data.
- Serialize and save the trained model as 'linear_regression_model.pkl'.

## Interpretation

- ![Distribution Plot](res/displot.png)
  The distribution plot shows that most of the columns present a normal distribution; specifically, the column we are trying to predict is a normal distribution.

- ![Box Plot](res/boxplot.png)
  The box plot shows that there aren't many outliers in our data.

- ![Pair Plot](res/pairplot.png)
  The pair plot reveals strong correlations between certain features. While considering feature selection, note that some features exhibit significant interdependence.

- ![Correlation Heatmap](res/heatmap.png)
  The heatmap visually confirms the correlations observed in the pair plot. Strong positive and negative correlations are highlighted, further emphasizing the need for careful feature consideration.

## Dataset
You can find the dataset [here](https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature).

## Author
Zakaria Akerdad




