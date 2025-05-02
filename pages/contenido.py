import streamlit as st

import streamlit as st
from PIL import Image

st.title("Mi primera chamba")
st.header("la proxima semana no se como hice esto")
st.write("soy diseñadora, no programadora, no sé que pretenden")
fotito=Image.open('actually.jpg')
st.image(fotito, caption= 'Sisoy')


texto=st.text_input('Holi', 'holix2')
st.write('El texto escrito es:', texto)

st.subheader ("Ahora usemos 2 columnas")

col1,col2= st.columns(2)

with col1:
  st.subheader("Primera columna")
  st.write("pros de diseño interactivo:")
  resp= st.checkbox ("dibujitos")
  if resp:
    st.write("Obvio")

with col2:
  st.subheader("Segunda columna")
  modo= st.radio ("Razones por las que odiar la carrera",("nochamba", "quesehaceahi", "jesus"))
  if modo== "nochamba":
    st.write("total, hay que salir de este hueco")

  if modo== "quesehaceahi":
    st.write("diseño grafico 2.0")

  if modo== "jesus":
    st.write("yo no le creo lo de rehabilitado")

#Botoncito


st.subheader("Uso de Botones")
if st. button ("Presiona aqui"):
  st.write("que juicioso")
else:
  st.write("porfavor :(")

st.subheader("selectbox")
in_mod=st.selectbox(
  "Helado fav",
  ("Chocolate","Vainilla","Fresa"),
)
