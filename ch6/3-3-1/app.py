from langchain.agents import Tool, create_openai_tools_agent, AgentExecutor
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import time
load_dotenv()

def create_prompt():
    print("📝 프롬프트 템플릿을 생성하는 중...")
    template = ChatPromptTemplate.from_messages([
        ("system", "당신은 뉴스 기사를 쓰는 블로거입니다. 다음 주제에 대해 구글 검색을 통해 최신 정보를 얻고, 그 정보를 바탕으로 뉴스 기사를 작성해 주세요. 1000자 이상, 한국어로 출력해 주세요. 기사 말미에 참고한 URL을 참조 출처로 제목과 URL을 출력해 주세요."),
        ("human", "{theme}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])
    print("✅ 프롬프트 템플릿 생성 완료")
    return template

def define_tools():
    print("🔧 도구(Tools)를 정의하는 중...")
    
    # Google API 키와 CSE ID가 설정되어 있는지 확인
    google_api_key = os.getenv("GOOGLE_API_KEY")
    google_cse_id = os.getenv("GOOGLE_CSE_ID")
    
    print(f"🔑 Google API Key: {'설정됨' if google_api_key else '❌ 미설정'}")
    print(f"🔍 Google CSE ID: {'설정됨' if google_cse_id and google_cse_id != 'your_custom_search_engine_id_here' else '❌ 미설정'}")
    
    if not google_api_key or not google_cse_id or google_cse_id == "your_custom_search_engine_id_here":
        print("⚠️  Google API 키 또는 CSE ID가 설정되지 않았습니다.")
        print("   Custom Search Engine을 생성하고 .env 파일을 업데이트해주세요.")
        print("   https://cse.google.com/cse/ 에서 검색 엔진을 생성하세요.")
        print("❌ 검색 도구 없이 실행됩니다.")
        return []
    
    print("🔍 Google Search API Wrapper를 초기화하는 중...")
    search = GoogleSearchAPIWrapper(
        google_api_key=google_api_key,
        google_cse_id=google_cse_id
    )
    
    tools = [
        Tool(
            name = "Search",
            func=search.run,
            description="useful for when you need to answer questions about current events. You should ask targeted questions"
        ),
    ]
    print(f"✅ {len(tools)}개의 도구가 정의되었습니다.")
    return tools

def write_response_to_file(response, filename):
    print(f"💾 결과를 {filename} 파일에 저장하는 중...")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response)
    print(f"✅ {filename} 파일 저장 완료")

def main():
    # 전체 실행 시간 측정 시작
    total_start_time = time.time()
    
    print("🚀 뉴스 기사 생성 프로그램을 시작합니다...")
    print("=" * 50)
    
    # 1. LLM 초기화
    print("🤖 OpenAI LLM을 초기화하는 중...")
    llm_start_time = time.time()
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", max_tokens=2000, api_key=os.getenv("OPENAI_API_KEY"))
    llm_time = time.time() - llm_start_time
    print(f"✅ LLM 초기화 완료 (소요시간: {llm_time:.2f}초)")
    
    # 2. 도구 정의
    tools_start_time = time.time()
    tools = define_tools()
    tools_time = time.time() - tools_start_time
    print(f"⏱️  도구 정의 소요시간: {tools_time:.2f}초")
    
    # 3. 프롬프트 생성
    prompt_start_time = time.time()
    prompt = create_prompt()
    prompt_time = time.time() - prompt_start_time
    print(f"⏱️  프롬프트 생성 소요시간: {prompt_time:.2f}초")

    # 4. 에이전트 생성
    print("🤖 AI 에이전트를 생성하는 중...")
    agent_start_time = time.time()
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)
    agent_time = time.time() - agent_start_time
    print(f"✅ AI 에이전트 생성 완료 (소요시간: {agent_time:.2f}초)")

    # 5. 사용자 입력 받기
    print("\n" + "=" * 50)
    input_start_time = time.time()
    theme = input("📝 기사 주제를 입력해 주세요: ")
    input_time = time.time() - input_start_time
    print(f"📋 입력된 주제: {theme}")
    print(f"⏱️  사용자 입력 소요시간: {input_time:.2f}초")
    print("=" * 50)

    # 6. 에이전트 실행
    print("🔄 AI 에이전트가 작업을 시작합니다...")
    print("   (검색 및 기사 작성 중... 시간이 걸릴 수 있습니다)")
    
    try:
        agent_execution_start_time = time.time()
        response = agent_executor.invoke({"theme": theme})
        agent_execution_time = time.time() - agent_execution_start_time
        print(f"✅ AI 에이전트 작업 완료 (소요시간: {agent_execution_time:.2f}초)")
        
        # 7. 결과 저장
        save_start_time = time.time()
        write_response_to_file(response["output"], 'output.txt')
        save_time = time.time() - save_start_time
        print(f"⏱️  파일 저장 소요시간: {save_time:.2f}초")
        
        # 전체 실행 시간 계산
        total_time = time.time() - total_start_time
        
        print("\n" + "=" * 50)
        print("🎉 뉴스 기사 생성이 완료되었습니다!")
        print("📄 output.txt 파일을 확인해보세요.")
        print("\n📊 실행 시간 요약:")
        print("=" * 50)
        print(f"🤖 LLM 초기화: {llm_time:.2f}초")
        print(f"🔧 도구 정의: {tools_time:.2f}초")
        print(f"📝 프롬프트 생성: {prompt_time:.2f}초")
        print(f"🤖 에이전트 생성: {agent_time:.2f}초")
        print(f"⌨️  사용자 입력: {input_time:.2f}초")
        print(f"🔄 AI 작업 실행: {agent_execution_time:.2f}초")
        print(f"💾 파일 저장: {save_time:.2f}초")
        print("-" * 30)
        print(f"⏱️  총 실행 시간: {total_time:.2f}초")
        print("=" * 50)
        
    except Exception as e:
        total_time = time.time() - total_start_time
        print(f"❌ 오류가 발생했습니다: {str(e)}")
        print("   API 키 설정을 확인해주세요.")
        print(f"⏱️  오류 발생까지 소요시간: {total_time:.2f}초")

if __name__ == "__main__":
    main()
