import requests
from bs4 import BeautifulSoup
import os
import time
from unidecode import unidecode
import re

# Ler faixas
with open("faixas_caprichoso.txt", "r", encoding="utf-8") as f:
    musicas = [l.strip().split(". ",1)[1] for l in f]

os.makedirs("letras", exist_ok=True)

def slugify(text):
    t = unidecode(text.lower())
    t = re.sub(r'[^a-z0-9 ]', '', t)
    return "-".join(t.split())

def buscar_letra(musica):
    q = f"{musica} Boi Caprichoso"
    busca = f"https://www.letras.mus.br/pesquisa?q={requests.utils.quote(q)}"
    resp = requests.get(busca)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        for a in soup.select("ul.art_music-list li a"):
            nome = a.get_text(strip=True)
            href = a['href']
            if "caprichoso" in href and musica.split()[0].lower() in unidecode(nome.lower()):
                return "https://www.letras.mus.br" + href

    # fallback se não encontrar
    slug = slugify(musica)
    path = f"caprichoso-boi-bumba/{slug}/"
    fallback_url = "https://www.letras.mus.br/" + path
    resp2 = requests.get(fallback_url)
    if resp2.status_code == 200:
        return fallback_url

    return None

for m in musicas:
    print(f"🔍 Buscando: {m}")
    url = buscar_letra(m)
    if not url:
        print(f"❌ Não encontrou nem com fallback: {m}")
        continue

    print(f"👉 Achou URL: {url}")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    
    letra_div = soup.find("div", class_="lyric-original")
    if not letra_div:
        print(f"⚠️ Letra não encontrada no HTML: {m}")
        continue

    letra = letra_div.get_text(separator="\n").strip()
    index = musicas.index(m) + 1
    numero = f"{index:02d}"
    fn = f"letras/{numero} - {m}.txt"

    with open(fn, "w", encoding="utf-8") as f:
        f.write(m + "\n\n" + letra)

    print(f"✅ Letra salva: {fn}")
    time.sleep(1)
