import streamlit as st
import pandas as pd
import yfinance as yf
import datetime

st.set_page_config(
        page_title="ANALISE AÇÕES - YFINANCE",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )
st.sidebar.image("imagem/logo.svg")
st.sidebar.write(" # Análise de Ações com Yfinance ")


col1, col2 = st.columns(2)

# Defina o dicionário de tickers fora do escopo do bloco
tickers = {
    'ITAÚ - (ITUB4)': 'ITUB4.SA',
    'PETROBRÁS - (PETR4)': 'PETR4.SA',
    'BRADESCO - (BBDC4)': 'BBDC4.SA',
    'MAGALU - (MGLU3)': 'MGLU3.SA',
    'AMBEV - (ABEV3)': 'ABEV3.SA',
    'VALE - (VALE3)': 'VALE3.SA',
    'GERDAU - (GGBR4)': 'GGBR4.SA',
    'VIA VAREJO - (VVAR3)': 'VVAR3.SA',
    'BANCO DO BRASIL - (BBAS3)': 'BBAS3.SA',
    'SANTANDER BRASIL - (SANB11)': 'SANB11.SA',
    'BANRISUL - (BRSR6)': 'BRSR6.SA',
    'BANCO ABC BRASIL - (ABCB4)': 'ABCB4.SA',
    'BANESTES - (BEES3 e BEES4)': 'BEES3.SA',
    'BANPARÁ - (BPAR3)': 'BPAR3.SA',
    'BTG PACTUAL - (BPAC11)': 'BPAC11.SA'
}



ticker = st.sidebar.selectbox(
    'Selecione o Ticker desejado',
    list(tickers.keys()))

ticker_selecionado = tickers[ticker]

    
with col1:
    data_inicio = st.sidebar.date_input("Selecione a Data de Início",datetime.date(2023, 1, 1), key="data_inicio")
    dt_inicio = pd.to_datetime(data_inicio).strftime('%Y-%m-%d')
    
with col2:
    data_fim = st.sidebar.date_input("Selecione a Data de Fim", key="data_fim")
    dt_final = pd.to_datetime(data_fim).strftime('%Y-%m-%d')
    
informacao_ticker = yf.Ticker(ticker_selecionado)
historico_ticker = informacao_ticker.history(period='1d', start=dt_inicio, end=dt_final)

st.write(" # :bar_chart: Análise de Ações com Yfinance ")

st.divider()
st.write('### Informações da Empresa')
col1, col2, col3 = st.columns(3)
col1.markdown(f"**Empresa:** {informacao_ticker.info['longName']}")
col2.markdown(f"**Mercado :** {informacao_ticker.info['industryDisp']}")
col3.markdown(f"**Preço Atual :** {informacao_ticker.info['currentPrice']} BRL")

st.divider()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.write('### Grafico de Preço de Fechamento ')
st.warning(f'Periodo :({dt_inicio} - {dt_final})')
st.line_chart(historico_ticker['Close'], use_container_width=True)
   
st.write('### Gráfico de Variação Percentual Diário')
st.warning(f'Periodo :({dt_inicio} - {dt_final})')
historico_ticker['Variação Diária (%)'] = historico_ticker['Close'].pct_change() * 100
st.area_chart(historico_ticker['Variação Diária (%)'], use_container_width=True)

st.caption('Os dados foram obtidos a partir do site : https://pypi.org/project/yfinance/')