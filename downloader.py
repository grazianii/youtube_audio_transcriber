from yt_dlp import YoutubeDL


def download_audio(video_url):

    # Define parâmetros ao baixar vídeos
    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": "audios/%(title)s.%(ext)s",
        "windowsfilenames": True,
    }

    # Baixa áudio de vídeos
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(
            video_url,
            download=True
        )
        return ydl.prepare_filename(info)