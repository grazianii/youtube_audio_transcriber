from search import search_videos
from downloader import download_audio
from transcriber import transcribe

# Define pesquisas de vídeos no YouTube
QUERIES = [
    "como melhorar linkedin TI",
    "linkedin desenvolvedor",
    "linkedin engenheiro de dados",
    "linkedin para vagas de TI",
    "currículo TI",
    "currículo desenvolvedor",
    "currículo engenharia de dados",
    "currículo para tecnologia",
    "perfil linkedin tecnologia",
    "perfil linkedin desenvolvedor",
    "recrutador TI linkedin",
    "ATS currículo TI"
]

# Cria lista de vídeos
videos = []

# Busca vídeos e adiciona à lista
for query in QUERIES:
    videos.extend(
        search_videos(
        query = query,
        max_results=5
        )
    )

# Baixa, transcreve e salva vídeos
for video in videos:
    print("-" * 30)
    print(video["title"])
    #print(video["url"])
    audio = download_audio(video["url"])
    transcript = transcribe(audio)
    print(f"Transcrição salva em: {transcript}")