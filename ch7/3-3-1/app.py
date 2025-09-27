import load_pdf
import csv
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter
from dotenv import load_dotenv
import os
import time
load_dotenv()

def write_to_csv(billing_data):
    print("💾 CSV 파일을 생성하는 중...")
    csv_start_time = time.time()
    
    # CSV 파일명
    csv_file = "invoices.csv"
    print(f"📄 파일명: {csv_file}")

    # 헤더를 결정 (JSON의 키에서)
    header = billing_data[0].keys()
    print(f"📋 CSV 헤더: {list(header)}")
    print(f"📊 데이터 행 수: {len(billing_data)}")

    # CSV 파일을 쓰기 모드로 열어 데이터를 쓰기
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(billing_data)
    
    csv_time = time.time() - csv_start_time
    print(f"✅ CSV 파일 생성 완료 (소요시간: {csv_time:.2f}초)")
    return csv_time

def draw_graph(filename):
    print("📊 그래프를 생성하는 중...")
    graph_start_time = time.time()
    
    try:
        # pandas의 DataFrame으로 'invoices.csv' 파일에서 데이터 읽기 (숫자의 콤마 구분에 대응)
        print("📁 CSV 파일을 읽는 중...")
        df = pd.read_csv("invoices.csv", thousands=",")
        print(f"✅ CSV 파일 읽기 완료 (행 수: {len(df)})")

        # 데이터 타입 확인 및 변환
        print("🔍 데이터 타입을 확인하는 중...")
        print(f"   청구금액(총액) 컬럼 타입: {df['청구금액(총액)'].dtype}")
        print(f"   청구금액(총액) 샘플 값: {df['청구금액(총액)'].head().tolist()}")
        
        # 청구금액을 숫자로 변환 (문자열인 경우 처리)
        if df["청구금액(총액)"].dtype == 'object':
            print("🔢 청구금액을 숫자로 변환하는 중...")
            df["청구금액(총액)"] = pd.to_numeric(df["청구금액(총액)"].astype(str).str.replace(',', ''), errors='coerce')
            print("✅ 숫자 변환 완료")

        # 날짜 형식 변환
        print("📅 날짜 형식을 변환하는 중...")
        df["발행일"] = pd.to_datetime(
            df["발행일"].str.replace(" ", "").str.replace("년", "-").str.replace("월", "-").str.replace("일", ""),
            format="%Y-%m-%d",
        )
        print("✅ 날짜 변환 완료")

        # 그래프 그리기
        print("📈 그래프를 그리는 중...")
        fig, ax = plt.subplots()
        ax.bar(df["발행일"], df["청구금액(총액)"])
        ax.set_xlabel("date")
        ax.set_ylabel("price")
        ax.set_xticks(df["발행일"])
        ax.set_xticklabels(df["발행일"].dt.strftime("%Y-%m-%d"), rotation=45)

        # y축의 최솟값을 0으로 설정 (숫자 타입 확인)
        max_amount = df["청구금액(총액)"].max()
        print(f"💰 최대 청구금액: {max_amount:,.0f}원")
        ax.set_ylim(0, max_amount + 100000)

        # y축 라벨을 원래 숫자로 표시
        ax.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ",")))

        plt.tight_layout()
        print("✅ 그래프 생성 완료")
        plt.show()
        
        graph_time = time.time() - graph_start_time
        print(f"⏱️  그래프 생성 소요시간: {graph_time:.2f}초")
        return graph_time
        
    except Exception as e:
        print(f"❌ 그래프 생성 중 오류 발생: {str(e)}")
        print("   데이터 형식을 확인해주세요.")
        return 0


def main():
    # 전체 실행 시간 측정 시작
    total_start_time = time.time()
    
    print("🚀 PDF 데이터 추출, CSV 변환 및 그래프 생성 프로그램을 시작합니다...")
    print("=" * 70)
    
    # 1. PDF 파일 로딩
    print("📁 PDF 파일들을 로딩하는 중...")
    print("   📂 대상 폴더: data/")
    
    pdf_start_time = time.time()
    billing_data = load_pdf.load_all_pdfs("data")
    pdf_time = time.time() - pdf_start_time
    
    print(f"✅ PDF 로딩 완료 (소요시간: {pdf_time:.2f}초)")
    print(f"📊 추출된 데이터 건수: {len(billing_data)}건")
    
    if billing_data:
        print("📋 추출된 데이터 샘플:")
        print(f"   - 첫 번째 레코드 키: {list(billing_data[0].keys())}")
        print(f"   - 첫 번째 레코드 값: {list(billing_data[0].values())}")
    else:
        print("⚠️  추출된 데이터가 없습니다.")
        print("   data/ 폴더에 PDF 파일이 있는지 확인해주세요.")
        return

    # 2. CSV 파일 생성
    print("\n" + "=" * 70)
    csv_time = write_to_csv(billing_data)

    # 3. 그래프 생성
    print("\n" + "=" * 70)
    graph_time = draw_graph("invoices.csv")
    
    # 전체 실행 시간 계산
    total_time = time.time() - total_start_time
    
    print("\n" + "=" * 70)
    print("🎉 PDF 데이터 추출, CSV 변환 및 그래프 생성이 완료되었습니다!")
    
    print("\n📊 실행 시간 요약:")
    print("=" * 70)
    print(f"📁 PDF 파일 로딩: {pdf_time:.2f}초")
    print(f"💾 CSV 파일 생성: {csv_time:.2f}초")
    print(f"📊 그래프 생성: {graph_time:.2f}초")
    print("-" * 50)
    print(f"⏱️  총 실행 시간: {total_time:.2f}초")
    print("=" * 70)


if __name__ == "__main__":
    main()
