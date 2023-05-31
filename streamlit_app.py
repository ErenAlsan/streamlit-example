import streamlit as st

# Streamlit uygulamasının başlığı
st.title('Credit Approval Prediction App')

# Kullanıcıdan girişleri alma
input_data = []
for i in range(8):
    input_value = st.text_input(f'TAE Input {i+1}')
    input_data.append(input_value)

# Tahmin yapma butonu
if st.button('Can You get a loan?'):
    # Burada tahmin yapma işlemini gerçekleştirebilirsiniz
    # Örnek olarak, giriş verilerini kullanarak tahmin sonucunu hesaplayabilirsiniz
    # prediction = model.predict(input_data)

    # Tahmin sonucunu ekrana yazdırma
    st.subheader('Result:')
    # st.write(prediction)
