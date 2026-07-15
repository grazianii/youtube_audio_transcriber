from faster_whisper import WhisperModel
import os

# Define parâmetros do WhisperModel
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def transcribe(audio_file):

    segments, info = model.transcribe(audio_file)
    text = ""
    for segment in segments:
        text += segment.text + "\n"

    filename = os.path.splitext(os.path.basename(audio_file))[0]

    output_file = os.path.join(
        "transcripts",
        f"{filename}.txt"
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    return output_file