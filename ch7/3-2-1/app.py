import load_pdf
import csv
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator, FuncFormatter
import time
from dotenv import load_dotenv
import os
load_dotenv()

def write_to_csv(billing_data):
    print("💾 CSV 파일을 생성하는 중...")
    csv_start_time = time.time()
    
    # CSV 파일명
    csv_file = "invoices.csv"
    

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

def main():
    # 전체 실행 시간 측정 시작
    total_start_time = time.time()
    
    print("🚀 PDF 데이터 추출 및 CSV 변환 프로그램을 시작합니다...")
    print("=" * 60)
    
    # 1. PDF 파일 로딩
    print("📁 PDF 파일들을 로딩하는 중...")
    print("   📂 대상 폴더: data/")
    
    pdf_start_time = time.time()
    billing_data = load_pdf.load_all_pdfs('data')
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
    print("\n" + "=" * 60)
    csv_time = write_to_csv(billing_data)
    
    # 전체 실행 시간 계산
    total_time = time.time() - total_start_time
    
    print("\n" + "=" * 60)
    print("🎉 PDF 데이터 추출 및 CSV 변환이 완료되었습니다!")
    print("📄 invoices.csv 파일을 확인해보세요.")
    
    print("\n📊 실행 시간 요약:")
    print("=" * 60)
    print(f"📁 PDF 파일 로딩: {pdf_time:.2f}초")
    print(f"💾 CSV 파일 생성: {csv_time:.2f}초")
    print("-" * 40)
    print(f"⏱️  총 실행 시간: {total_time:.2f}초")
    print("=" * 60)

if __name__ == "__main__":
    main()
