import requests
import time
from datetime import datetime

def check_chzzk():
    target_url = "https://chzzk.naver.com"
    
    try:
        # 1. 접속 시도 및 시간 측정 시작
        start_time = time.time()
        response = requests.get(target_url, timeout=5) # 5초 안에 응답 없으면 실패로 간주
        end_time = time.time()
        
        # 2. 결과 분석
        latency = round(end_time - start_time, 3) # 소수점 3자리까지
        status_code = response.status_code
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if status_code == 200:
            print(f"[{now}] ✅ 치지직 정상 작동 중! (응답 시간: {latency}초)")
        else:
            print(f"[{now}] ⚠️ 치지직 상태 불안정. (상태 코드: {status_code})")

    except requests.exceptions.Timeout:
        print(f"[{now}] 🚨 응답 시간 초과! 서버가 매우 느리거나 죽었을 가능성이 있습니다.")
    except Exception as e:
        print(f"[{now}] ❌ 연결 실패: {e}")

# 실행
if __name__ == "__main__":
    print("--- 치지직 모니터링 시작 ---")
    check_chzzk()