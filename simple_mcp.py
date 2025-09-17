#!/usr/bin/env python3
"""
간단한 MCP 호환 서버 - 행운의 로또 번호 생성기
playMCP와 호환되는 간단한 HTTP 서버
"""

import random
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import os

def generate_lotto_numbers():
    """
    1부터 45까지의 숫자 중에서 중복되지 않는 6개의 숫자를 무작위로 뽑아
    오름차순으로 정렬한 리스트를 반환하는 함수
    """
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))
    
    # 6개의 숫자를 무작위로 선택 (중복 없음)
    selected_numbers = random.sample(numbers, 6)
    
    # 오름차순으로 정렬
    selected_numbers.sort()
    
    return selected_numbers

class MCPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """GET 요청 처리"""
        if self.path == '/':
            # 로또 번호 생성
            numbers = generate_lotto_numbers()
            
            # MCP 형식 응답
            response = {
                "jsonrpc": "2.0",
                "id": 1,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": f"오늘의 행운의 로또 번호: {', '.join(map(str, numbers))}"
                        }
                    ]
                }
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        """POST 요청 처리"""
        if self.path == '/':
            # 로또 번호 생성
            numbers = generate_lotto_numbers()
            
            # MCP 형식 응답
            response = {
                "jsonrpc": "2.0",
                "id": 1,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": f"오늘의 행운의 로또 번호: {', '.join(map(str, numbers))}"
                        }
                    ]
                }
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_OPTIONS(self):
        """OPTIONS 요청 처리 (CORS)"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    server = HTTPServer(('0.0.0.0', port), MCPHandler)
    print(f"MCP 서버가 포트 {port}에서 시작되었습니다...")
    server.serve_forever()
