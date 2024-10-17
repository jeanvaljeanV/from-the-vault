import requests

def pegar_previsao_do_tempo():
    # Definindo a chave da API e a URL base da API do OpenWeatherMap
    api_key = 'd66c4b5713de7ec212ee16574401d224'  # Coloque sua chave aqui
    cidade = 'São Paulo'
    url_base = f"http://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={api_key}&lang=pt&units=metric"

    # Fazendo a requisição para a API
    resposta = requests.get(url_base)
    
    # Verificando se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()
        
        # Extraindo informações da previsão do tempo
        print(f"Previsão do tempo para {cidade}:")
        for previsao in dados['list'][:7]:  # Pegar as 7 primeiras previsões (que são de 3 em 3 horas)
            data_hora = previsao['dt_txt']
            temperatura = previsao['main']['temp']
            descricao_clima = previsao['weather'][0]['description']
            print(f"{data_hora}: {temperatura}°C, {descricao_clima}")
    else:
        print("Erro ao buscar os dados da API")

pegar_previsao_do_tempo()
