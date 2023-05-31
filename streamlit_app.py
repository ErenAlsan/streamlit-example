import streamlit as st

# Streamlit uygulamasının başlığı
st.title('Credit Approval Prediction App')

# Kullanıcıdan girişleri alma
input_data = []
input_labels = ['duration', 'euribor3m', 'age', 'nr. of employers', 'job', 'campaign', 'day_of_week', 'education']
for i in range(8):
    input_value = st.text_input(input_labels[i])
    input_data.append(input_value)

# Tahmin yapma butonu
if st.button('Can You Get a Loan?'):
    # Burada tahmin yapma işlemini gerçekleştirebilirsiniz
    # Örnek olarak, giriş verilerini kullanarak tahmin sonucunu hesaplayabilirsiniz
    # prediction = model.predict(input_data)

    # Tahmin sonucunu ekrana yazdırma
    st.subheader('Result:')
    # st.write(prediction)
