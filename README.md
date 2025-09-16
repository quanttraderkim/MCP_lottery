# 행운의 로또 번호 생성기 (GCP Cloud Functions)

Google Cloud Functions를 사용하여 playMCP에 연동할 수 있는 로또 번호 생성기 API입니다.

## 기능

- 1부터 45까지의 숫자 중 중복되지 않는 6개의 숫자를 무작위로 생성
- 생성된 번호를 오름차순으로 정렬하여 반환
- JSON 형식의 API 응답
- CORS 지원으로 웹에서 직접 호출 가능

## API 엔드포인트

### HTTP GET 요청

로또 번호를 생성합니다.

**응답 예시:**
```json
{
  "numbers": [5, 12, 23, 31, 38, 44]
}
```

## 로컬 테스트

1. 의존성 설치:
```bash
pip install -r requirements.txt
```

2. Functions Framework로 로컬 실행:
```bash
functions-framework --target=lotto_generator_mcp --source=main.py
```

3. API 테스트:
```bash
curl http://127.0.0.1:8080
```

## GCP 배포

### 1. Google Cloud CLI 설치 및 설정
```bash
# gcloud CLI 설치 (macOS)
brew install google-cloud-sdk

# 인증
gcloud auth login

# 프로젝트 설정
gcloud config set project YOUR_PROJECT_ID
```

### 2. Cloud Functions 배포
```bash
gcloud functions deploy lotto-generator-mcp \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --source . \
  --entry-point lotto_generator_mcp
```

### 3. 함수 URL 확인
```bash
gcloud functions describe lotto-generator-mcp --region=us-central1
```

## playMCP 등록 정보

- **MCP 이름**: 행운의 로또 번호 생성기
- **MCP 설명**: 오늘의 행운을 시험해보세요! 버튼 하나로 간편하게 로또 추천 번호를 받을 수 있습니다.
- **MCP Endpoint**: `https://us-central1-YOUR_PROJECT_ID.cloudfunctions.net/lotto-generator-mcp`
- **대화 예시**: 
  - "로또 번호 추천해줘"
  - "로또 번호 생성"
  - "행운의 숫자 알려줘"
