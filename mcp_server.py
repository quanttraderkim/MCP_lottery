#!/usr/bin/env python3
"""
MCP 서버 - 행운의 로또 번호 생성기
FastMCP 프레임워크를 사용하여 MCP 스펙에 맞는 서버 구현
"""

import random
import json
import asyncio
from fastmcp import FastMCP

# MCP 서버 인스턴스 생성
mcp = FastMCP("행운의 로또 번호 생성기")

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

@mcp.tool()
def generate_lotto() -> str:
    """
    로또 번호를 생성합니다.
    1부터 45까지의 숫자 중에서 중복되지 않는 6개의 숫자를 무작위로 선택하여 반환합니다.
    
    Returns:
        str: 생성된 로또 번호를 문자열로 반환
    """
    numbers = generate_lotto_numbers()
    return f"오늘의 행운의 로또 번호: {', '.join(map(str, numbers))}"

@mcp.tool()
def get_lotto_numbers() -> dict:
    """
    로또 번호를 JSON 형식으로 생성합니다.
    
    Returns:
        dict: {"numbers": [숫자 리스트]} 형식의 딕셔너리
    """
    numbers = generate_lotto_numbers()
    return {"numbers": numbers}

async def main():
    """메인 함수"""
    import os
    port = int(os.environ.get('PORT', 8000))
    await mcp.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # MCP 서버 실행
    asyncio.run(main())
