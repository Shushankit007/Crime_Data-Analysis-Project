# Laptop Price Prediction Project
This repository's bramch contains files related to a machine learning project focused on predicting laptop prices. The project is divided into two main parts, each contained in a separate Jupyter Notebook.

# **Project Title: Laptop Price Prediction for SmartTech Co.**

## Project Overview:
SmartTech Co. has partnered with our data science team to develop a robust machine learning model that predicts laptop prices accurately. As the market for laptops continues to expand with a myriad of brands and specifications, having a precise pricing model becomes crucial for both consumers and manufacturers.

## Objectives:
* Accurate Pricing: Develop a model that can accurately predict laptop prices based on various features, helping our clients stay competitive in the market.
* Market Positioning: Understand how different features contribute to pricing, enabling SmartTech Co. to strategically position its laptops in the market.
* Brand Influence: Assess the impact of brand reputation on pricing, providing insights into brand perception and market demand.

## **Project Phases:**
### Data Exploration and Understanding:
* Dive into the dataset to understand the landscape of laptop specifications.
* Visualize trends in laptop prices and identify potential influential features.
### Data Preprocessing:
* Handle missing values, outliers, and encode categorical variables.
* Ensure the dataset is ready for model training.
### Feature Engineering:
* Extract meaningful features to enhance model performance.
* Consider creating new features that capture the essence of laptop pricing.
### Model Development:
* Employ machine learning algorithms such as Linear Regression, Random Forest, and Gradient Boosting to predict laptop prices.
* Evaluate and choose the model that aligns best with the project's objectives.
### Hyperparameter Tuning:
* Fine-tune the selected model to achieve optimal performance.
### Real-time Predictions:
* Implement a mechanism for the model to make predictions for new laptops entering the market.
### Interpretability and Insights:
* Uncover insights into which features play a pivotal role in pricing decisions.
* Ensure that SmartTech Co. can interpret and trust the model's predictions.


## Project File :
- `ML_Project_(Part_1).ipynb`: This notebook covers the initial stages of the project, including data exploration, data cleaning, and preprocessing. The original dataset `laptop.csv` is used for this purpose. After preprocessing, the cleaned dataset is saved as `new_laptop.xlsx`.

- `ML_Project(Part_2).ipynb`: In this notebook, feature selection and encoding techniques are applied to the preprocessed dataset (`new_laptop.xlsx`). The encoded data is saved as `encoded_laptop.xlsx`. Additionally, machine learning models are developed, trained, and evaluated. The best-performing model, XGBoost, is selected and saved as `best_xgb_model.pkl`.

## Files and Descriptions
- `laptop.csv`: Original dataset containing information about laptops.
- `new_laptop.xlsx`: Preprocessed dataset obtained after data cleaning and preprocessing.
- `encoded_laptop.xlsx`: Dataset with encoded features generated from `new_laptop.xlsx`.
- `best_xgb_model.pkl`: Trained XGBoost model, selected as the best-performing model for laptop price prediction.
- `feature_df_laptop.xlsx`: Dataset used for the Streamlit UI. It contains simplified features without the target variable (price) and some complex or unnecessary features to facilitate a streamlined user interface.
- `LaptopPricePrediction.py`: Python file containing the Streamlit application for the laptop price prediction model. It provides a user-friendly interface for predicting laptop prices based on the trained model. Users can run the application locally by executing the provided command in their command prompt.
- `README.md`: This file, providing an overview of the project and descriptions of the files present in the repository.

### Running the Streamlit Application 
To run the Streamlit application for laptop price prediction, execute the following command in the terminal:
```bash
streamlit run LaptopPricePrediction.py
```
## **Dependencies:**
1. Pandas
2. NumPy
3. Matplotlib
4. Seaborn
5. Scikit-learn
6. Joblib
7. Streamlit
8. XGBoost
9. os
10. re
11. openxyl

## Expected Outcomes:
* A reliable machine learning model capable of predicting laptop prices with high accuracy.
* Insights into the factors influencing laptop prices, empowering SmartTech Co. in market positioning and strategy.











