FROM python:3.11-slim

WORKDIR /app

# 소스 코드 복사
COPY correct_mcp_server.py .

# 포트 설정
EXPOSE 8000

# 올바른 MCP 서버 실행
CMD ["python", "correct_mcp_server.py"]
