import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
st.header("Introduzindo os Elementos do Streamlit")

menu = option_menu(menu_title="Menu",
                 options=["Início", "Gráficos Estáticos", "Gráficos Dinâmicos", "Widgets", "Formulário"],
                 icons=["house", "bar-chart", "menu-button", "toggles", "grid"],
                 menu_icon="cast",
                 default_index=0,
                 orientation="vertical")
with st. sidebar:
  st.success("**UPLOUD DE DADOS**")
  dados = st.file_uploader("Carregue ...",
          type=["xlsl","xls"])
  if dados:
    def carregar_dados(dados):
      try:
        df = pd. read_excel (dados)
        return df
      except FileNotFoundError:
        return pd.DataFrame()
    df = carregar_dados(dados)
    st.table(df)
  else:
    st.info("🎰 Carregue um ficheiro Excel para começar")

if menu == "Início":
    with st.expander("**Sobre o Instituto Nacional de Estatística**"):
        st.write("Acesse o site www.ine.cv")
        st.image("Ine.jpg")

    
                 
