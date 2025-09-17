FROM python:3.11-slim

WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY mcp_server.py .

# 포트 설정
EXPOSE 8000

# MCP 서버 실행
CMD ["python", "mcp_server.py"]
