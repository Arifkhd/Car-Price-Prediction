# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:21:18 2024

@author: Dell
"""
import streamlit as st
import joblib
import pandas as pd
from sklearn.ensemble import AdaBoostRegressor
model = joblib.load('car.pkl')

st.title('Car Price Prediction')

def predict(Name,Year,Km_Driven,Fuel_Type,Seller_Type,Transmission,Owner_Type):
    prediction = model.predict([[Name,Year,Km_Driven,Fuel_Type,Seller_Type,Transmission,Owner_Type]])
    return prediction[0]
    
    
def main():
    st.markdown('Car Price Prediction :chart:')  
    Name = st.selectbox('Name of the car and model name',('None','Honda Jazz 1.5 E i DTEC', 'Honda City i-VTEC VX', 'Honda Amaze 1.5 E i-DTEC',
    'Honda WR-V i-VTEC S', 'Honda Civic ZX CVT Petrol', 'Honda BR-V S i-VTEC',
    'Honda Accord Hybrid', 'Honda CR-V 2.0L 2WD', 'Honda Mobilio V i-DTEC',
    'Honda City ZX Diesel', 'Honda Civic i-DTEC VX', 'Honda Brio VX AT',
    'Honda Amaze VX CVT Petrol', 'Honda WR-V VX Diesel', 'Honda Jazz ZX CVT',

    # Toyota
    'Toyota Innova 2.5 VX 7 STR', 'Toyota Fortuner 2.8 Sigma 4', 'Toyota Camry Hybrid',
    'Toyota Corolla Altis 1.8 G', 'Toyota Etios Liva VXD', 'Toyota Yaris VX CVT',
    'Toyota Urban Cruiser Premium', 'Toyota Glanza V', 'Toyota Hilux STD MT',
    'Toyota Qualis GS Diesel', 'Toyota Prius Z5 Hybrid', 'Toyota C-HR Dynamic',
    'Toyota RAV4 Adventure AWD', 'Toyota Hiace Commuter Bus', 'Toyota Land Cruiser Prado VX',
    'Toyota Innova 2.5 E 8 STR',

    # Hyundai
    'Hyundai Creta SX 1.4 CRDi', 'Hyundai i20 Asta 1.2', 'Hyundai Verna SX 1.6 VTVT',
    'Hyundai Elantra SX MT', 'Hyundai Venue SX (O) 1.0 Turbo', 'Hyundai Santro Xing GLS LPG',
    'Hyundai Tucson GLS 2WD', 'Hyundai Kona Electric Premium', 'Hyundai Grand i10 Sportz AT',
    'Hyundai Getz Prime GLE', 'Hyundai Accent Viva Diesel', 'Hyundai Aura SX Petrol',
    'Hyundai Alcazar Signature Diesel AT', 'Hyundai Sonata Gold AT', 'Hyundai i10 Era 1.1',

    # Maruti Suzuki
    'Maruti Swift ZXi Plus', 'Maruti Alto 800 LXI CNG', 'Maruti Baleno Alpha CVT',
    'Maruti Ertiga ZDi Plus', 'Maruti Ciaz Delta Diesel SHVS', 'Maruti Vitara Brezza VDi',
    'Maruti WagonR VXI AMT', 'Maruti Ignis Zeta Petrol', 'Maruti S-Cross Zeta 1.6',
    'Maruti XL6 Alpha Petrol', 'Maruti Omni 5-Seater E MPI', 'Maruti Dzire Tour S Diesel',
    'Maruti Ritz VDi ABS', 'Maruti Eeco 7 Seater STD', 'Maruti Kizashi CVT',

    # Ford
    'Ford Ecosport Titanium Diesel', 'Ford Endeavour Titanium 4X4 AT', 'Ford Aspire Trend Petrol',
    'Ford Fiesta Classic 1.4 Duratorq', 'Ford Figo Titanium Blu 1.5', 'Ford Freestyle Titanium Plus',
    'Ford Mustang GT Fastback 5.0L', 'Ford Mondeo 2.0 Ghia', 'Ford Focus Titanium TDCi',
    'Ford Ranger Wildtrak 4X4', 'Ford Explorer ST-Line', 'Ford Expedition Limited MAX',
    'Ford Galaxy Zetec Diesel', 'Ford C-MAX Hybrid SE', 'Ford Puma Titanium',

    # Mahindra
    'Mahindra Scorpio S11 4WD', 'Mahindra Thar LX 4-Str Hard Top Diesel', 'Mahindra Bolero ZLX',
    'Mahindra XUV700 AX7 Diesel AT', 'Mahindra Marazzo M6 Plus', 'Mahindra KUV100 NXT G80 K8',
    'Mahindra TUV300 T10 AMT Dual Tone', 'Mahindra Xylo H8 ABS Airbag BSIV',
    'Mahindra Verito Vibe CS 1.5 D6', 'Mahindra Alturas G4 4WD AT', 'Mahindra Quanto C6 Diesel',
    'Mahindra E2O Plus P8', 'Mahindra Supro LX 8 Seater', 'Mahindra Jeeto S6-11 BS6',
    'Mahindra Armada Grand Diesel',

    # Tata
    'Tata Tiago XZ Petrol', 'Tata Nexon EV Prime XZ+', 'Tata Harrier XT Plus',
    'Tata Safari Adventure Persona', 'Tata Tigor JTP', 'Tata Indica V2 eV2 LS',
    'Tata Zest XT Petrol', 'Tata Hexa XM Diesel', 'Tata Bolt XMS Petrol',
    'Tata Sumo Gold CX', 'Tata Aria Pride 4X4', 'Tata Nano GenX XTA',
    'Tata Altroz XZ Option', 'Tata Indigo CS LX Diesel', 'Tata Manza Aqua Quadrajet',

    # Volkswagen
    'Volkswagen Polo GT TSI', 'Volkswagen Vento Highline Plus Diesel AT',
    'Volkswagen Passat 2.0 TDI Comfortline', 'Volkswagen Tiguan Allspace TSI',
    'Volkswagen Jetta 1.4 TSI Comfortline', 'Volkswagen T-Roc Style',
    'Volkswagen Ameo Highline Plus Diesel', 'Volkswagen Golf GTI',
    'Volkswagen Touareg V6 Diesel', 'Volkswagen ID.4 Pure Performance',
    'Volkswagen Cross Polo 1.2 MPI', 'Volkswagen Up! Move TSI', 'Volkswagen Arteon Elegance',
    'Volkswagen Taigun GT Plus', 'Volkswagen Phaeton 3.6 FSI',

    # Miscellaneous
    'Chevrolet Cruze LTZ Diesel', 'Fiat Punto Evo Emotion', 'Nissan Micra Active XL',
    'Jeep Grand Cherokee Summit', 'Skoda Superb L&K Diesel AT', 'MG Hector Sharp Diesel',
    'Renault Kwid RXT 1.0', 'Kia Seltos HTX Plus Diesel AT', 'Datsun GO T Optional',
    'Mitsubishi Pajero Sport Dual Tone', 'Isuzu D-Max V-Cross Z Prestige', 'Audi Q3 35 TDI Premium',
    'BMW X1 sDrive20i xLine', 'Mercedes-Benz C-Class C200 Progressive', 'Jaguar XF 2.0 Prestige'))
    if Name == 'None':
        st.warning("Please select a valid car model.")
    else:
        st.success(f"You selected: {Name}")
    
    # Year validation
    Year = st.selectbox('Select Year', list(range(1980, 2025)))
    if Year < 1980 or Year > 2025:
        st.warning("Please select a valid manufacturing year.")
    else:
        st.success(f"Manufacturing Year: {Year}")
    
    # Kilometers Driven validation
    Km_Driven = st.number_input("Enter Kilometers Driven:", min_value=0, max_value=500000, step=100, value=0)
    if Km_Driven <= 0:
        st.warning("Kilometers Driven must be greater than 0.")
    
    # Fuel type validation
    Fuel_Type = st.selectbox('Fuel Type', ('None', 'Petrol', 'Diesel', 'Electric', 'CNG', 'LPG'))
    if Fuel_Type == 'None':
        st.warning("Please select a valid fuel type.")
    else:
        st.success(f"You selected: {Fuel_Type}")

    # Seller type validation
    Seller_Type = st.selectbox('Seller Type', ('None', 'Individual', 'Dealer','Trustmark Dealer'))
    if Seller_Type == 'None':
        st.warning('Please select a valid seller type.')
    else:
        st.success(f"You selected: {Seller_Type}")
        
    # Transmission validation
    Transmission = st.selectbox('Transmission', ('None', 'Manual', 'Automatic'))
    if Transmission == 'None':
        st.warning('Please select a valid transmission type.')
    else:
        st.success(f'You selected: {Transmission}')
        
    # Owner type validation
    Owner_Type = st.selectbox('Owner Type', ('None', 'First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above','Test Drive Car'))
    if Owner_Type == "None":
        st.warning("Please select a valid owner type.")
    else:
        st.success(f"You selected: {Owner_Type}")
        
    # Prediction button and result
    if st.button('Predict'):
        # Ensure all validations are met
        if Name == 'None' or Fuel_Type == 'None' or Seller_Type == 'None' or Transmission == 'None' or Owner_Type == 'None' or Km_Driven <= 0:
            st.error("Please fill in all the required fields correctly before predicting.")
        else:
            result = predict(Name, Year, Km_Driven, Fuel_Type, Seller_Type, Transmission, Owner_Type)
            st.success(f'Predicted Car Price: ₹{result:,.0f}')

if __name__ == '__main__':
    main()
