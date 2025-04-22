import streamlit as stl
import pandas as pd
import pickle
import numpy as np
import os

# Function to load the model
def load_model():
    try:
        # First try to load from the current directory
        if os.path.exists("random_forest_model.pkl"):
            with open("random_forest_model.pkl", "rb") as f:
                return pickle.load(f)
        # If not found, try to load from the models directory
        elif os.path.exists("models/random_forest_model.pkl"):
            with open("models/random_forest_model.pkl", "rb") as f:
                return pickle.load(f)
        else:
            stl.error("Model file not found. Please ensure random_forest_model.pkl exists in the correct location.")
            return None
    except Exception as e:
        stl.error(f"Error loading model: {str(e)}")
        return None

# Load the model
model = load_model()

# If model loading failed, show error and stop execution
if model is None:
    stl.stop()

#Setup app title and description
stl.title("House Price Prediction Model")
stl.write("Please enter the known details about the house") 

# Create tabs for different feature categories
tab1, tab2, tab3, tab4 = stl.tabs(["Basic Information", "Exterior Features", "Interior Features", "Garage & Additional Features"])

with tab1:
    stl.header("Basic Information")
    lot_area = stl.number_input("Lot Area (sq ft)", min_value=0, value=50000)
    lot_frontage = stl.number_input("Lot Frontage (ft)", min_value=0, value=80)
    year_built = stl.slider("Year Built", min_value=1800, max_value=2025, value=1961)
    year_remod_add = stl.slider("Year Remodeled", min_value=1800, max_value=2025, value=1961)
    overall_qual = stl.slider("Overall Quality", min_value=1, max_value=10, value=5)
    overall_cond = stl.slider("Overall Condition", min_value=1, max_value=10, value=5)
    gr_liv_area = stl.number_input("Above Grade Living Area (sq ft)", min_value=0, value=1710)
    low_qual_fin_sf = stl.number_input("Low Quality Finished Area (sq ft)", min_value=0, value=0)
    street = stl.selectbox("Street Type", ["Pave", "Grvl"])
    utilities = stl.selectbox("Utilities", ["AllPub", "NoSewr", "NoSeWa", "ELO"])
    lot_config = stl.selectbox("Lot Configuration", ["Inside", "Corner", "CulDSac", "FR2", "FR3"])
    condition1 = stl.selectbox("Proximity to Main Road", ["Artery", "Feedr", "Norm", "RRNn", "RRAn", "PosN", "PosA", "RRNe", "RRAe"])
    condition2 = stl.selectbox("Proximity to Secondary Road", ["Artery", "Feedr", "Norm", "RRNn", "RRAn", "PosN", "PosA", "RRNe", "RRAe"])

with tab2:
    stl.header("Exterior Features")
    house_style = stl.selectbox("House Style", ["1Story", "2Story", "1.5Fin", "1.5Unf", "SFoyer", "SLvl", "2.5Unf", "2.5Fin"])
    roof_style = stl.selectbox("Roof Style", ["Gable", "Hip", "Gambrel", "Mansard", "Flat", "Shed"])
    roof_matl = stl.selectbox("Roof Material", ["CompShg", "Tar&Grv", "WdShngl", "WdShake", "Metal", "Membran", "Roll"])
    exterior1st = stl.selectbox("Primary Exterior Material", ["VinylSd", "MetalSd", "Wd Sdng", "HdBoard", "BrkFace", "WdShing", "CemntBd", "Plywood", "AsbShng", "Stucco", "BrkComm", "AsphShn", "Stone", "ImStucc", "CBlock"])
    exterior2nd = stl.selectbox("Secondary Exterior Material", ["VinylSd", "MetalSd", "Wd Sdng", "HdBoard", "BrkFace", "WdShing", "CemntBd", "Plywood", "AsbShng", "Stucco", "BrkComm", "AsphShn", "Stone", "ImStucc", "CBlock"])
    foundation = stl.selectbox("Foundation Type", ["PConc", "CBlock", "BrkTil", "Slab", "Stone", "Wood"])

with tab3:
    stl.header("Interior Features")
    total_bsmt_sf = stl.number_input("Total Basement Area (sq ft)", min_value=0, value=882)
    bsmt_qual = stl.selectbox("Basement Quality", ["Ex", "Gd", "TA", "Fa", "Po", "NA"])
    bsmt_cond = stl.selectbox("Basement Condition", ["Ex", "Gd", "TA", "Fa", "Po", "NA"])
    bsmt_exposure = stl.selectbox("Basement Exposure", ["Gd", "Av", "Mn", "No", "NA"])
    bsmt_full_bath = stl.number_input("Basement Full Bathrooms", min_value=0, value=0)
    bsmt_half_bath = stl.number_input("Basement Half Bathrooms", min_value=0, value=0)
    full_bath = stl.number_input("Full Bathrooms", min_value=0, value=1)
    kitchen_qual = stl.selectbox("Kitchen Quality", ["Ex", "Gd", "TA", "Fa", "Po"])
    kitchen_abv_gr = stl.number_input("Kitchens Above Grade", min_value=0, value=1)
    tot_rms_abv_grd = stl.number_input("Total Rooms Above Grade", min_value=0, value=5)
    fireplaces = stl.number_input("Number of Fireplaces", min_value=0, value=0)
    heating = stl.selectbox("Heating Type", ["GasA", "GasW", "Grav", "Wall", "OthW", "Floor"])
    heating_qc = stl.selectbox("Heating Quality", ["Ex", "Gd", "TA", "Fa", "Po"])
    central_air = stl.radio("Central Air Conditioning", ["Y", "N"])
    electrical = stl.selectbox("Electrical System", ["SBrkr", "FuseA", "FuseF", "FuseP", "Mix"])
    first_flr_sf = stl.number_input("First Floor Area (sq ft)", min_value=0, value=856)
    second_flr_sf = stl.number_input("Second Floor Area (sq ft)", min_value=0, value=854)

with tab4:
    stl.header("Garage & Additional Features")
    garage_type = stl.selectbox("Garage Type", ["Attchd", "Detchd", "BuiltIn", "CarPort", "Basment", "2Types", "NA"])
    garage_yr_blt = stl.slider("Garage Year Built", min_value=1800, max_value=2025, value=1961)
    garage_finish = stl.selectbox("Garage Finish", ["Fin", "RFn", "Unf", "NA"])
    garage_cars = stl.number_input("Garage Car Capacity", min_value=0, value=1)
    garage_area = stl.number_input("Garage Area (sq ft)", min_value=0, value=730)
    paved_drive = stl.selectbox("Paved Driveway", ["Y", "P", "N"])
    wood_deck_sf = stl.number_input("Wood Deck Area (sq ft)", min_value=0, value=140)
    open_porch_sf = stl.number_input("Open Porch Area (sq ft)", min_value=0, value=0)
    enclosed_porch = stl.number_input("Enclosed Porch Area (sq ft)", min_value=0, value=0)
    three_ssn_porch = stl.number_input("Three Season Porch Area (sq ft)", min_value=0, value=0)
    screen_porch = stl.number_input("Screen Porch Area (sq ft)", min_value=0, value=120)
    pool_area = stl.number_input("Pool Area (sq ft)", min_value=0, value=0)
    fence = stl.selectbox("Fence Quality", ["GdPrv", "MnPrv", "GdWo", "MnWw", "NA"])
    mo_sold = stl.slider("Month Sold", min_value=1, max_value=12, value=6)
    yr_sold = stl.slider("Year Sold", min_value=2006, max_value=2010, value=2010)
    sale_type = stl.selectbox("Sale Type", ["WD", "CWD", "VWD", "New", "COD", "Con", "ConLw", "ConLI", "ConLD", "Oth"])
    sale_condition = stl.selectbox("Sale Condition", ["Normal", "Abnorml", "AdjLand", "Alloca", "Family", "Partial"])

#Organize input into a DataFrame
input_data = pd.DataFrame({
    "LotArea": [lot_area],
    "LotFrontage": [lot_frontage],
    "Street": [street],
    "Utilities": [utilities],
    "LotConfig": [lot_config],
    "Condition1": [condition1],
    "Condition2": [condition2],
    "OverallQual": [overall_qual],
    "OverallCond": [overall_cond],
    "YearBuilt": [year_built],
    "YearRemodAdd": [year_remod_add],
    "HouseStyle": [house_style],
    "RoofStyle": [roof_style],
    "RoofMatl": [roof_matl],
    "Exterior1st": [exterior1st],
    "Exterior2nd": [exterior2nd],
    "Foundation": [foundation],
    "TotalBsmtSF": [total_bsmt_sf],
    "BsmtQual": [bsmt_qual],
    "BsmtCond": [bsmt_cond],
    "BsmtExposure": [bsmt_exposure],
    "BsmtFullBath": [bsmt_full_bath],
    "BsmtHalfBath": [bsmt_half_bath],
    "FullBath": [full_bath],
    "KitchenQual": [kitchen_qual],
    "KitchenAbvGr": [kitchen_abv_gr],
    "TotRmsAbvGrd": [tot_rms_abv_grd],
    "Fireplaces": [fireplaces],
    "Heating": [heating],
    "HeatingQC": [heating_qc],
    "CentralAir": [central_air],
    "Electrical": [electrical],
    "1stFlrSF": [first_flr_sf],
    "2ndFlrSF": [second_flr_sf],
    "GrLivArea": [gr_liv_area],
    "LowQualFinSF": [low_qual_fin_sf],
    "GarageType": [garage_type],
    "GarageYrBlt": [garage_yr_blt],
    "GarageFinish": [garage_finish],
    "GarageCars": [garage_cars],
    "GarageArea": [garage_area],
    "PavedDrive": [paved_drive],
    "WoodDeckSF": [wood_deck_sf],
    "OpenPorchSF": [open_porch_sf],
    "EnclosedPorch": [enclosed_porch],
    "3SsnPorch": [three_ssn_porch],
    "ScreenPorch": [screen_porch],
    "PoolArea": [pool_area],
    "Fence": [fence],
    "MoSold": [mo_sold],
    "YrSold": [yr_sold],
    "SaleType": [sale_type],
    "SaleCondition": [sale_condition]
})

#Prediction Button 
if stl.button("Predict House Price"):
    try:
        # One-hot encode categorical variables
        input_data_encoded = pd.get_dummies(input_data, drop_first=True)
        
        # Load the training data to get all possible columns
        train_data = pd.read_csv("train.csv")
        train_data_encoded = pd.get_dummies(train_data, drop_first=True)
        
        # Ensure all columns from training data are present in input data
        for col in train_data_encoded.columns:
            if col not in input_data_encoded.columns and col != 'SalePrice':
                input_data_encoded[col] = 0
        
        # Reorder columns to match training data
        input_data_encoded = input_data_encoded[train_data_encoded.columns.drop('SalePrice')]
        
        # Make prediction
        prediction = model.predict(input_data_encoded)
        stl.success(f'Predicted Price of the House is: ${prediction[0]:,.2f}')
    except Exception as e:
        stl.error(f"An error occurred during prediction: {str(e)}")