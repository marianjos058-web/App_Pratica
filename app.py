import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

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

if menu == "Widgets"



    
                 
