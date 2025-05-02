import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.infomoney.com.br/cotacoes/ibovespa/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Parsear o HTML
soup = BeautifulSoup(response.text, 'lxml')

# Encontrar a tabela de cotações (essa parte pode mudar se o site mudar o layout)
table = soup.find('table')

# Carregar a tabela em um DataFrame do Pandas
df = pd.read_html(str(table))[0]

print(df)
