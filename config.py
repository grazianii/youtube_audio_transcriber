from dotenv import load_dotenv
import os

load_dotenv()

# Define chave de API do YouTube obtida através do Google Cloud
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")