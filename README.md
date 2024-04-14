# 《OpenAI API와 파이썬으로 나만의 챗GPT 만들기》 실습 예제

원서 제목: ChatGPT API×Pythonで始める対話型AI実装入門（GPT-3.5&GPT-4 対応）

# ▣ 01장: 챗GPT의 기본을 배우자

## 1 챗GPT란?
###  1-1 사람처럼 대화할 수 있는 챗GPT
### 1-2 챗GPT를 뒷받침하는 기술
  
  1-3 챗GPT는 다양한 용도로 활용할 수 있다
  
  1-4 챗GPT 이용 시 주의점
  
  1-5 챗GPT는 브라우저와 API로 이용할 수 있다
  
  1-6 GPT-3.5와 GPT-4의 차이점은?
  
  1-7 ChatGPT Plus 유료 버전의 특징

##2 챗GPT API 개요 알아보기
###__2-1 챗GPT API란?
###__2-2 GPT-3.5와 GPT-4는 어떻게 사용할까?

##3 챗GPT의 핵심 키워드를 이해하자!
###__3-1 프롬프트는 ‘AI에 대한 지시문’
###__3-2 토큰이란 ‘문자열을 나누는 단위’
###__3-3 매개변수란 ‘작동을 제어하기 위한 설정값’

##4 챗GPT API 요금 체계
###__4-1 챗GPT API의 요금 체계
###__4-2 API 이용 요금 계산 방법
###__4-3 Tokenizer로 토큰 수를 확인하자
###__4-4 한국어는 영어보다 토큰 수가 더 많다

##5 API로 확장되는 챗GPT의 가능성
###__5-1 챗GPT API로 할 수 있는 일 알아보기
###__5-2 답변의 내용과 스타일을 세밀하게 조정할 수 있다
###__5-3 정보를 학습할 수 있다
###__5-4 기능 확장 가능

##6 좋은 답변을 얻기 위한 프롬프트 작성 가이드
###__6-1 프롬프트로 챗GPT 답변의 질을 높인다
###__6-2 역할 전달
###__6-3 맥락 전달
###__6-4 목적 전달
###__6-5 출력 형식 전달
###__6-6 적절한 문체 선택
 
▣ 02장: 개발 환경과 API를 준비하자
1 챗GPT API 키 받기
__1-1 챗GPT API를 사용하려면?
__1-2 OpenAI 계정을 만들자
__1-3 API 키를 얻자
__1-4 API 키 취급에 주의
2 파이썬을 사용할 준비를 하자
__2-1 왜 파이썬을 사용해야 하는가?
__2-2 파이썬 버전에 대해서
__2-3 파이썬을 설치하자 (윈도우의 경우)
__2-4 파이썬을 설치하자 (macOS의 경우)
3 코드 편집기를 준비하자
__3-1 비주얼 스튜디오 코드(VS Code)란?
__3-2 VS Code를 설치하자
__3-3 파이썬 코드를 작성해 보자
__3-4 파이썬 코드를 실행해 보자
4 파이썬에서 챗GPT API를 사용하는 방법
__4-1 파이썬에서 챗GPT API를 사용하기 위해 필요한 것들
__4-2 OpenAI의 라이브러리를 사용해 보자
__4-3 환경 변수란?
__4-4 API 키를 환경 변수로 설정하기 (윈도우의 경우)
__4-5 API 키를 환경 변수로 설정하자 (macOS의 경우)
__4-6 API를 사용해 챗GPT에 질문해 보기
5 챗GPT API의 기본 사용법
__5-1 요청과 응답
__5-2 챗GPT API의 요청과 응답
__5-3 챗GPT API의 매개변수를 이해하자
 
▣ 03장: 단문 작성과 SNS 포스팅을 자동화하자
1 SNS 포스팅 글 생성 봇 개요 및 완성형
__1-1 완성형을 살펴보자
__1-2 게시물 생성 봇이란?
__1-3 개발의 흐름
2 과거 포스팅 글에서 문체를 학습시키자!
__2-1 퓨샷 학습이란?
__2-2 사용하는 프롬프트
__2-3 제로샷의 경우
__2-4 원샷 학습의 경우
__2-5 퓨샷 학습의 경우
3 트위터 API를 사용해 게시하기
__3-1 트위터 API로 할 수 있는 일
__3-2 트위터 API 요금제
__3-3 트위터 API의 API 키를 얻자
__3-4 봇을 구현하자
__3-5 게시물의 무작위성이나 어조를 조절하기
__3-6 봇의 적용 사례와 주의점
 
▣ 04장: 나만의 데이터로 학습한 채팅봇을 만들어보자
1 챗봇의 개요와 완성형
__1-1 완성형을 살펴보자
__1-2 개발의 흐름
2 나만의 데이터를 학습하는 방법
__2-1 대량의 데이터를 학습시킬 수 있는 RAG
__2-2 벡터 데이터를 보관하는 벡터 DB
__2-3 RAG를 활용하여 데이터에 기반한 답변을 이끌어내는 방법은?
3 독자적인 데이터를 임베딩해 보자
__3-1 학습 데이터의 텍스트 파일을 만들자
__3-2 학습 데이터를 CSV로 변환하자
__3-3 학습 데이터를 임베딩하자
4 챗봇을 작동시켜 보자
__4-1 챗GPT와 대화하는 프로그램을 만들어 보자
__4-2 주어진 지식을 바탕으로 답하는 프로그램을 만들어 보자
__4-3 대화 프로그램을 개조하여 챗봇을 완성하자
__4-4 챗봇에 개성을 부여
__4-5 자체 데이터를 학습한 챗봇의 응용 사례
 
▣ 05장: 음성 데이터를 필사하고 요약해 보자
1 위스퍼 개요 및 완성형
__1-1 위스퍼 개요
__1-2 완성형을 살펴보자
__1-3 개발 단계
2 음성 필사 가능한 위스퍼
__2-1 전사 AI의 기술적 구조
__2-2 높은 정확도의 전사 작업이 가능한 위스퍼
__2-3 언어에 따른 정확도 차이
__2-4 OSS 버전과 API 버전
__2-5 요금 체계
3 위스퍼로 받아쓰기를 해 보자
__3-1 음성 파일 준비하기
__3-2 클라이언트를 준비하자
__3-3 API 키 설정하기
__3-4 전사 작업을 해보자
__3-5 출력 형식을 바꿔보자
4 받아쓴 문장을 요약해 보자
__4-1 필사하자
__4-2 요약하기
5 위스퍼의 번역 기능을 활용해 받아쓰기와 번역을 동시에 실행
__5-1 위스퍼의 번역 기능이 무엇인지 알아보자!
__5-2 한국어 음성을 번역하고 영어 전사 작업을 한다
__5-3 영어로 번역하면서 필사본을 요약해 보자
 
▣ 06장: 최신 정보를 포함한 뉴스 기사를 만들자
1 뉴스 기사 생성 프로그램 개요 및 완성형
__1-1 완성형을 살펴보자
__1-2 개발 흐름
__1-3 검색엔진과 챗GPT를 연동해 활용하기
2 복잡한 LLM 앱 개발을 효율화하는 랭체인
__2-1 랭체인이란?
__2-2 랭체인의 주요 기능
__2-3 랭체인 사용 시 주의 사항
3 최신 정보를 포함한 뉴스 기사를 만들자
__3-1 필요한 라이브러리를 설치하자
__3-2 Google 검색을 위한 API 키를 얻자
__3-3 최신 정보에 기반한 뉴스 기사 생성하기
__3-4 해외 사이트에서 정보 수집하여 기사화하기
 
▣ 07장: PDF에서 데이터를 추출해 그래프로 만들어 보자
1 PDF에서 데이터 추출하는 프로그램의 개요 및 완성형
__1-1 완성형을 살펴보자
__1-2 개발 흐름
2 구조화된 데이터와 비정형 데이터란?
__2-1 정형 데이터와 비정형 데이터
__2-2 비정형 데이터의 활용이 중요한 이유
__2-3 비정형 데이터를 정형 데이터로 변환하기
3 랭체인으로 PDF를 구조화된 데이터로 변환하자
__3-1 PDF를 읽어 들여 구조화된 데이터로 변환하자
__3-2 구조화된 데이터를 CSV로 출력해 보자
__3-3 데이터 시각화하기
__3-4 활용 사례
4 PDF의 내용을 바탕으로 답변하는 챗봇 만들기
__4-1 챗봇의 완성형
__4-2 PDF 내용을 바탕으로 챗봇이 답변하게 하기
__4-3 다양한 응용 가능성
 
▣ 08장: 운영상의 문제를 예방하자
1 챗GPT API 이용 시 주의사항
__1-1 OpenAI의 데이터 이용 정책 알아보기
__1-2 개인정보, 기밀정보 입력 금지
__1-3 예상치 못한 고액 청구 방지
2 부적절한 콘텐츠 생성을 방지
__2-1 부적절한 콘텐츠 생성 방지의 필요성에 대해
__2-2 문제 발언을 감지할 수 있는 ‘모더레이션 API’란?
__2-3 모더레이션 API를 사용해 보자
__2-4 모더레이션 API의 주의점
3 오류에 대처하자
__3-1 OpenAI의 API 오류 코드와 대처 방법
__3-2 파이썬 라이브러리 오류 대처 방법
__3-3 API 접속 횟수를 제한하는 ‘Rate Limits’
 
▣ 09장: 프롬프트 주입에 대한 대책을 세우자
1 프롬프트 주입이란?
__1-1 프롬프트 주입은 AI에 대한 공격 기법
__1-2 프롬프트 주입의 작동 원리
__1-3 프롬프트 주입이 유발하는 문제
2 프롬프트 주입 예시
__2-1 모델 출력 가로채기
__2-2 시스템에서 설정한 프롬프트 추출하기
__2-3 윤리적으로 문제가 있는 내용을 출력하게 한다.
3 프롬프트 주입 대책
__3-1 프롬프트 주입에 대한 대책은 어렵다
__3-2 대책 ➊: 사용자 입력값 제한 및 검증하기
__3-3 대책 ➋: 챗GPT의 출력 검증하기
__3-4 대책 ➌: 사용자 입출력 텍스트 수집하기
