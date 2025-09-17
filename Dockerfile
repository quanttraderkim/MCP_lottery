FROM python:3.11-slim

WORKDIR /app

# 소스 코드 복사
COPY simple_mcp.py .

# 포트 설정
EXPOSE 8000

# 간단한 MCP 서버 실행
CMD ["python", "simple_mcp.py"]
