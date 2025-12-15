import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt
st.header("Introduzindo os Elementos do Streamlit")

menu = option_menu(menu_title="Menu",
                 options=["Início", "Gráficos Estáticos", "Gráficos Dinâmicos", "Widgets", "Formulário"],
                 icons=["house", "bar-chart", "bar-chart-line", "toggles", "bar-chart"],
                 menu_icon="cast",
                 default_index=0,
                 orientation="horizontal")
                 
