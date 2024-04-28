import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import xgboost
import numpy as np
import os

model_path = "C:/Users/ASUS/OneDrive/Desktop/Capstone_Project_DS/ML - Capstone Project/best_xgb_model.pkl"
feature_data_path = "C:/Users/ASUS/OneDrive/Desktop/Capstone_Project_DS/ML - Capstone Project/feature_df_laptop.xlsx"
# Load the trained model
model = joblib.load(model_path)
# loading the dataset
feature_data = pd.read_excel(feature_data_path)

# Function to preprocess input features
def preprocess_input(features, label_encoders):
    # Label encoding for categorical features
    for column, encoder in label_encoders.items():
        if column in ['IPS_Panel', 'Touchscreen']:
            # Convert 'Yes'/'No' to 1/0
            features[column] = 1 if features[column] == 'Yes' else 0
        else:
            features[column] = encoder.transform([features[column]])[0]
    return features

# Define label encoders for categorical features
label_encode_columns = ['Company', 'TypeName', 'IPS_Panel', 'Touchscreen', 'Memory_1_Type', 'Memory_2_Type', 'OS_Brand', 'OS_Version', 'Processor', 'Graphic_Card', 'GPU_Model_series', 'Display_Type']
label_encoders = {}
for column in label_encode_columns:
    label_encoders[column] = LabelEncoder()
    label_encoders[column].fit(feature_data[column])

# Create the Streamlit app
def main():
    st.title('Laptop Price Predictor')

    # Define input fields
    Company = st.selectbox('Company', feature_data['Company'].unique())
    TypeName = st.selectbox('Type Name', feature_data['TypeName'].unique())
    Inches = st.slider('Inches', min_value=int(feature_data['Inches'].min()), max_value=int(feature_data['Inches'].max()), value=int(feature_data['Inches'].mean()))
    Weight_kg = st.slider('Weight (kg)', min_value=float(feature_data['Weight_kg'].min()), max_value=float(feature_data['Weight_kg'].max()), value=float(feature_data['Weight_kg'].mean()))
    IPS_Panel = st.radio('IPS Panel', ['Yes', 'No'])
    Touchscreen = st.radio('Touchscreen', ['Yes', 'No'])
    PPI = st.slider('PPI', min_value=int(feature_data['PPI'].min()), max_value=int(feature_data['PPI'].max()), value=int(feature_data['PPI'].mean()))
    Display_Type = st.selectbox('Display Type', feature_data['Display_Type'].unique())
    CPU_Speed_GHz = st.slider('CPU Speed (GHz)', min_value=float(feature_data['CPU_Speed_GHz'].min()), max_value=float(feature_data['CPU_Speed_GHz'].max()), value=float(feature_data['CPU_Speed_GHz'].mean()))
    RAM_GB = st.slider('RAM (GB)', min_value=int(feature_data['RAM_GB'].min()), max_value=int(feature_data['RAM_GB'].max()), value=int(feature_data['RAM_GB'].mean()))
    Memory_1_Size_GB = st.slider('Memory 1 Size (GB)', min_value=int(feature_data['Memory_1_Size_GB'].min()), max_value=int(feature_data['Memory_1_Size_GB'].max()), value=int(feature_data['Memory_1_Size_GB'].mean()))
    Memory_1_Type = st.selectbox('Memory 1 Type', feature_data['Memory_1_Type'].unique())
    Memory_2_Size_GB = st.slider('Memory 2 Size (GB)', min_value=int(feature_data['Memory_2_Size_GB'].min()), max_value=int(feature_data['Memory_2_Size_GB'].max()), value=int(feature_data['Memory_2_Size_GB'].mean()))
    Memory_2_Type = st.selectbox('Memory 2 Type', feature_data['Memory_2_Type'].unique())
    OS_Brand = st.selectbox('OS Brand', feature_data['OS_Brand'].unique())
    OS_Version = st.selectbox('OS Version', feature_data['OS_Version'].unique())
    Processor = st.selectbox('Processor', feature_data['Processor'].unique())
    Graphic_Card = st.selectbox('Graphic Card', feature_data['Graphic_Card'].unique())
    GPU_Model_series = st.selectbox("Graphic card's  Series", feature_data['GPU_Model_series'].unique())

    # Prepare input features as a dictionary
    input_features = {
        'Company': Company,
        'TypeName': TypeName,
        'Inches': Inches,
        'Weight_kg': Weight_kg,
        'IPS_Panel': IPS_Panel,
        'Touchscreen': Touchscreen,
        'PPI': PPI,
        'Display_Type': Display_Type,
        'CPU_Speed_GHz': CPU_Speed_GHz,
        'RAM_GB': RAM_GB,
        'Memory_1_Size_GB': Memory_1_Size_GB,
        'Memory_1_Type': Memory_1_Type,
        'Memory_2_Size_GB': Memory_2_Size_GB,
        'Memory_2_Type': Memory_2_Type,
        'OS_Brand': OS_Brand,
        'OS_Version': OS_Version,
        'Processor': Processor,
        'Graphic_Card': Graphic_Card,
        'GPU_Model_series' : GPU_Model_series
    }

    # Preprocess input features
    input_features = preprocess_input(input_features, label_encoders)

    # Convert input_features to a numpy array
    input_features = np.array(list(input_features.values()))

    # Make predictions
    prediction = model.predict(input_features.reshape(1, -1))

    # Display prediction to user in a larger, bold font
    st.write(f"<h1 style='font-size: 50px;'>Predicted Laptop Price: INR {prediction[0]}</h1>", unsafe_allow_html=True)


if __name__ == '__main__':
    main()


# to run this script iin browser from cmd
# streamlit run C:\Users\ASUS\PycharmProjects\Py_capstoneProject\LaptopPricePrediction.py [ARGUMENTS]


# dependecies : openxyl, streramlit, os -- to luanch our steamlit app
# other : pandas, sklearn, xgboost, numpy and straamlit for creating application