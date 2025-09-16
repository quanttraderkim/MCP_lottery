import streamlit as st
import random
import requests
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

# Streamlit 앱 설정
st.set_page_config(
    page_title="행운의 로또 번호 생성기",
    page_icon="🎲",
    layout="centered"
)

# 메인 타이틀
st.title("🎲 행운의 로또 번호 생성기")
st.markdown("---")

# 설명
st.markdown("**오늘의 행운을 시험해보세요!**")
st.markdown("1부터 45까지의 숫자 중에서 중복되지 않는 6개의 숫자를 추천해드립니다.")

# 버튼과 로또 번호 생성
if st.button("🎯 로또 번호 생성하기", type="primary", use_container_width=True):
    with st.spinner("행운의 숫자를 뽑고 있습니다..."):
        numbers = generate_lotto_numbers()
    
    # 결과 표시
    st.success("🎉 행운의 로또 번호가 생성되었습니다!")
    
    # 번호를 예쁘게 표시
    cols = st.columns(6)
    for i, num in enumerate(numbers):
        with cols[i]:
            st.markdown(f"""
            <div style="
                background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
                color: white;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                margin: 5px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            ">
                {num}
            </div>
            """, unsafe_allow_html=True)
    
    # JSON 형식으로도 표시 (API 호출용)
    st.markdown("**API 응답 형식:**")
    st.json({"numbers": numbers})
    
    # 새로고침 버튼
    if st.button("🔄 다른 번호 생성하기", use_container_width=True):
        st.rerun()

# API 엔드포인트 정보
st.markdown("---")
st.markdown("### 📡 API 정보")
st.markdown("이 앱은 MCP 서버로도 사용할 수 있습니다:")
st.code("GET /generate", language="text")
st.markdown("**응답 예시:**")
st.json({"numbers": [5, 12, 23, 31, 38, 44]})

# 푸터
st.markdown("---")
st.markdown("💡 **팁**: 새로고침하거나 버튼을 다시 클릭하면 새로운 번호를 받을 수 있습니다!")
