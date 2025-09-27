from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import json

# 환경 변수 로드
load_dotenv()

def check_moderation(text, client):
    """텍스트의 적절성을 검사하는 함수"""
    try:
        response = client.moderations.create(input=text)
        return response
    except Exception as e:
        print(f"❌ 모더레이션 API 호출 중 오류 발생: {str(e)}")
        return None

def format_moderation_result(response):
    """모더레이션 결과를 보기 좋게 포맷팅하는 함수"""
    if not response:
        return "❌ 모더레이션 검사 실패"
    
    result = response.results[0]
    
    # 기본 정보
    flagged = result.flagged
    categories = result.categories
    category_scores = result.category_scores
    
    # 결과 출력
    print("\n" + "=" * 60)
    print("🔍 모더레이션 검사 결과")
    print("=" * 60)
    
    # 전체 플래그 상태
    status = "🚫 부적절한 내용 감지됨" if flagged else "✅ 적절한 내용"
    print(f"📊 전체 상태: {status}")
    
    # 카테고리별 상세 정보
    print(f"\n📋 카테고리별 분석:")
    print("-" * 40)
    
    for category, is_flagged in categories.model_dump().items():
        score = getattr(category_scores, category)
        status_icon = "🚫" if is_flagged else "✅"
        print(f"{status_icon} {category}: {is_flagged} (점수: {score:.4f})")
    
    # JSON 형태로도 출력
    print(f"\n📄 JSON 형태 결과:")
    print("-" * 40)
    print(response.model_dump_json(indent=2))
    
    return flagged

def main():
    # 전체 실행 시간 측정 시작
    total_start_time = time.time()
    
    print("🚀 OpenAI 모더레이션 API 테스트 프로그램을 시작합니다...")
    print("=" * 70)
    
    # API 키 확인
    print("🔑 API 키를 확인하는 중...")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai_api_key:
        print("❌ OPENAI_API_KEY가 설정되지 않았습니다.")
        print("   .env 파일에 OPENAI_API_KEY를 설정해주세요.")
        return
    
    print("✅ OpenAI API 키 확인 완료")
    
    # OpenAI 클라이언트 초기화
    print("🤖 OpenAI 클라이언트를 초기화하는 중...")
    client_start_time = time.time()
    try:
        client = OpenAI(api_key=openai_api_key)
        client_time = time.time() - client_start_time
        print(f"✅ OpenAI 클라이언트 초기화 완료 (소요시간: {client_time:.2f}초)")
    except Exception as e:
        print(f"❌ OpenAI 클라이언트 초기화 중 오류 발생: {str(e)}")
        return
    
    # 테스트 루프
    print("\n" + "=" * 70)
    print("💬 모더레이션 테스트를 시작합니다!")
    print("   텍스트를 입력하거나 'quit'을 입력하여 종료하세요.")
    print("=" * 70)
    
    test_count = 0
    flagged_count = 0
    
    while True:
        try:
            # 사용자 입력 받기
            print(f"\n📝 테스트 #{test_count + 1}:")
            text = input("   검사할 텍스트를 입력하세요: ").strip()
            
            if text.lower() in ['quit', 'exit', '종료', 'q']:
                print("👋 모더레이션 테스트를 종료합니다.")
                break
            
            if not text:
                print("⚠️  텍스트를 입력해주세요.")
                continue
            
            print(f"🔍 입력된 텍스트: {text}")
            print("🤖 모더레이션 검사를 실행하는 중...")
            
            # 모더레이션 검사 실행
            moderation_start_time = time.time()
            response = check_moderation(text, client)
            moderation_time = time.time() - moderation_start_time
            
            if response:
                is_flagged = format_moderation_result(response)
                if is_flagged:
                    flagged_count += 1
                
                print(f"\n⏱️  검사 소요시간: {moderation_time:.2f}초")
            
            test_count += 1
            
        except KeyboardInterrupt:
            print("\n\n👋 사용자가 프로그램을 종료했습니다.")
            break
        except Exception as e:
            print(f"\n❌ 테스트 중 오류 발생: {str(e)}")
            print("   다시 시도해주세요.")
    
    # 전체 실행 시간 계산
    total_time = time.time() - total_start_time
    
    print(f"\n📊 테스트 실행 요약:")
    print("=" * 70)
    print(f"🤖 클라이언트 초기화: {client_time:.2f}초")
    print(f"🧪 총 테스트 수: {test_count}개")
    print(f"🚫 부적절한 내용 감지: {flagged_count}개")
    print(f"✅ 적절한 내용: {test_count - flagged_count}개")
    print(f"⏱️  총 실행 시간: {total_time:.2f}초")
    print("=" * 70)
    print("🎉 모더레이션 테스트가 완료되었습니다!")

if __name__ == "__main__":
    main()