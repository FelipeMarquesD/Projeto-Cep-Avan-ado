import streamlit as st
from ferramentas import buscar_cep
import pandas as pd

st.sidebar.image("logo.jpeg")
st.sidebar.title("CEP Aladin")
cep = st.sidebar.text_input("Digite o CEP que deseja consultar: ")

if st.sidebar.button("Consultar"):
    dados = buscar_cep(cep)
    lat = float(dados.get("lat")) #Pega a lat de dados
    lng = float(dados.get("lng")) #Pega a lng de dados

    coordenadas = pd.DataFrame({"latitude":[lat], "longitude":[lng]})

    st.title(f"{dados.get["city"]}, {dados.get("state")}")
    st.map(coordenadas, zoom=15, color="#6DB8FF")

    st.json(dados)

