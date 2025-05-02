import streamlit as st
from PIL import Image

st.set_page_config(page_title="Solo soy una chica", page_icon="💖", layout="wide")

st.markdown(
    '<style>body {background-color: #fff0f5; color: #880e4f; font-family: "Comic Sans MS", cursive, sans-serif;} h1, h2, h3, h4, h5, h6 {color: #d81b60;} .stButton>button {background-color: #f8bbd0; color: #ffffff; border-radius: 12px; padding: 10px 20px;} .stButton>button:hover {background-color: #f48fb1;}</style>',
    unsafe_allow_html=True
)

st.title("💖 Solo soy una chica... con mil entregas 💖")
st.header("🌷 Sobreviviendo con glitter y ansiedad 🌷")

st.subheader("💌 Deja tu pink thought")
texto = st.text_input('Escribe aquí tu confesión existencial', 'holix2')
st.write('💬 Dijiste:', texto)

st.subheader("🍨 Elige tu vibe de hoy")
helado = st.selectbox("Tu helado emocional", ("Chocolate", "Vainilla", "Fresa"))
emoji = st.selectbox("Tu mood del día", ("🥲 llorando pero cute", "🤡 fingiendo que todo bien", "✨ girlboss en construcción", "😵‍💫 modo colapso"))

st.subheader("🎀 Botoncitos para fingir control 🎀")
if st.button("Necesito un break"):
    st.write("vete a ver reels un rato")

if st.button("Ya mandé el archivo"):
    st.write("aunque no era el final :)")

if st.button("No me hablen hoy"):
    st.write("ni modo, diva colapsando")

if st.button("Solo vine a clickear"):
    st.write("validada estás")

if st.button("Siguiente crisis por favor"):
    st.write("cambio de look incoming")

st.subheader("💅 Escoge tu versión girlboss del día")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("✨ Creativa en caos")
    st.write("pros de diseño interactivo:")
    resp = st.checkbox("dibujitos")
    if resp:
        st.write("Obvio")

with col2:
    st.subheader("💔 Crisis vocacional")
    modo = st.radio("Motivos para dudar de esta carrera", ("nochamba", "quesehaceahi", "jesus"))
    if modo == "nochamba":
        st.write("total, hay que salir de este hueco")
    if modo == "quesehaceahi":
        st.write("diseño grafico 2.0")
    if modo == "jesus":
        st.write("yo no le creo lo de rehabilitado")

with col3:
    st.subheader("🌸 Freelancer desaparecida")
    st.write("un espacio vacío... como mi agenda de clientes")

st.subheader("👛 Selfies mentales antes del colapso")
col_img1, col_img2 = st.columns(2)

with col_img1:
    fotito = Image.open('actually.jpg')
    st.image(fotito, caption='Sisoy')

with col_img2:
    st.image(fotito, caption='Otra vez yo')
