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

videos = []

for query in QUERIES:
    videos.extend(
        search_videos(
            query=query,
            max_results=3
        )
    )

for video in videos:
    print("-" * 30)
    print(video["title"])

    audio = download_audio(video["url"])

    if audio is None:
        continue

    transcript = transcribe(audio)
    print(f"Transcrição salva em: {transcript}")

print("\nTranscrição concluída com sucesso!")