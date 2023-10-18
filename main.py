from googleapiclient.discovery import build

# Substitua 'YOUR_API_KEY' pelo seu próprio chave de API do Google
api_key = 'AIzaSyA_M84eCi4LmhPD5kURX2lBsBo0YCxjVI0'

# Crie um serviço da API do YouTube
youtube = build('youtube', 'v3', developerKey=api_key)

# Defina os parâmetros de pesquisa
# Defina as palavras-chave de pesquisa
keyword1 = 'Shorts'
keyword2 = 'Funny'  # Outra palavra-chave que você deseja adicionar

# Concatene as palavras-chave em uma única string
search_query = keyword1 + ' ' + keyword2

# Realize a pesquisa
search_response = youtube.search().list(
    q=search_query,
    type='video',
    part='snippet',  # Adicione esta linha para solicitar informações básicas dos vídeos
    maxResults=10  # Número máximo de resultados que você deseja
).execute()

# Analise os resultados
for search_result in search_response.get('items', []):
    video_id = search_result['id']['videoId']
    video_title = search_result['snippet']['title']
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    print(f'Título: {video_title}')
    print(f'URL: {video_url}')
    print('---')
