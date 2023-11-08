import streamlit as st
import pandas as pd
import pickle
import joblib

#with open('project_model.pkl', 'rb') as model_file:
    #model = pickle.load(model_file)

model= joblib.load('./AML_model.pkl')

def predict_price(make, year, mileage, car_type, transmission, cc):
    input_data = pd.DataFrame([[make, year, mileage, car_type, transmission, cc]],
                               columns=['Make', 'Year', 'Mileage', 'Type', 'Transmission', 'CC'])
    predicted_price = model.predict(input_data)
    return predicted_price[0]

# Streamlit app
st.title('Car Price Prediction App')

# User input
make = st.selectbox('Make:',['Honda', 'Suzuki', 'Toyota', 'Changan', 'KIA', 'Mitsubishi',
       'Nissan', 'Daihatsu', 'Hyundai'])
year = st.selectbox('Year:', list(range(1990, 2023)))
mileage = st.number_input('Mileage:')
car_type = st.selectbox('Type:', ['Petrol', 'Diesel', 'Hybrid'])
transmission = st.selectbox('Transmission:', ['Automatic', 'Manual'])
cc = st.number_input('CC:')


if st.button('Predict Price'):
    result = predict_price(make, year, mileage, car_type, transmission, cc)
    st.success(f'Predicted Price: ${result:.2f}')