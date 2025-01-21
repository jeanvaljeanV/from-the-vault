#Código em Python

import yfinance as yf
import numpy as np

# Baixar dados do ativo e do índice de referência
ticker = "PETR4.SA"  # Substituir pelo ticker da empresa
indice = "^BVSP"  # Ibovespa como índice de referência

ativo = yf.download(ticker, start="2020-01-01", end="2024-12-01")['Adj Close']
indice_ref = yf.download(indice, start="2020-01-01", end="2024-12-01")['Adj Close']

# Calcular retornos diários
retorno_ativo = ativo.pct_change().dropna()
retorno_indice = indice_ref.pct_change().dropna()

# Regressão para encontrar o beta
cov_matrix = np.cov(retorno_ativo, retorno_indice)
beta = cov_matrix[0, 1] / cov_matrix[1, 1]

print(f"O beta do ativo {ticker} em relação ao índice {indice} é {beta:.2f}")

#Otimização da Carteira

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt.expected_returns import mean_historical_return

# Dados de exemplo: preços históricos de ações
tickers = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]  # Substituir pelos ativos escolhidos
dados = yf.download(tickers, start="2020-01-01", end="2024-12-01")['Adj Close']

# Calcular retornos esperados e matriz de covariância
retornos_esperados = mean_historical_return(dados)
matriz_covariancia = CovarianceShrinkage(dados).ledoit_wolf()

# Otimização para máxima relação Sharpe
ef = EfficientFrontier(retornos_esperados, matriz_covariancia)
pesos = ef.max_sharpe()
ef.clean_weights()

print("Pesos otimizados para máxima relação Sharpe:")
print(pesos)

#Visualização dos Pesos

import matplotlib.pyplot as plt

# Visualizar a alocação dos ativos
labels = list(pesos.keys())
sizes = list(pesos.values())

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Alocação da Carteira - Máxima Relação Sharpe')
plt.show()
