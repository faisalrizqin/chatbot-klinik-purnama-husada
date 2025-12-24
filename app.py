import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ========================
# KONFIGURASI AWAL
# ========================
st.set_page_config(
    page_title="Chatbot Klinik Purnama Husada",
    page_icon="🩺",
    layout="wide"
)

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# ========================
# SIDEBAR
# ========================
with st.sidebar:
    st.image("logo.png", width=180)
    st.title("Klinik Purnama Husada")
    st.write("**Dr. Nur Widyastuti, M.KM**")
    st.markdown("---")

    menu = st.radio(
        "Menu",
        ["Chatbot AI", "Profil Klinik", "Layanan", "Jadwal Dokter", "Kontak & Lokasi"]
    )

# ========================
# HALAMAN CHATBOT
# ========================
if menu == "Chatbot AI":
    st.header("💬 Chatbot AI Klinik Purnama Husada")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Tulis pertanyaan Anda:")

    if st.button("Kirim"):
        if user_input:
            prompt = f"""
            Kamu adalah chatbot resmi Klinik Purnama Husada by Dr. Nur Widyastuti, M.KM.
            Klinik memiliki Poli Umum dan Poli Gigi.
            Jawablah dengan bahasa sopan, singkat, dan informatif.

            Pertanyaan pasien:
            {user_input}
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.session_state.chat_history.append(
                ("Pasien", user_input)
            )
            st.session_state.chat_history.append(
                ("Chatbot", response.text)
            )

    for role, message in st.session_state.chat_history:
        if role == "Pasien":
            st.markdown(f"**🧑 Pasien:** {message}")
        else:
            st.markdown(f"**🤖 Chatbot:** {message}")

# ========================
# PROFIL KLINIK
# ========================
elif menu == "Profil Klinik":
    st.header("🏥 Profil Klinik")

    st.write("""
    **Nama Klinik:** Klinik Purnama Husada  
    **Pemilik:** Dr. Nur Widyastuti, M.KM  

    Klinik Purnama Husada merupakan fasilitas pelayanan kesehatan
    yang menyediakan layanan **Poli Umum** dan **Poli Gigi**
    untuk masyarakat umum.
    """)

# ========================
# LAYANAN
# ========================
elif menu == "Layanan":
    st.header("🩺 Layanan Klinik")

    st.subheader("Poli Umum")
    st.write("""
    - Konsultasi  
    - Kesehatan Ibu & Anak (KIA & KB)  
    - Bedah Minor  
    - Laboratorium Sederhana  
    - Promosi Kesehatan  
    - Home Visit  
    """)

    st.subheader("Poli Gigi")
    st.write("""
    - Konsultasi  
    - Bedah Mulut Minor  
    - Penambalan Gigi  
    - Pencabutan gigi dewasa & anak  
    - Pembersihan karang gigi  
    - Pembuatan gigi tiruan  
    """)

# ========================
# JADWAL DOKTER
# ========================
elif menu == "Jadwal Dokter":
    st.header("📅 Jadwal Praktek Dokter")

    st.subheader("Poli Umum")
    st.write("""
    **dr. Tiwin Wiharsih**  
    Senin–Sabtu: 07.00–11.00  
    Ahad/Hari Besar: Tutup  

    **Dr. Nur Widyastuti, M.KM**  
    Senin–Jumat: 16.00–20.00  
    Sabtu: 15.00–19.00  
    Ahad/Hari Besar: Tutup  
    """)

    st.subheader("Poli Gigi")
    st.write("""
    **drg. Etty Handayaningsih**  
    Senin–Kamis: 14.00–18.00  
    Jumat: 12.00–16.00  
    Sabtu: 13.00–17.00  
    Ahad/Hari Besar: Tutup  
    """)

# ========================
# KONTAK & LOKASI
# ========================
elif menu == "Kontak & Lokasi":
    st.header("📍 Kontak & Lokasi")

    st.write("""
    **Alamat:**  
    Jl. Raya Soekarno-Hatta No.111, Kersan, Kebondalem,  
    Kec. Kendal, Kab. Kendal, Jawa Tengah 51318
    """)

    st.markdown(
        "[📍 Lihat Lokasi di Google Maps](https://www.google.com/maps/place/Klinik+Purnama+Husada+by+Dr.+Nur+Widyastuti/@-6.9277279,110.2074678,17z/data=!3m1!4b1!4m6!3m5!1s0x2e705c416a874dad:0x1c09fe1e80abf72d!8m2!3d-6.9277279!4d110.2074678!16s%2Fg%2F11dzlf527l!5m1!1e1?entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoASAFQAw%3D%3D)"
    )

    st.write("""
    **Instagram:** @klinikpurnamahusada  
    **Pendaftaran Poli Umum:** Aplikasi JKN Mobile  
    **Reservasi Poli Gigi (WhatsApp = 082313522209):**  
    """)

    st.markdown(
        "[💬 Chat WhatsApp Admin](https://api.whatsapp.com/send/?phone=6282313522209)"
    )
