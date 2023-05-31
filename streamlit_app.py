import streamlit as st
import numpy as np
import pickle
import os

# Streamlit uygulamasının başlığı
st.title('Credit Approval Prediction App')

column_mappings = {
    'job': {'admin.': 0, 'blue-collar': 1, 'entrepreneur': 2, 'housemaid': 3, 'management': 4, 'retired': 5, 'self-employed': 6, 'services': 7, 'student': 8, 'technician': 9, 'unemployed': 10},
    'education': {'basic.4y': 0, 'basic.6y': 1, 'basic.9y': 2, 'high.school': 3, 'illiterate': 4, 'professional.course': 5, 'university.degree': 6},
    'day_of_week': {'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3, 'fri': 4},
}

# Kullanıcıdan girişleri alma
input_data = []
input_labels = ['euribor3m', 'age', 'nr. of employers',
                'job', 'campaign', 'day_of_week', 'education']
for i in range(input_labels.__len__()):
    if input_labels[i] in column_mappings:
        input_value = st.selectbox(
            input_labels[i], list(column_mappings[input_labels[i]].keys()))
        input_value = column_mappings[input_labels[i]][input_value]
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
