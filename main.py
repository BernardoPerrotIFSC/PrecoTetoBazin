import yfinance as yf
from datetime import datetime, timedelta

ativo = yf.Ticker("VALE3.SA")

dividend_info = ativo.dividends

data_atual = datetime.now()

data_um_ano_atras = data_atual - timedelta(days=365)

data_um_ano_atras_formatada = data_um_ano_atras.strftime("%Y-%m-%d")

filtered_dividends = dividend_info[dividend_info.index >= data_um_ano_atras_formatada]
total = 0
count = -1
for i in filtered_dividends:
    dividend = dividend_info.iloc[count]
    data = dividend_info.index[count]
    print(data)
    print(f'R$ {dividend}')
    total = total + dividend
    count = count -1
preco_teto = total*16.6
print(f'R$ {total}')
print(f'Preco teto: R$ {preco_teto}')
preco = round(ativo.history(period='1d')['Close'][0], 2)
print(f'Preco atual: R$ {preco}')
print(data_um_ano_atras_formatada)