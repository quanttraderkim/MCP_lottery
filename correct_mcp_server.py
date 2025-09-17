#!/usr/bin/env python3
"""
올바른 MCP 서버 - 행운의 로또 번호 생성기
PlayMCP와 호환되는 MCP 프로토콜 구현
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
    def do_POST(self):
        """POST 요청 처리 - MCP 프로토콜"""
        if self.path == '/mcp':
            # 요청 본문 읽기
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode('utf-8'))
            
            # MCP 프로토콜 처리
            response = self.handle_mcp_request(request_data)
            
            # 응답 전송
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
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
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def handle_mcp_request(self, request):
        """MCP 요청 처리"""
        method = request.get('method')
        request_id = request.get('id', 1)
        
        if method == 'tools/list':
            # 사용 가능한 도구 목록 반환
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "tools": [
                        {
                            "name": "generate_lotto",
                            "description": "Generate lucky lotto numbers (6 numbers from 1 to 45)",
                            "inputSchema": {
                                "type": "object",
                                "properties": {},
                                "required": []
                            }
                        }
                    ]
                }
            }
        
        elif method == 'tools/call':
            # 도구 실행
            params = request.get('params', {})
            tool_name = params.get('name')
            
            if tool_name == 'generate_lotto':
                numbers = generate_lotto_numbers()
                return {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": f"🎲 Today's lucky lotto numbers: {', '.join(map(str, numbers))}"
                            }
                        ]
                    }
                }
            else:
                return {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "error": {
                        "code": -32601,
                        "message": f"Tool '{tool_name}' not found"
                    }
                }
        
        else:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32601,
                    "message": f"Method '{method}' not found"
                }
            }

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    server = HTTPServer(('0.0.0.0', port), MCPHandler)
    print(f"MCP 서버가 포트 {port}에서 시작되었습니다...")
    print(f"Endpoint: http://0.0.0.0:{port}/mcp")
    server.serve_forever()
