import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Configuración visual para diseñadores
st.set_page_config(page_title="PB Finance OS", page_icon="⚡")
st.markdown("<style>main {background-color: #000; color: #0fF;}</style>", unsafe_allow_html=True)

# Conexión a tu Google Sheet
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("⚡ PB FINANCE : OPERATING SYSTEM")

# Formulario rápido para la micro
with st.form("registro"):
    detalle = st.text_input("¿Qué compraste?")
    monto = st.number_input("Monto ($)", step=1000)
    origen = st.selectbox("Origen", ["Sueldo Base", "Bolsa Extras"])
    if st.form_submit_button("INYECTAR MOVIMIENTO"):
        st.balloons()
        st.success("Registrado en la nube")

# Visualización de tus 'Saquitos'
st.divider()
st.subheader("🎒 ESTADO DE SAQUITOS")
st.write("Vacaciones 🏖️")
st.progress(0.45)
