import streamlit as st
st.set_page_config(page_title="Mi primera chamba", page_icon="🎨", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: #fff8f0;
        color: #3b2f2f;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .stButton>button {
        background-color: #ffb6b9;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff999c;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Mi primera chamba")
st.header("la proxima semana no se como hice esto")
st.write("soy diseñadora, no programadora, no sé que pretenden")

st.subheader("Imagenes random antes del texto (cambio de orden)")
col_img1, col_img2 = st.columns(2)

with col_img1:
    fotito = Image.open('actually.jpg')
    st.image(fotito, caption='Sisoy')

with col_img2:
    st.image(fotito, caption='Otra vez yo')

texto = st.text_input('Holi', 'holix2')
st.write('El texto escrito es:', texto)

st.subheader("Ahora usemos 3 columnas (antes eran 2)")

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
