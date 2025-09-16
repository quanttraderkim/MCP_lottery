from flask import Flask, jsonify
import random

app = Flask(__name__)

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

@app.route('/generate', methods=['GET'])
def get_lotto_numbers():
    """
    로또 번호를 생성하고 JSON 형식으로 반환하는 API 엔드포인트
    """
    try:
        numbers = generate_lotto_numbers()
        return jsonify({"numbers": numbers})
    except Exception as e:
        return jsonify({"error": "로또 번호 생성 중 오류가 발생했습니다."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
