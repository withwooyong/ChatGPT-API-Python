import openai
import os
openai.api_key = os.environ["OPENAI_API_KEY"]

file = open("sample.wav", "rb")

transcript = openai.Audio.transcribe(
    model="whisper-1",
    file=file,
    # 매개변수 추가
    response_format="srt"
)

print(transcript)