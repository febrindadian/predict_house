import pickle
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Membaca model
house_model = pickle.load(open('house_price_predict.sav', 'rb'))

# Judul web
st.title('Prediksi Harga Rumah')

# Input data dengan validasi
st.sidebar.header('Input Data')
def user_input_features():
    SquareFeet = st.sidebar.text_input('SquareFeet', '0.0')
    Bedrooms = st.sidebar.text_input('Bedrooms', '0.0')
    Bathrooms = st.sidebar.text_input('Bathrooms', '0.0')
    Neighborhood = st.sidebar.text_input('Neighborhood', '0.0')
    YearBuilt = st.sidebar.text_input('YearBuilt', '0.0')
    data = {
        'SquareFeet': float(SquareFeet),
        'Bedrooms': float(Bedrooms),
        'Bathrooms': float(Bathrooms),
        'Neighborhood': float(Neighborhood),
        'YearBuilt': float(YearBuilt)
    }
    return data

data = user_input_features()

# Menampilkan data input
st.subheader('Input Data')
st.write(data)

if st.button('Prediksi'):
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[data['SquareFeet'], data['Bedrooms'], data['Bathrooms'], data['Neighborhood']], data['YearBuilt']])

        # Lakukan prediksi
        prediksi_rumah = house_model.predict(inputs)
        probabilities = house_model.predict_proba(inputs)  # Mendapatkan probabilitas
        
        # Menampilkan hasil prediksi
        st.subheader('Hasil Prediksi')
        if prediction[0] == 'Low':
            print('Harga rumah dalam kategori Low')
        elif prediction[0] == 'Medium':
            print('Harga rumah dalam kategori Medium')
        elif prediction[0] == 'High':
            print('Harga rumah dalam kategori High')
        elif prediction[0] == 'Very High':
            print('Harga rumah dalam kategori Very High')
        else:
            print('Harga rumah dalam kategori Luxury')

        # Visualisasi probabilitas
        fig, ax = plt.subplots()
        classes = ['Low', 'Medium', 'High', 'Very High', 'Luxury']
        ax.bar(classes, probabilities[0])
        ax.set_ylabel('Probabilitas')
        ax.set_title('Probabilitas Prediksi')
        st.pyplot(fig)
    
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
