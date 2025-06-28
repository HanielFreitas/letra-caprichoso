import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Carrega variáveis do .env
load_dotenv()

# Autenticação
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Busca o álbum
query = "É tempo de retomada boi caprichoso"
result = sp.search(q=query, type="album", limit=1)
if not result['albums']['items']:
    print("Álbum não encontrado.")
    exit()

album = result['albums']['items'][0]
album_id = album['id']
album_name = album['name']
release_date = album['release_date']

print(f"\n🎧 Álbum encontrado: {album_name} - Lançamento: {release_date}\n")

# Lista as faixas
tracks = sp.album_tracks(album_id)['items']

with open("faixas_caprichoso.txt", "w", encoding="utf-8") as f:
    print("🎵 Faixas:")
    for i, track in enumerate(tracks, 1):
        name = track['name']
        print(f"{i}. {name}")
        f.write(f"{i}. {name}\n")

print("\n✅ Faixas salvas no arquivo: faixas_caprichoso.txt")
