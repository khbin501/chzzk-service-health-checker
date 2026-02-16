# chzzk-service-health-checker

📺 Chzzk Service Monitor
Chzzk Service Monitor는 네이버의 스트리밍 플랫폼 '치지직(Chzzk)'의 가동 상태와 응답 속도를 실시간으로 감시하는 파이썬 기반 모니터링 도구입니다. 클라우드 엔지니어링의 핵심인 서비스 가용성(Availability) 체크 기능을 구현한 프로젝트입니다.

🚀 주요 기능
상태 코드 확인: HTTP 응답 코드를 통해 서버의 정상 작동 여부 판단

지연 시간 측정: 서버 응답 속도(Latency)를 초 단위로 계산하여 성능 모니터링

예외 처리: 서버 다운, 타임아웃 등 다양한 장애 상황에 대한 로그 출력

🛠 시작하기
1. 요구 사항
이 프로젝트를 실행하기 위해 파이썬 3.x 버전과 requests 라이브러리가 필요합니다.

Bash
pip install requests
2. 설치 및 실행
Bash
# 저장소 복제
git clone https://github.com/khbin501/chzzk-service-health-checker

# 폴더 이동
./cd chzzk-service-health-checker

# 스크립트 실행
python main.py

📂 프로젝트 구조
main.py: 서비스 상태를 체크하는 메인 로직

README.md: 프로젝트 설명 문서

📈 향후 계획 (Roadmap)
로그 저장: 모니터링 결과를 .txt 또는 .csv 파일로 저장 기능 추가

알림 시스템: 서버 장애 발생 시 텔레그램 알림 발송 기능 구현

대시보드: Streamlit을 활용한 실시간 응답 속도 시각화