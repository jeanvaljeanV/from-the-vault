
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime

#autenticação com as credencias do spotify developer

client_id = 'd84c2961d740432d94a46115275381e1'
client_secret = '2e00d6674a184d9b9eb135ae8eec1ac3'

#configuração de autenticação
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

#buscar lançamentos sexta-feira (dia comum de lançamentos de novas musicas)
def get_friday_releases():
    today = datetime.datetime.today()

#lançamentos da ultima sexta feira
    last_friday = today - datetime.timedelta(days=(today.weekday() + 3) % 7)
    date_str = last_friday.strftime('%y-%m-%d')

#busca lançamentos recentes
    new_releases = sp.new_releases(limit=20, country='EUA')

    print(f"lançamentos de {date_str}:")
    for album in new_releases['albums']['items']:
        print(f"{album['name']} - {album['artists'][0]['name']}")

#rodar função

get_friday_releases()    

