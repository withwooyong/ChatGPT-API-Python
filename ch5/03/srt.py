from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

file = open("sample.wav", "rb")
transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=file,
    # 매개변수 추가
    response_format="srt"
)

print(transcript)