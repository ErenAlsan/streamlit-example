import streamlit as st
import pandas as pd
import joblib

# Modeli yükleme
model = joblib.load('model.pkl')

# Streamlit uygulamasının başlığı
st.title('Model Sonuçları')

# Kullanıcıdan girişleri alma
input_data = []
for i in range(8):
    input_value = st.text_input(f'TAE Input {i+1}')
    input_data.append(input_value)

# Giriş verilerini DataFrame'e dönüştürme
input_df = pd.DataFrame([input_data], columns=['TAE Input 1', 'TAE Input 2', 'TAE Input 3', 'TAE Input 4',
                                               'TAE Input 5', 'TAE Input 6', 'TAE Input 7', 'TAE Input 8'])

# Modeli kullanarak tahmin yapma
prediction = model.predict(input_df)

# Sonucu ekrana yazdırma
st.subheader('Tahmin Sonucu:')
st.write(prediction)
