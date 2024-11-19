import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('gb_model.joblib')

# Define the input fields for the model features
st.title("Car Valuation Prediction App")
st.write("Enter the car details to predict the car's valuation.")

# Collect inputs for each feature used in the model
make_year = st.number_input('Make Year', min_value=1995, max_value=2024, step=1)
mileage = st.number_input('Kilometers Driven', min_value=0, max_value=3000000, step=1000)
engine_displacement = st.number_input('Engine Displacement (cc)', min_value=500, max_value=5000, step=10)
max_power = st.number_input('Max Power (bhp)', min_value=30, max_value=500, step=1)
torque = st.number_input('Torque (Nm)', min_value=50, max_value=1000, step=10)
gear_box = st.number_input('Gear Box', min_value=4, max_value=8, step=1)
acceleration = st.number_input('Acceleration (0-100 km/h in seconds)', min_value=1.0, max_value=20.0, step=0.1)

# Dropdown or radio button for categorical fields
brand = st.selectbox('Car Brand', ['BMW 3 Series 320d', 'BMW 6 Series GT', 'Land Rover Range Rover', 
                                   'Mercedes-Benz E-Class Exclusive E', 'Volvo XC 90 Excellence'])
fuel_type = st.selectbox('Fuel Type', ['Diesel', 'Petrol'])
transmission = st.selectbox('Transmission Type', ['Manual', 'Automatic'])
drive_type = st.selectbox('Drive Type', ['AWD', 'FWD', 'RWD'])

# Convert inputs to a format the model can process (like encoding categorical values)
brand_features = {
    'BMW 3 Series 320d': [1, 0, 0, 0, 0],
    'BMW 6 Series GT': [0, 1, 0, 0, 0],
    'Land Rover Range Rover': [0, 0, 1, 0, 0],
    'Mercedes-Benz E-Class Exclusive E': [0, 0, 0, 1, 0],
    'Volvo XC 90 Excellence': [0, 0, 0, 0, 1]
}

fuel_type_value = 1 if fuel_type == 'Diesel' else 0
transmission_value = 1 if transmission == 'Manual' else 0
drive_type_values = {'AWD': [1, 0, 0], 'FWD': [0, 1, 0], 'RWD': [0, 0, 1]}

# Prepare the input data for prediction
input_data = [
    make_year, mileage, engine_displacement, max_power, torque, gear_box, acceleration,
    *brand_features[brand], fuel_type_value, transmission_value, *drive_type_values[drive_type]
]
input_array = np.array(input_data).reshape(1, -1)

# Check the input data shape (length should be 18)
st.write(f"Input data shape: {input_array.shape}")

# Make a prediction when the user clicks "Predict"
if st.button("Predict"):
    prediction = model.predict(input_array)
    st.write(f"Estimated Car Valuation: ${prediction[0]:,.2f}")
