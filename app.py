import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import time
import re
from datetime import date

st.header("Introduzindo os Elementos do Streamlit")

menu = option_menu(
    menu_title="Menu",
    options=["Início", "Gráficos Estáticos", "Gráficos Dinâmicos", "Widgets", "Formulário"],
    icons=["house", "bar-chart", "menu-button", "toggles", "grid"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical"
)

with st.sidebar:
    st.success("**UPLOAD DE DADOS**")
    dados = st.file_uploader(
        "Carregue um arquivo Excel",
        type=["xlsx"]
    )

    if dados is not None:
        try:
            df = pd.read_excel(dados, engine="openpyxl")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Erro ao ler o arquivo: {e}")
    else:
        st.info("🎰 Carregue um ficheiro Excel para começar")

if menu == "Início":
    with st.expander("**Sobre o Instituto Nacional de Estatística**"):
        st.markdown("[Acesse o site do INE](https://www.ine.cv)")
        st.image("Ine.jpg")

if menu == "Widgets":
    bt = st.button("Dê um Clique!")

    if bt:
        sd = st.slider(
            "Mova o ponto do Slider!",
            min_value=25,
            max_value=35,
            value=30,
            step=1
        )

        texto = f"Eu tenho {sd} anos!"
        st.success(texto)




if menu == "Gráficos Estáticos":
    col1, col3 = st.columns([0.45, 0.45])  # duas colunas iguais, ajuste as proporções
    with col1:
        st.subheader("Coluna 1")
        dados_hist = [3,9,5,12,6,7,5,10,6,10]
        fig, ax = plt.subplots()
        ax.hist(dados_hist, bins=5, color="skyblue", edgecolor="black")
        ax.set_title("Histograma")
        st.pyplot(fig)

    with col3:
        st.subheader("Coluna 2")
        lab = ["Python", "Java", "C++", "JavaScript"]
        pop = [45, 25, 15, 15]
        fig, ax = plt.subplots()
        ax.pie(pop, labels=lab, autopct="%1.1f%%", startangle=90)
        ax.set_title("Gráfico Circular")
        ax.axis("equal")
        st.pyplot(fig)
        

  


    
                 
