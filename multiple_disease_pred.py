"""
Created on Sun Nov 26 11:53:51 2023

@author: Jeanne Mukakalisa
"""

import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open(r'C:\Users\mukak\Videos\ML_Assignments\Final_Summative_Multi_Disease_Prediction_System/saved models/diabetes_model.sav', 'rb'))

kidney_model = pickle.load(open(r'C:\Users\mukak\Videos\ML_Assignments\Final_Summative_Multi_Disease_Prediction_System/saved models/Kidney_model.sav', 'rb'))

heart_disease_model = pickle.load(open(r'C:\Users\mukak\Videos\ML_Assignments\Final_Summative_Multi_Disease_Prediction_System/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open(r'C:\Users\mukak\Videos\ML_Assignments\Final_Summative_Multi_Disease_Prediction_System/saved models/parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open(r'C:\Users\mukak\Videos\ML_Assignments\Final_Summative_Multi_Disease_Prediction_System/saved models/breast_cancer_model.sav', 'rb'))

hepatitis_model = pickle.load(open(r'C:\Users\mukak\Videos\ML_Assignments\Final_Summative_Multi_Disease_Prediction_System/saved models/hepatitis_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multi-Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Kidney Prediction',
                           'Heart Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction',
                           'Hepatitis C Prediction'],
                          icons=['activity','droplet', 'heart','person', 'bandaid', 'heart-pulse'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction System')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diabetes_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diabetes_prediction[0] == 1):
          diabetes_diagnosis = 'The person is diabetic'
        else:
          diabetes_diagnosis = 'The person is not diabetic'
        
    st.success(diabetes_diagnosis)


    
# Kidney Prediction Page
if (selected == 'Kidney Prediction'):
    
    # page title
    st.title('Chronic Kidney Prediction System')
    
    
    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        blood_pressure = st.text_input('Blood Pressure')
    
    with col3:
        specific_gravity = st.text_input('Specific Gravity')
    
    with col4:
        albumin = st.text_input('Albumin')

    with col1:
        sugar = st.text_input('Sugarred Blood Cells')

    with col2:
        red_blood_cells = st.text_input('Red Blood Cells')        
    
    with col3:
        pus_cell = st.text_input('Pus Cell')
    
    with col4:
        pus_cell_clumps = st.text_input('Pus Cell Clumps')
    
    with col1:
        bacteria = st.text_input('Bacteria')

    with col2:
        blood_glucose_random = st.text_input('Blood Glucose Random')

    with col3:
        blood_urea = st.text_input('Blood Urea')

    with col4:
        serum_creatinine = st.text_input('Serum Creatinine')

    with col1:
        sodium = st.text_input('Sodium')

    with col2:
        potassium = st.text_input('Potassium')

    with col3:
        haemoglobin = st.text_input('Haemoglobin') 

    with col4:
        packed_cell_volume = st.text_input('Packed Cell Volume')

    with col1:
        white_blood_cell_count = st.text_input('White Blood Cell Count')

    with col2:
        red_blood_cell_count = st.text_input('Red Blood Cell Count')

    with col3:
        hypertension = st.text_input('Hypertension')

    with col4:
        diabetes_mellitus = st.text_input('Diabetes Mellitus')

    with col1:
        coronary_artery_disease = st.text_input('Coronary Artery Disease')

    with col2:
        appetite = st.text_input('Appetite')

    with col3:
        peda_edema = st.text_input('Peda Edema')

    with col4:
        aanemia = st.text_input('Aanemia')
    
    
    # code for Prediction
    kidney_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Test Result'):

        data = pd.DataFrame([[age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
                                                   blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, 
                                                   white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, aanemia]], 
                                                   columns= ['age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar', 'red_blood_cells', 'pus_cell', 'pus_cell_clumps', 'bacteria',
                                                   'blood_glucose_random', 'blood_urea', 'serum_creatinine', 'sodium', 'potassium', 'haemoglobin', 'packed_cell_volume', 
                                                   'white_blood_cell_count', 'red_blood_cell_count', 'hypertension', 'diabetes_mellitus', 'coronary_artery_disease', 'appetite', 'peda_edema', 'aanemia'])
        kidney_prediction = kidney_model.predict(data)
        
        if (kidney_prediction[0] == 1):
          kidney_diagnosis = 'The Person has a Chronic Kidney Disease'
        else:
          kidney_diagnosis = 'The Person does not have a Chronic Kidney Disease'
        
    st.success(kidney_diagnosis)



# Heart Disease Prediction Page
if (selected == 'Heart Prediction'):
    
    # page title
    st.title('Heart Disease Prediction System')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect') 
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Test Result'):

        data = pd.DataFrame([[
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
        ]], columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

        heart_prediction = heart_disease_model.predict(data)

        # heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction System")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')     

    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)



# breast cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction System')
    
    
    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        mean_radius = st.text_input('Mean Radius')
        
    with col2:
        mean_texture = st.text_input('Mean Texture')
    
    with col3:
        mean_perim = st.text_input('Mean Perimeter')
    
    with col4:
        mean_area = st.text_input('Mean Area')

    with col1:
        mean_smoothness = st.text_input('Mean Smoothness')

    with col2:
        mean_comp = st.text_input('Mean Compactness')        
    
    with col3:       
        mean_concav = st.text_input('Mean Concavity')
    
    with col4:
        mean_concavp = st.text_input('Mean Concavity Points')
    
    with col1:
        mean_sym = st.text_input('Mean Symetry')

    with col2:
        mean_fract_dim = st.text_input('Mean Fract_Dim')

    with col3:
        radius_err = st.text_input('Radius Error')

    with col4:
        texture_err = st.text_input('Texture Error')

    with col1:
        perimeter_err = st.text_input('Perimeter Error')

    with col2:
        area_err = st.text_input('Area Error')

    with col3:
        smothness_err = st.text_input('Smothness Error') 

    with col4:
        compactness_err = st.text_input('Compactness Error')

    with col1:
        concav_err = st.text_input('Concavity Error')

    with col2:
        concavp_err = st.text_input('Concavity Point Error')

    with col3:
        symetry_err = st.text_input('Symetry Error')

    with col4:
        fract_dim_err = st.text_input('Fract_Dim_Error')

    with col1:
        worst_radius = st.text_input('Worst Radius')

    with col2:
        worst_texture = st.text_input('Worst Texture')

    with col3:
        worst_perim = st.text_input('Worst Perimeter')

    with col4:
        worst_area = st.text_input('Worst Area')

    with col1:
        worst_smoothness = st.text_input('Worst Smothness')

    with col2:
        worst_comp = st.text_input('Worst Compactness') 

    with col3:
        worst_concav = st.text_input('Worst Concavity')

    with col4:
        worst_concavp = st.text_input('Worst Concavity Points')

    with col1:
        worst_sym = st.text_input('Worst Symetry')

    with col2:
        worst_fract_dim = st.text_input('Worst Fract_Dim')
    
    
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Test Result'):
        breat_cancer_pred = breast_cancer_model.predict([[mean_radius, mean_texture, mean_perim, mean_area, mean_smoothness, mean_comp, mean_concav, mean_concavp,
        mean_sym, mean_fract_dim, radius_err, texture_err, perimeter_err, area_err, smothness_err, compactness_err, concav_err, concavp_err, symetry_err, fract_dim_err,
        worst_radius, worst_texture, worst_perim, worst_area,worst_smoothness, worst_comp, worst_concav, worst_concavp, worst_sym, worst_fract_dim]])
        
        if (breat_cancer_pred[0] == 1):
          breast_cancer_diagnosis = 'The Breast Cancer is Benign     '
        else:
          breast_cancer_diagnosis = 'The Breast cancer is Malignant'
        
    st.success(breast_cancer_diagnosis)



# Hepatitis C Prediction Page
if (selected == 'Hepatitis C Prediction'):
    
    # page title
    st.title('Hepatitis C Prediction System')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        Sex = st.text_input('Sex')
    
    with col3:
        ALB = st.text_input('Albumin Blood Test')
    
    with col1:
        ALP = st.text_input('Alkaline phosphatase')

    with col2:
        ALT = st.text_input('Alanine Transaminase')

    with col3:
        AST = st.text_input('Aspartate Transaminase')        
    
    with col1:
        BIL = st.text_input('Bilirubin')
    
    with col2:
        CHE = st.text_input('Acetylcholinesterase')
    
    with col3:
        CHOL = st.text_input('Cholesterol')

    with col1:
        CREA = st.text_input('Creatinine')

    with col2:
        GGT = st.text_input('Gamma-Glutamyl Transferase')

    with col3:
        PROT = st.text_input('Total Protein')
    								
    
    # code for Prediction
    hepatitis_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Test Result'):
        hepatitis_prediction = hepatitis_model.predict([[Age, Sex, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT]])
        
        if (hepatitis_prediction[0] == 1):
          hepatitis_diagnosis = 'The Person has Hepatitis C Disease'
        else:
          hepatitis_diagnosis = 'The Person does not have Hepatitis C Disease'
        
    st.success(hepatitis_diagnosis)
