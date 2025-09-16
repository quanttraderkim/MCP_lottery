import functions_framework
import random
import json
import os
from flask import Flask, request, jsonify

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

# Cloud Run용 Flask 앱 생성
app = Flask(__name__)

@app.route('/', methods=['GET', 'OPTIONS'])
def lotto_generator_mcp():
    """
    Cloud Run HTTP 엔드포인트
    로또 번호를 생성하고 JSON 형식으로 반환
    """
    # CORS 헤더 설정 (웹에서 호출 가능하도록)
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    # OPTIONS 요청 처리 (CORS preflight)
    if request.method == 'OPTIONS':
        return ('', 204, headers)
    
    # GET 요청만 허용
    if request.method != 'GET':
        return jsonify({"error": "Method Not Allowed"}), 405
    
    try:
        # 로또 번호 생성
        numbers = generate_lotto_numbers()
        
        # JSON 응답 생성
        response_data = {"numbers": numbers}
        
        # HTTP 200 상태 코드와 함께 JSON 응답 반환
        return jsonify(response_data), 200
        
    except Exception as e:
        # 에러 발생 시 500 에러 반환
        error_response = {"error": "로또 번호 생성 중 오류가 발생했습니다."}
        return jsonify(error_response), 500

# Cloud Functions용 함수 (호환성 유지)
@functions_framework.http
def lotto_generator_mcp_functions(request):
    """
    Google Cloud Functions HTTP 트리거 함수 (호환성 유지)
    """
    return lotto_generator_mcp()

if __name__ == '__main__':
    # Cloud Run에서 실행될 때 포트 8080 사용
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
