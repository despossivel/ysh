from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Termo de pesquisa
query = "Python programming"

# Número de resultados que você deseja obter
num_results = 10

# Faz a pesquisa e itera pelos resultados
for result in search(query, num_results=num_results):
    try:
        response = requests.get(result)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else 'N/A'
            content = soup.get_text()
            content = ' '.join(content.split())  # Remove espaços em branco extras

            print("URL:", result)
            print("Título:", title)
            print("Parte do Conteúdo:", content[:200])  # Exibe os primeiros 200 caracteres do conteúdo
            print("\n")
    except Exception as e:
        print(f"Erro ao acessar {result}: {str(e)}")
