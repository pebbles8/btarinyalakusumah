import streamlit as st

st.title("Pebbles")
st.write(
    "Btari Nyala Kusumah, an avid movie watcher."
)
st.image("IMG_0698.jpeg", width=200)



#st.header("Aplikasi Mengecek Nilai Genap/Ganjil") 
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0: 
    st.write(f"{angka} adalah Bilangan Genap") 
else: 
    st.write(f"{angka} adalah Bilangan Ganjil")
