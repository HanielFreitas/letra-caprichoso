# Letras do Álbum "É Tempo de Retomada" - Boi Caprichoso 2025

Este projeto tem como objetivo coletar as letras das músicas do álbum oficial "É Tempo de Retomada" do Boi Caprichoso, realizado durante o Festival de Parintins 2025.

---

## 📀 Funcionalidades principais

1. **Busca as faixas do álbum no Spotify**  
   - Utiliza a API oficial do Spotify para encontrar o álbum "É Tempo de Retomada" e listar suas faixas.  
   - Salva as faixas num arquivo `faixas_caprichoso.txt` com numeração.

2. **Coleta automática das letras das músicas**  
   - Para cada faixa listada, o script realiza busca no site [letras.mus.br](https://www.letras.mus.br) para encontrar a página da letra.  
   - Caso a busca falhe, utiliza uma estratégia de fallback construindo a URL baseada no padrão do site.  
   - Raspagem (web scraping) da letra no HTML, extraindo o conteúdo textual da página.  
   - Salva as letras em arquivos `.txt` numerados na pasta `letras/`.

---

## 🚀 Como usar

### 1. Clonar o repositório e instalar dependências

```bash
git clone https://github.com/seuusuario/boi-caprichoso-letras.git
cd boi-caprichoso-letras
pip install -r requirements.txt
