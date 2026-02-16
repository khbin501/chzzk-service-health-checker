import requests
import time
from datetime import datetime

def check_chzzk():
    target_url = "https://chzzk.naver.com"
    log_file = "chzzk_monitor.log"
    
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
            log_msg = (f"[{now}] ✅ 정상 작동 중! (응답 시간: {latency}초)")
        else:
            log_msg = (f"[{now}] ⚠️ 상태 불안정. (상태 코드: {status_code})")

    except requests.exceptions.Timeout:
        log_msg = (f"[{now}] 🚨 응답 시간 초과! 서버가 매우 느리거나 죽었을 가능성이 있습니다.")

    except Exception as e:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_msg = f"[{now}] ❌ 장애 발생: {e}"
        
        #1. 화면에 출력
    print(log_msg)

        # 2. 파일에 저장 ('a' 모드는 기존 내용 뒤에 이어서 쓴다는 뜻입니다)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_msg + "\n")









if __name__ == "__main__":
    print("--- 치지직 모니터링 및 로그 기록 시작 ---")
    # 테스트를 위해 5번 반복 실행해봅니다.
    for i in range(5):
        check_chzzk()
        time.set_sleep = time.sleep(2) # 2초 간격으로 체크