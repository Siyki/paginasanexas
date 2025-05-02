import streamlit as st
from PIL import Image

st.set_page_config(page_title="Mi primera chamba", page_icon="🎨", layout="wide")

st.markdown(
    '<style>body {background-color: #fef6e4; color: #001858; font-family: Helvetica, sans-serif;} .stButton>button {background-color: #f582ae; color: white; border-radius: 10px; padding: 8px 18px;} .stButton>button:hover {background-color: #f55c94;}</style>',
    unsafe_allow_html=True
)

st.title("Mi primera chamba")
st.header("la proxima semana no se como hice esto")
st.write("soy diseñadora, no programadora, no sé que pretenden")

st.subheader("Imagenes random antes del texto")
col_img1, col_img2 = st.columns(2)

with col_img1:
    fotito = Image.open('actually.jpg')
    st.image(fotito, caption='Sisoy')

with col_img2:
    st.image(fotito, caption='Otra vez yo')

texto = st.text_input('Holi', 'holix2')
st.write('El texto escrito es:', texto)

st.subheader("Ahora usemos 3 columnas")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Primera columna")
    st.write("pros de diseño interactivo:")
    resp = st.checkbox("dibujitos")
    if resp:
        st.write("Obvio")

with col2:
    st.subheader("Segunda columna")
    modo = st.radio("Razones por las que odiar la carrera", ("nochamba", "quesehaceahi", "jesus"))
    if modo == "nochamba":
        st.write("total, hay que salir de este hueco")
    if modo == "quesehaceahi":
        st.write("diseño grafico 2.0")
    if modo == "jesus":
        st.write("yo no le creo lo de rehabilitado")

with col3:
    st.subheader("Tercera columna")
    st.write("un espacio vacío... como mi agenda de clientes")

st.subheader("Uso de Botones")
if st.button("Presiona aqui"):
    st.write("que juicioso")
else:
    st.write("porfavor :(")

if st.button("Segundo botoncito"):
    st.write("gracias por insistir")

if st.button("Tercer botoncito"):
    st.write("ya estuvo bueno")

st.subheader("selectbox")
in_mod = st.selectbox(
    "Helado fav",
    ("Chocolate", "Vainilla", "Fresa"),
)
