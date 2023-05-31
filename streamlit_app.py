import streamlit as st
import numpy as np
import pickle
import os

# Streamlit uygulamasının başlığı
st.title('Credit Approval Prediction App')

# Kullanıcıdan girişleri alma
input_data = []
input_labels = ['duration', 'euribor3m', 'age', 'nr. of employers',
                'job', 'campaign', 'day_of_week', 'education']
for i in range(8):
    if input_labels[i] == 'job':
        job_options = ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management',
                       'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown']
        input_value = st.selectbox(input_labels[i], job_options)
    else:
        input_value = st.text_input(input_labels[i])
    input_data.append(float(input_value) if input_value else 0.0)

# Tahmin yapma butonu
if st.button('Can You Get a Loan?'):
    # Modeli yükleme
    classifier = pickle.load(
        open('deployment/model.sav', 'rb'))

    # Giriş verilerini numpy dizisine dönüştürme
    input_data = np.array([input_data])

    # Tahmini gerçekleştirme
    prediction = classifier.predict(input_data)

    # Tahmin sonucunu ekrana yazdırma
    st.subheader('Result:')
    if prediction == 1:
        st.write("Congratulations, you can get a loan!")
    else:
        st.write("Sorry, you are not eligible to get a loan.")
