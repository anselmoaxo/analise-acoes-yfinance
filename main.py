import streamlit as st
import pandas as pd
import yfinance as yf


st.set_page_config(
        page_title="ANALISE AÇÕES - YFINANCE",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )
st.sidebar.write(" # Análise de Ações com Yfinance! ")


col1, col2 = st.columns(2)

# Defina o dicionário de tickers fora do escopo do bloco
tickers = {
    'ITAÚ - (ITUB4)': 'ITUB4.SA',
    'PETROBRÁS -(PETR4)': 'PETR4.SA',
    'BRADESCO - (BBDC4)': 'BBDC4.SA',
    'MAGALU - (MGLU3) ': 'MGLU3.SA',
    'IBOVESPA - (^BVSP)': '^BVSP',
    'AMBEV - (ABEV3)': 'ABEV3.SA',
    'VALE-(VALE3)': 'VALE3.SA',
    'GERDAU - (GGBR4)': 'GGBR4.SA'
}


ticker = st.sidebar.selectbox(
    'Selecione o Ticker desejado',
    list(tickers.keys()))

ticker_selecionado = tickers[ticker]
    
with col1:
    data_inicio = st.sidebar.date_input("Selecione a Data de Início", key="data_inicio")
    dt_inicio = pd.to_datetime(data_inicio).strftime('%Y-%m-%d')
    
with col2:
    data_fim = st.sidebar.date_input("Selecione a Data de Fim", key="data_fim")
    dt_final = pd.to_datetime(data_fim).strftime('%Y-%m-%d')
    
informacao_ticker = yf.Ticker(ticker_selecionado).info
st.write(f" # Informações do Ticker : {ticker} ")

st.divider()

col1,col2,col3,col4 = st.columns(4)

col1.markdown(f"**Industria:** {informacao_ticker['industry']}")
col1.markdown(f"**Setor :** {informacao_ticker['sector']}")
market_cap_formatted = "{:,}".format(informacao_ticker['marketCap'])
col1.markdown(f"**Valor do Mercado :** {market_cap_formatted}")

st.divider()

historico_ticker = yf.download(ticker_selecionado, start=dt_inicio, end=dt_final )

st.write('Grafico de Preço de Fechamento')
st.line_chart(historico_ticker['Close'], use_container_width=True)
    
st.write('Gráfico de Volume')
st.line_chart(historico_ticker['Volume'], use_container_width=True)
    
st.write('Gráfico de Variação Percentual Diário')
historico_ticker['Variação Diária (%)'] = historico_ticker['Close'].pct_change() * 100
st.line_chart(historico_ticker['Variação Diária (%)'], use_container_width=True)

st.caption('Os dados foram obtidos a partir do site : https://pypi.org/project/yfinance/')