import yfinance as yf
from datetime import datetime, timedelta

acao = str(input("Digite o Ticker da empresa: "))
acao.upper()

ativo = yf.Ticker(acao+".SA")
dolar = yf.Ticker("USDBRL=X")
dividend_info = ativo.dividends

data_atual = datetime.now()

data_um_ano_atras = data_atual - timedelta(days=365)

data_um_ano_atras_formatada = data_um_ano_atras.strftime("%Y-%m-%d")

filtered_dividends = dividend_info[dividend_info.index >= data_um_ano_atras_formatada]

dividend_dolar_total = 0
count = -1

cotacao_ativo = round(ativo.history(period='1d')['Close'].iloc[0], 2)
cotacao_dolar = round(dolar.history(period='1d')['Close'].iloc[0], 3)

for i in filtered_dividends:
    dividend_real = round(dividend_info.iloc[count], 4)
    data = dividend_info.index[count]
    data_organizada = data.strftime("%d/%m/%Y")
    cotacao_data_dividendo = round(dolar.history(start=data, end=data)["Close"].iloc[0], 4)
    dividend_dolar = round(dividend_real/cotacao_data_dividendo, 4)
    dividend_dolar_total = round(dividend_dolar_total+dividend_dolar, 4)
    print(f'Cotação dolar na data do dividendo: ${cotacao_data_dividendo}')
    print(f'Dividendo em dolar: $ {dividend_dolar}')
    print(f'Dividendo em reais: R$ {dividend_real}')
    print(f'Data do dividendo: {data_organizada}')
    print("----------------------------------------")
    count = count-1
preco_teto_dolar = round((dividend_dolar_total*cotacao_dolar)*16.667, 2)

print(f'Total dividendos em dolar: $ {dividend_dolar_total}')
print(f'Preço teto em dolar: R$ {preco_teto_dolar}')