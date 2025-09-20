import pandas as pd
import streamlit as st
import plotly.express as px

#config da pagina

st.set_page_config(
    page_title="Dashboard da Zara",
    layout="wide"
)

st.title('Dashboard de Análise de roupas')

st.markdown('**Explore** os dados de produtos da Zara')

@st.cache_data

def load_data():
    df = pd.read_csv('zara.csv', sep =';')
    return df

df = load_data()

section = st.sidebar.multiselect(
    "Selecione a seção: ",
    options = df['section'].unique(),
    default = df['section'].unique()
)

promotion = st.sidebar.multiselect(
    "Selecione se quer itens promocionais: ",
    options = df['Promotion'].unique(),
    default = df['Promotion'].unique()
)

df_filtered = df[
    df['section'].isin(section) &
    df['Promotion'].isin(promotion)
    ]

st.subheader('Principais métricas')

col1, col2, col3 = st.columns(3)
tamanho = len(df_filtered)
col1.metric('Total de produtos', tamanho)
soma = sum(df_filtered['price'])
col2.metric('Soma de valores', round(soma,2))
try:
    col3.metric('Média de valor', round((soma/tamanho), 2))
except:
    col3.metric('Média de valor', 0)

price_distribution = px.histogram(
    df_filtered,
    x='price',
    nbins=50,
    title='Distribuição de preços',
    template='plotly_white'
)


st.plotly_chart(price_distribution)
st.dataframe(df_filtered)
