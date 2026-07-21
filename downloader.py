from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from datetime import datetime
import os

# Salva erros de download em um arquivo de log diário
def log_download_error(video_url, error):

    os.makedirs("logs", exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(
        "logs",
        f"download_errors_{today}.log"
    )

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"URL: {video_url}\n")
        f.write(f"Erro: {error}\n\n")


def download_audio(video_url):

    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": "audios/%(title)s.%(ext)s",
        "windowsfilenames": True,
        "retries": 2,
        "fragment_retries": 2,
        "skip_unavailable_fragments": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                video_url,
                download=True
            )
            return ydl.prepare_filename(info)

    except DownloadError as e:
        log_download_error(video_url, e)
        return None