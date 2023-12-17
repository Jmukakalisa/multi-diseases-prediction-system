"""
Created on Sun Nov 26 11:53:51 2023

@author: Jeanne Mukakalisa
"""

import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
try:

    diabetes_model = pickle.load(open('models/diabetes_model.sav', 'rb'))

    kidney_model = pickle.load(open('models/Kidney_model.sav', 'rb'))

    heart_disease_model = pickle.load(open('models/heart_disease_model.sav','rb'))

    parkinsons_model = pickle.load(open('models/parkinsons_model.sav', 'rb'))

    breast_cancer_model = pickle.load(open('models/breast_cancer_model.sav', 'rb'))

    hepatitis_model = pickle.load(open('models/hepatitis_model.sav', 'rb'))

    model_accuracies = {
    'diabetes': 0.87,  # replace with actual calculated accuracy
    'diabetes_test': 0.85,  # replace with actual calculated accuracy
    'kidney': 1.0,
    'kidney_test': 0.98,
    'heart_disease': 0.85,
    'heart_disease_test': 0.81,
    'parkinsons': 1.0,
    'parkinsons_test': 0.89,
    'breast_cancer': 0.98,
    'breast_cancer_test': 0.98,
    'hepatitis': 0.94,
    'hepatitis_test': 0.91
}


except FileNotFoundError:
    st.error("Model file not found. Please check the file path.")
    st.stop()

    
def validate_input(input_value):
    try:
        return float(input_value)
    except ValueError:
        return None


# Function to sign up a new user
def signup(email, username, password):
    users = st.session_state['users']
    if email in users:
        st.error("Email already exists.")
    else:
        users[username] = password
        st.success("Account created successfully. Please log in.")
        pass

# Function to log in a user
def login(email, password):
    users = st.session_state['users']
    if email in users and users[email] == password:
        st.session_state['current_user'] = email
        st.success(f"Logged in as {email}")
    else:
        st.error("Invalid email or password.")
        pass

def show_auth():
    # User is not logged in; show login and signup options
    with st.sidebar:
        auth_selection = option_menu(
            "Auth",
            ["Login", "Signup"],
            icons=['log-in', 'person-plus-fill'],
            menu_icon="cast",
            default_index=0,
            key='auth_selection_sidebar'
        )

# Check if a user is logged in
    if 'current_user' not in st.session_state or not st.session_state['current_user']:
        # User is not logged in; show login and signup options
        
        # with st.sidebar:
        #     auth_selection = option_menu("Auth", ["Login", "Signup"], icons=['log-in', 'person-plus-fill'], menu_icon="cast", default_index=0)
        
        if auth_selection == "Signup":
            st.subheader("Create a new account")
            new_email = st.text_input("Email", key="new_email")
            new_username = st.text_input("Username", key="new_username")
            new_password = st.text_input("Password", type="password", key="new_password")
            if st.button("Sign up"):
                signup(new_email, new_username, new_password)
                pass
        
        elif auth_selection == "Login":
            st.subheader("Log in")
            email = st.text_input("Email", key="email")
            password = st.text_input("Password", type="password", key="password")
            if st.button("Log in"):
                login(email, password)
                pass
    else:
        # User is logged in; show the main app or a logout button
        st.sidebar.success(f"Logged in as {st.session_state['current_user']}")
        if st.sidebar.button("Log out"):
            del st.session_state['current_user']
        


# Initialize users storage in session state if not already done
if 'users' not in st.session_state:
    st.session_state['users'] = {}

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multi-Disease Prediction System',
                          
                          ['About',
                           'Get Started',
                           'Diabetes Prediction',
                           'Kidney Prediction',
                           'Heart Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction',
                           'Hepatitis C Prediction'],
                          icons=['house', 'play-circle','activity','droplet', 'heart','person', 'bandaid', 'heart-pulse'],
                          default_index=0,
                          key='main_option_menu'
                          )

if (selected == 'About'):
    st.title('About This System')

    st.write('''Developed by Jeanne Mukakalisa, the Multi-Disease Prediction System is a cutting-edge application designed to bring the power of machine learning and predictive analytics directly to users seeking quick health assessments across various conditions, including diabetes, kidney disease, heart disease, Parkinson's, breast cancer, and hepatitis C. Leveraging a suite of sophisticated models, each meticulously trained on comprehensive datasets specific to the conditions they predict, the application offers an intuitive interface that guides users through a seamless process of inputting their health metrics. Upon submission, the system utilizes its predictive models to analyze the inputs and returns a prediction that helps in understanding potential health risks.

The system is built with the user in mind, featuring a straightforward navigation sidebar that simplifies the journey through different prediction modules. Its design ensures that even those with minimal medical or technical knowledge can interact with the platform effectively, making health prediction accessible to a wider audience. This initiative not only exemplifies the potential of artificial intelligence in enhancing public health awareness and early diagnosis but also showcases Jeanne's commitment to leveraging technology for the betterment of community health outcomes. Through this application, users are empowered with knowledge about their health, enabling informed decisions and encouraging proactive health management.''')
    
    st.button( 'Get Stared')

    # show_auth()  # Place this where you want the Get Started button to appear

elif selected == 'Get Started':
    show_auth()

# if 'current_user' in st.session_state and st.session_state['current_user']:
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction System')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = validate_input(st.text_input('Number of Pregnancies'))
        
    with col2:
        Glucose = validate_input(st.text_input('Glucose Level'))
    
    with col3:
        BloodPressure = validate_input(st.text_input('Blood Pressure value'))
    
    with col1:
        SkinThickness = validate_input(st.text_input('Skin Thickness value'))
    
    with col2:
        Insulin = validate_input(st.text_input('Insulin Level'))
    
    with col3:
        BMI = validate_input(st.text_input('BMI value'))
    
    with col1:
        DiabetesPedigreeFunction = validate_input(st.text_input('Diabetes Pedigree Function value'))
    
    with col2:
        Age = validate_input(st.text_input('Age of the Person'))
    
    
    # code for Prediction
    diabetes_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Test Result'):

        if None in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]:
            st.error("Invalid input. Please enter numeric values.")
        else:
            diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diabetes_prediction[0] == 1):
                diabetes_diagnosis = 'The person is diabetic'
            else:
                diabetes_diagnosis = 'The person is not diabetic'
            
            accuracy_msg = f"Training Accuracy Score: {model_accuracies['diabetes']:.2%}"
            accuracy_test = f"Test Accuracy Score: {model_accuracies['diabetes_test']:.2%}"
            st.success(f"{diabetes_diagnosis}, \n{accuracy_msg}, \n{accuracy_test}")
            pass



    
# Kidney Prediction Page
if (selected == 'Kidney Prediction'):
    
    # page title
    st.title('Chronic Kidney Prediction System')
    
    
    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        age = validate_input(st.text_input('Age'))
        
    with col2:
        blood_pressure = validate_input(st.text_input('Blood Pressure'))
    
    with col3:
        specific_gravity = validate_input(st.text_input('Specific Gravity'))
    
    with col4:
        albumin = validate_input(st.text_input('Albumin')
)
    with col1:
        sugar = validate_input(st.text_input('Sugarred Blood Cells'))

    with col2:
        red_blood_cells = validate_input(st.text_input('Red Blood Cells'))        
    
    with col3:
        pus_cell = validate_input(st.text_input('Pus Cell'))
    
    with col4:
        pus_cell_clumps = validate_input(st.text_input('Pus Cell Clumps'))
    
    with col1:
        bacteria = validate_input(st.text_input('Bacteria'))

    with col2:
        blood_glucose_random = validate_input(st.text_input('Blood Glucose Random'))

    with col3:
        blood_urea = validate_input(st.text_input('Blood Urea'))

    with col4:
        serum_creatinine = validate_input(st.text_input('Serum Creatinine'))

    with col1:
        sodium = validate_input(st.text_input('Sodium'))

    with col2:
        potassium = validate_input(st.text_input('Potassium'))

    with col3:
        haemoglobin = validate_input(st.text_input('Haemoglobin')) 

    with col4:
        packed_cell_volume = validate_input(st.text_input('Packed Cell Volume'))

    with col1:
        white_blood_cell_count = validate_input(st.text_input('White Blood Cell Count'))

    with col2:
        red_blood_cell_count = validate_input(st.text_input('Red Blood Cell Count'))

    with col3:
        hypertension = validate_input(st.text_input('Hypertension'))

    with col4:
        diabetes_mellitus = validate_input(st.text_input('Diabetes Mellitus'))

    with col1:
        coronary_artery_disease = validate_input(st.text_input('Coronary Artery Disease'))

    with col2:
        appetite = validate_input(st.text_input('Appetite'))

    with col3:
        peda_edema = validate_input(st.text_input('Peda Edema'))

    with col4:
        aanemia = validate_input(st.text_input('Aanemia'))
    
    
    # code for Prediction
    kidney_diagnosis = ''
    
# creating a button for Prediction
    if st.button('Test Result'):
        # Prepare and validate input data
        input_data = [
            age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
            blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, 
            white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, 
            appetite, peda_edema, aanemia
        ]

        # Check if any input is invalid
        if None in input_data:
            st.error("Invalid input. Please enter numeric values.")
        else:
            # Create DataFrame for prediction
            data = pd.DataFrame([input_data], columns=[
                'age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar', 'red_blood_cells', 'pus_cell', 'pus_cell_clumps', 'bacteria',
                'blood_glucose_random', 'blood_urea', 'serum_creatinine', 'sodium', 'potassium', 'haemoglobin', 'packed_cell_volume', 
                'white_blood_cell_count', 'red_blood_cell_count', 'hypertension', 'diabetes_mellitus', 'coronary_artery_disease', 
                'appetite', 'peda_edema', 'aanemia'
            ])
            
            # Make prediction
            kidney_prediction = kidney_model.predict(data)

            # Interpret prediction
            if kidney_prediction[0] == 1:
                kidney_diagnosis = 'The Person has a Chronic Kidney Disease'
            else:
                kidney_diagnosis = 'The Person does not have a Chronic Kidney Disease'

            accuracy_msg = f"Training Accuracy Score: {model_accuracies['kidney']:.2%}"
            accuracy_test = f"Test Accuracy Score: {model_accuracies['kidney_test']:.2%}"
            st.success(f"{kidney_diagnosis}, \n{accuracy_msg}, \n{accuracy_test}")
            pass



# Heart Disease Prediction Page
if (selected == 'Heart Prediction'):
    
    # page title
    st.title('Heart Disease Prediction System')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = validate_input(st.text_input('Age'))
        
    with col2:
        sex = validate_input(st.text_input('Sex'))
        
    with col3:
        cp = validate_input(st.text_input('Chest Pain types'))
        
    with col1:
        trestbps = validate_input(st.text_input('Resting Blood Pressure'))
        
    with col2:
        chol = validate_input(st.text_input('Serum Cholestoral in mg/dl'))
        
    with col3:
        fbs = validate_input(st.text_input('Fasting Blood Sugar > 120 mg/dl'))
        
    with col1:
        restecg = validate_input(st.text_input('Resting Electrocardiographic results'))
        
    with col2:
        thalach = validate_input(st.text_input('Maximum Heart Rate achieved'))
        
    with col3:
        exang = validate_input(st.text_input('Exercise Induced Angina'))
        
    with col1:
        oldpeak = validate_input(st.text_input('ST depression induced by exercise'))
        
    with col2:
        slope = validate_input(st.text_input('Slope of the peak exercise ST segment'))
        
    with col3:
        ca = validate_input(st.text_input('Major vessels colored by flourosopy'))
        
    with col1:
        thal = validate_input(st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')) 
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Test Result'):
        # Prepare and validate input data
        input_data = [
            age, sex, cp, trestbps, chol, fbs, 
            restecg, thalach, exang, oldpeak, slope, ca, thal
        ]

        # Check if any input is invalid
        if None in input_data:
            st.error("Invalid input. Please enter numeric values.")
        else:
            # Create DataFrame for prediction
            data = pd.DataFrame([input_data], columns=[
                'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
                'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
            ])
            
            # Make prediction
            heart_prediction = heart_disease_model.predict(data)

            # Interpret prediction
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

            accuracy_msg = f"Training Accuracy Score: {model_accuracies['heart_disease']:.2%}"
            accuracy_test = f"Test Accuracy Score: {model_accuracies['heart_disease_test']:.2%}"
            st.success(f"{heart_diagnosis}, \n{accuracy_msg}, \n{accuracy_test}")
            pass
        
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction System")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = validate_input(st.text_input('MDVP:Fo(Hz)'))
        
    with col2:
        fhi = validate_input(st.text_input('MDVP:Fhi(Hz)'))
        
    with col3:
        flo = validate_input(st.text_input('MDVP:Flo(Hz)'))
        
    with col4:
        Jitter_percent = validate_input(st.text_input('MDVP:Jitter(%)'))
        
    with col5:
        Jitter_Abs = validate_input(st.text_input('MDVP:Jitter(Abs)'))
        
    with col1:
        RAP = validate_input(st.text_input('MDVP:RAP'))
        
    with col2:
        PPQ = validate_input(st.text_input('MDVP:PPQ'))
        
    with col3:
        DDP = validate_input(st.text_input('Jitter:DDP'))
        
    with col4:
        Shimmer = validate_input(st.text_input('MDVP:Shimmer'))
        
    with col5:
        Shimmer_dB = validate_input(st.text_input('MDVP:Shimmer(dB)'))
        
    with col1:
        APQ3 = validate_input(st.text_input('Shimmer:APQ3'))
        
    with col2:
        APQ5 = validate_input(st.text_input('Shimmer:APQ5'))
        
    with col3:
        APQ = validate_input(st.text_input('MDVP:APQ'))
        
    with col4:
        DDA = validate_input(st.text_input('Shimmer:DDA'))
        
    with col5:
        NHR = validate_input(st.text_input('NHR'))
        
    with col1:
        HNR = validate_input(st.text_input('HNR'))
        
    with col2:
        RPDE = validate_input(st.text_input('RPDE'))
        
    with col3:
        DFA = validate_input(st.text_input('DFA'))
        
    with col4:
        spread1 = validate_input(st.text_input('spread1'))
        
    with col5:
        spread2 = validate_input(st.text_input('spread2'))
        
    with col1:
        D2 = validate_input(st.text_input('D2'))
        
    with col2:
        PPE = validate_input(st.text_input('PPE'))     

    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Test Result"):
        # Prepare and validate input data
        input_data = [
            fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, 
            APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
        ]

        # Check if any input is invalid
        if None in input_data:
            st.error("Invalid input. Please enter numeric values.")
        else:
            # Creating DataFrame for prediction with correct column names
            data = pd.DataFrame([input_data], columns=[
                'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 
                'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 
                'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 
                'spread1', 'spread2', 'D2', 'PPE'
            ])

            # Make prediction
            parkinsons_prediction = parkinsons_model.predict(data)

            # Interpret prediction
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

            accuracy_msg = f"Training Accuracy Score: {model_accuracies['parkinsons']:.2%}"
            accuracy_test = f"Test Accuracy Score: {model_accuracies['parkinsons_test']:.2%}"
            st.success(f"{parkinsons_diagnosis}, \n{accuracy_msg}, \n{accuracy_test}")
            pass



# breast cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction System')
    
    
    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        mean_radius = validate_input(st.text_input('Mean Radius'))
        
    with col2:
        mean_texture = validate_input(st.text_input('Mean Texture'))
    
    with col3:
        mean_perim = validate_input(st.text_input('Mean Perimeter'))
    
    with col4:
        mean_area = validate_input(st.text_input('Mean Area'))

    with col1:
        mean_smoothness = validate_input(st.text_input('Mean Smoothness'))

    with col2:
        mean_comp = validate_input(st.text_input('Mean Compactness'))       
    
    with col3:       
        mean_concav = validate_input(st.text_input('Mean Concavity'))
    
    with col4:
        mean_concavp = validate_input(st.text_input('Mean Concavity Points'))
    
    with col1:
        mean_sym = validate_input(st.text_input('Mean Symetry'))

    with col2:
        mean_fract_dim = validate_input(st.text_input('Mean Fract_Dim'))

    with col3:
        radius_err = validate_input(st.text_input('Radius Error'))

    with col4:
        texture_err = validate_input(st.text_input('Texture Error'))

    with col1:
        perimeter_err = validate_input(st.text_input('Perimeter Error'))

    with col2:
        area_err = validate_input(st.text_input('Area Error'))

    with col3:
        smothness_err = validate_input(st.text_input('Smothness Error')) 

    with col4:
        compactness_err = validate_input(st.text_input('Compactness Error'))

    with col1:
        concav_err = validate_input(st.text_input('Concavity Error'))

    with col2:
        concavp_err = validate_input(st.text_input('Concavity Point Error'))

    with col3:
        symetry_err = validate_input(st.text_input('Symetry Error'))

    with col4:
        fract_dim_err = validate_input(st.text_input('Fract_Dim_Error'))

    with col1:
        worst_radius = validate_input(st.text_input('Worst Radius'))

    with col2:
        worst_texture = validate_input(st.text_input('Worst Texture'))

    with col3:
        worst_perim = validate_input(st.text_input('Worst Perimeter'))

    with col4:
        worst_area = validate_input(st.text_input('Worst Area'))

    with col1:
        worst_smoothness = validate_input(st.text_input('Worst Smothness'))

    with col2:
        worst_comp = validate_input(st.text_input('Worst Compactness'))

    with col3:
        worst_concav = validate_input(st.text_input('Worst Concavity'))

    with col4:
        worst_concavp = validate_input(st.text_input('Worst Concavity Points'))

    with col1:
        worst_sym = validate_input(st.text_input('Worst Symetry'))

    with col2:
        worst_fract_dim = validate_input(st.text_input('Worst Fract_Dim'))
    
    
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button('Test Result'):
        # Prepare and validate input data
        input_data = [
            mean_radius, mean_texture, mean_perim, mean_area, mean_smoothness, mean_comp, mean_concav, mean_concavp, mean_sym, mean_fract_dim, 
            radius_err, texture_err, perimeter_err, area_err, smothness_err, compactness_err, concav_err, concavp_err, symetry_err, fract_dim_err, 
            worst_radius, worst_texture, worst_perim, worst_area, worst_smoothness, worst_comp, worst_concav, worst_concavp, worst_sym, worst_fract_dim
        ]

        # Check if any input is invalid
        if None in input_data:
            st.error("Invalid input. Please enter numeric values.")
        else:
            # Create DataFrame for prediction
            data = pd.DataFrame([input_data], columns=['mean_radius', 'mean_texture', 'mean_perim', 'mean_area', 'mean_smoothness', 'mean_comp', 'mean_concav', 'mean_concavp', 
                'mean_sym', 'mean_fract_dim', 'radius_err', 'texture_err', 'perimeter_err', 'area_err', 'smothness_err', 'compactness_err', 
                'concav_err', 'concavp_err', 'symetry_err', 'fract_dim_err', 'worst_radius', 'worst_texture', 'worst_perim', 'worst_area', 
                'worst_smoothness', 'worst_comp', 'worst_concav', 'worst_concavp', 'worst_sym', 'worst_fract_dim'
            ])
            
            # Make prediction
            breast_cancer_pred = breast_cancer_model.predict(data)

            # Interpret prediction
            if breast_cancer_pred[0] == 1:
                breast_cancer_diagnosis = 'The Breast Cancer is Benign'
            else:
                breast_cancer_diagnosis = 'The Breast cancer is Malignant'

            # Fetch and display accuracy
            accuracy_msg = f"Training Accuracy Score: {model_accuracies['breast_cancer']:.2%}"
            accuracy_test = f"Test Accuracy Score: {model_accuracies['breast_cancer_test']:.2%}"
            st.success(f"{breast_cancer_diagnosis}, \n{accuracy_msg}, \n{accuracy_test}")
            pass



# Hepatitis C Prediction Page
if (selected == 'Hepatitis C Prediction'):
    
    # page title
    st.title('Hepatitis C Prediction System')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = validate_input(st.text_input('Age'))
        
    with col2:
        Sex = validate_input(st.text_input('Sex'))
    
    with col3:
        ALB = validate_input(st.text_input('Albumin Blood Test'))
    
    with col1:
        ALP = validate_input(st.text_input('Alkaline phosphatase'))

    with col2:
        ALT = validate_input(st.text_input('Alanine Transaminase'))

    with col3:
        AST = validate_input(st.text_input('Aspartate Transaminase'))        
    
    with col1:
        BIL = validate_input(st.text_input('Bilirubin'))
    
    with col2:
        CHE = validate_input(st.text_input('Acetylcholinesterase'))
    
    with col3:
        CHOL = validate_input(st.text_input('Cholesterol'))

    with col1:
        CREA = validate_input(st.text_input('Creatinine'))

    with col2:
        GGT = validate_input(st.text_input('Gamma-Glutamyl Transferase'))

    with col3:
        PROT = validate_input(st.text_input('Total Protein'))
                                    
    
    # code for Prediction
    hepatitis_diagnosis = ''
    

    # creating a button for Prediction    
    if st.button('Test Result'):
        # Prepare and validate input data
        input_data = [
            Age, Sex, ALB, ALP, ALT, AST, BIL, 
            CHE, CHOL, CREA, GGT, PROT
        ]

        # Check if any numeric input is invalid
        if None in input_data:
            st.error("Invalid input. Please enter valid values for all fields.")
        else:
            # Create DataFrame for prediction
            data = pd.DataFrame([input_data], columns=[
                'Age', 'Sex', 'ALB', 'ALP', 'ALT', 'AST', 'BIL', 
                'CHE', 'CHOL', 'CREA', 'GGT', 'PROT'
            ])
            
            # Make prediction
            hepatitis_prediction = hepatitis_model.predict(data)

            # Interpret prediction
            if hepatitis_prediction[0] == 1:
                hepatitis_diagnosis = 'The Person has Hepatitis C Disease'
            else:
                hepatitis_diagnosis = 'The Person does not have Hepatitis C Disease'

                # Fetch and display accuracy
            accuracy_msg = f"Training Accuracy Score: {model_accuracies['hepatitis']:.2%}"
            accuracy_test = f"Test Accuracy Score: {model_accuracies['hepatitis_test']:.2%}"
            st.success(f"{hepatitis_diagnosis}, \n{accuracy_msg}, \n{accuracy_test}")
            pass
# else:
#     st.warning("Please log in to access the app.")
