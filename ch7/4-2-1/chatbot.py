from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
import time

# 환경 변수 로드
load_dotenv()

def main():
    # 전체 실행 시간 측정 시작
    total_start_time = time.time()
    
    print("🚀 PDF 챗봇 프로그램을 시작합니다...")
    print("=" * 60)
    
    # 1. API 키 확인
    print("🔑 API 키를 확인하는 중...")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai_api_key:
        print("❌ OPENAI_API_KEY가 설정되지 않았습니다.")
        print("   .env 파일에 OPENAI_API_KEY를 설정해주세요.")
        return
    
    print("✅ OpenAI API 키 확인 완료")
    
    # 2. PDF 파일 로딩
    print("\n📁 PDF 파일을 로딩하는 중...")
    pdf_file = "★ 서울특별시 스마트도시 및 정보화 기본계획(홈페이지 게시용).pdf"
    print(f"   📄 파일명: {pdf_file}")
    
    # 파일 존재 확인
    if not os.path.exists(pdf_file):
        print(f"❌ PDF 파일을 찾을 수 없습니다: {pdf_file}")
        print("   파일이 현재 디렉토리에 있는지 확인해주세요.")
        return
    
    print("✅ PDF 파일 확인 완료")
    
    # PDF 로더 초기화
    print("📖 PDF 로더를 초기화하는 중...")
    loader_start_time = time.time()
    loader = PyPDFLoader(pdf_file)
    loader_time = time.time() - loader_start_time
    print(f"✅ PDF 로더 초기화 완료 (소요시간: {loader_time:.2f}초)")
    
    # 3. LLM 초기화
    print("\n🤖 LLM을 초기화하는 중...")
    llm_start_time = time.time()
    try:
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            api_key=openai_api_key
        )
        llm_time = time.time() - llm_start_time
        print(f"✅ LLM 초기화 완료 (소요시간: {llm_time:.2f}초)")
    except Exception as e:
        print(f"❌ LLM 초기화 중 오류 발생: {str(e)}")
        print("   API 키나 네트워크 연결을 확인해주세요.")
        return

    # 4. 문서 로딩 및 분할
    print("\n📄 PDF 문서를 로딩하고 분할하는 중...")
    docs_start_time = time.time()
    try:
        documents = loader.load()
        docs_time = time.time() - docs_start_time
        print(f"✅ 문서 로딩 완료 (소요시간: {docs_time:.2f}초)")
        print(f"   📊 로딩된 문서 수: {len(documents)}개")
    except Exception as e:
        print(f"❌ 문서 로딩 중 오류 발생: {str(e)}")
        return

    # 5. 벡터 저장소 생성
    print("\n🔍 벡터 저장소를 생성하는 중...")
    print("   (PDF 내용을 임베딩하고 벡터 저장소를 구축합니다... 시간이 걸릴 수 있습니다)")
    
    vectorstore_start_time = time.time()
    try:
        # 임베딩 모델 초기화
        embeddings = OpenAIEmbeddings(api_key=openai_api_key)
        
        # Chroma 벡터 저장소 생성
        vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )
        
        vectorstore_time = time.time() - vectorstore_start_time
        print(f"✅ 벡터 저장소 생성 완료 (소요시간: {vectorstore_time:.2f}초)")
    except Exception as e:
        print(f"❌ 벡터 저장소 생성 중 오류 발생: {str(e)}")
        print("   API 키나 네트워크 연결을 확인해주세요.")
        return

    # 6. 검색 체인 생성
    print("\n🔗 검색 체인을 생성하는 중...")
    chain_start_time = time.time()
    try:
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
            return_source_documents=True
        )
        chain_time = time.time() - chain_start_time
        print(f"✅ 검색 체인 생성 완료 (소요시간: {chain_time:.2f}초)")
    except Exception as e:
        print(f"❌ 검색 체인 생성 중 오류 발생: {str(e)}")
        return
    
    # 7. 질문-답변 루프
    print("\n" + "=" * 60)
    print("💬 챗봇이 준비되었습니다!")
    print("   질문을 입력하거나 'quit'을 입력하여 종료하세요.")
    print("=" * 60)
    
    question_count = 0
    
    while True:
        try:
            # 사용자 입력 받기
            print(f"\n📝 질문 #{question_count + 1}:")
            question = input("   질문을 입력하세요: ").strip()
            
            if question.lower() in ['quit', 'exit', '종료', 'q']:
                print("👋 챗봇을 종료합니다.")
                break
            
            if not question:
                print("⚠️  질문을 입력해주세요.")
                continue
            
            print(f"🔍 질문: {question}")
            print("🤖 답변을 생성하는 중... (시간이 걸릴 수 있습니다)")
            
            # 질문 처리
            query_start_time = time.time()
            result = qa_chain.invoke({"query": question})
            query_time = time.time() - query_start_time
            
            answer = result["result"]
            
            print(f"✅ 답변 생성 완료 (소요시간: {query_time:.2f}초)")
            print("\n" + "=" * 40)
            print("🤖 챗봇 답변:")
            print("=" * 40)
            print(answer)
            print("=" * 40)
            
            question_count += 1
            
        except KeyboardInterrupt:
            print("\n\n👋 사용자가 프로그램을 종료했습니다.")
            break
        except Exception as e:
            print(f"\n❌ 질문 처리 중 오류 발생: {str(e)}")
            print("   다시 시도해주세요.")
    
    # 전체 실행 시간 계산
    total_time = time.time() - total_start_time
    
    print(f"\n📊 프로그램 실행 요약:")
    print("=" * 60)
    print(f"📖 PDF 로더 초기화: {loader_time:.2f}초")
    print(f"🤖 LLM 초기화: {llm_time:.2f}초")
    print(f"📄 문서 로딩: {docs_time:.2f}초")
    print(f"🔍 벡터 저장소 생성: {vectorstore_time:.2f}초")
    print(f"🔗 검색 체인 생성: {chain_time:.2f}초")
    print(f"💬 처리된 질문 수: {question_count}개")
    print(f"⏱️  총 실행 시간: {total_time:.2f}초")
    print("=" * 60)
    print("🎉 프로그램이 종료되었습니다!")

if __name__ == "__main__":
    main()
