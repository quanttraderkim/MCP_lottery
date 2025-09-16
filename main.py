import functions_framework
import random
import json

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

@functions_framework.http
def lotto_generator_mcp(request):
    """
    Google Cloud Functions HTTP 트리거 함수
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
        return (json.dumps({"error": "Method Not Allowed"}), 405, headers)
    
    try:
        # 로또 번호 생성
        numbers = generate_lotto_numbers()
        
        # JSON 응답 생성
        response_data = {"numbers": numbers}
        response_json = json.dumps(response_data, ensure_ascii=False)
        
        # HTTP 200 상태 코드와 함께 JSON 응답 반환
        return (response_json, 200, headers)
        
    except Exception as e:
        # 에러 발생 시 500 에러 반환
        error_response = {"error": "로또 번호 생성 중 오류가 발생했습니다."}
        return (json.dumps(error_response, ensure_ascii=False), 500, headers)
