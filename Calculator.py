import streamlit as st

st.title("Kalkulator Sederhana")

# Input angka pertama
angka1 = st.number_input("Masukkan angka pertama", value=0)

# Input angka kedua
angka2 = st.number_input("Masukkan angka kedua", value=0)

# Pilih operasi
operasi = st.selectbox("Pilih operasi", ["Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)"])

# Tombol hitung
if st.button("Hitung"):
    if operasi == "Tambah (+)":
        hasil = angka1 + angka2
    elif operasi == "Kurang (-)":
        hasil = angka1 - angka2
    elif operasi == "Kali (×)":
        hasil = angka1 * angka2
    elif operasi == "Bagi (÷)":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            hasil = "Tidak bisa dibagi nol"
    st.success(f"Hasil: {hasil}")
