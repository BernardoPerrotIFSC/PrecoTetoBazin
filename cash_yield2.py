import yfinance as yf
from datetime import datetime, timedelta

acao = str(input("Digite o Ticker da empresa: "))
acao = acao.upper()

ativo = yf.Ticker(acao+".SA")
# acao = "CAML3"
# ativo= yf.Ticker("CAML3.SA")
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

print('------------------')
print(f'| Ticker: {acao} |')
print('------------------')

for i in filtered_dividends:
    dividend_real = round(dividend_info.iloc[count], 4)
    data = dividend_info.index[count]
    data_organizada = data.strftime("%d/%m/%Y")
    cotacao_data_dividendo = round(dolar.history(start=data, end=data)["Close"].iloc[0], 4)
    dividend_dolar = round(dividend_real/cotacao_data_dividendo, 4)
    dividend_dolar_total = round(dividend_dolar_total+dividend_dolar, 4)
    print(f'Cotação dolar na data do dividendo: ${cotacao_data_dividendo}')
    print(f'Dividendo em REAIS: R$ {dividend_real}')
    print(f'Dividendo em DOLAR: $ {dividend_dolar}')
    print(f'Data do dividendo: {data_organizada}')
    print("----------------------------------------")
    count = count-1
#MARGEM DE SEGURANÇA
preco_teto_dolar = round((dividend_dolar_total*16.667)*cotacao_dolar, 2)

print(f'Total dividendos em DOLAR: $ {dividend_dolar_total}')
print(f'Preço teto em DOLAR: R$ {preco_teto_dolar}')
