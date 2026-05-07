import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="PT. Karya Kerinci Seblat",
    page_icon="🏭",
    layout="wide"
)

# Sidebar menu
menu = st.sidebar.selectbox(
    "Pilih Halaman",
    ["Home", "Bahan Baku Masuk", "Produk Jadi"]
)

# =====================================
# HALAMAN HOME
# =====================================
if menu == "Home":

    st.title("🏭 PT. Karya Kerinci Seblat")

    st.image(
        "https://images.unsplash.com/photo-1517048676732-d65bc937f952",
        use_container_width=True
    )

    st.header("Selamat Datang")

    st.write("""
    Website ini digunakan untuk:
    - Monitoring bahan baku masuk
    - Monitoring produk jadi
    - Pendataan produksi perusahaan
    """)

    st.subheader("Tentang Perusahaan")

    st.write("""
    PT. Karya Kerinci Seblat merupakan perusahaan yang bergerak 
    di bidang industri dan produksi.
    """)

    st.success("Silakan pilih menu di sidebar kiri.")

# =====================================
# HALAMAN BAHAN BAKU MASUK
# =====================================
elif menu == "Bahan Baku Masuk":

    st.title("📦 Jumlah Bahan Baku Masuk")

    nama_bahan = st.text_input("Nama Bahan Baku")

    jumlah = st.number_input(
        "Jumlah Bahan Baku (Kg)",
        min_value=0
    )

    if st.button("Simpan Data"):
        st.success(
            f"Data {nama_bahan} sebanyak {jumlah} Kg berhasil disimpan!"
        )

    st.subheader("Data Bahan Baku")

    sample_data = pd.DataFrame({
        "Nama Bahan": ["Kayu", "Besi", "Plastik"],
        "Jumlah (Kg)": [500, 300, 200]
    })

    st.table(sample_data)

# =====================================
# HALAMAN PRODUK JADI
# =====================================
elif menu == "Produk Jadi":

    st.title("🏷️ Produk Jadi")

    produk = st.text_input("Nama Produk")

    jumlah_produk = st.number_input(
        "Jumlah Produk",
        min_value=0
    )

    if st.button("Tambah Produk"):
        st.success(
            f"Produk {produk} sebanyak {jumlah_produk} berhasil ditambahkan!"
        )

    st.subheader("Daftar Produk Jadi")

    produk_data = pd.DataFrame({
        "Nama Produk": ["Meja", "Kursi", "Lemari"],
        "Jumlah": [50, 80, 25]
    })

    st.table(produk_data)
