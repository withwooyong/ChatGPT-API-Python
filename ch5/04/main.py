from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()
    
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 전체 실행 시간 측정 시작
start_time = time.time()

print("🎵 음성 파일을 전사하는 중...")
transcription_start = time.time()

file = open("sample.wav", "rb")
transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=file,
)

transcription_time = time.time() - transcription_start
print(f"✅ 전사 완료! (소요시간: {transcription_time:.2f}초)")

# 챗GPT로 요약하기
print("📝 요약을 생성하는 중...")
summary_start = time.time()

summary = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": f"다음 문장을 3줄의 글머리 기호로 요약해 주세요:\n{transcript}"
        }
    ]
)

summary_time = time.time() - summary_start
print(f"✅ 요약 완료! (소요시간: {summary_time:.2f}초)")

# 전체 실행 시간 계산
total_time = time.time() - start_time

print("\n" + "="*50)
print("📋 결과:")
print("="*50)
print(summary.choices[0].message.content)
print(f"\n📊 사용한 토큰 수: {summary.usage.total_tokens}")
print(f"⏱️  전체 실행 시간: {total_time:.2f}초")
print(f"   - 전사 시간: {transcription_time:.2f}초")
print(f"   - 요약 시간: {summary_time:.2f}초")
