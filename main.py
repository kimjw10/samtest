from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI(
    title="간단한 상품 관리 API",
    description="FastAPI의 기본 기능을 보여주는 예제입니다."
)

# 임시 데이터베이스 (실제 서비스에서는 MySQL, PostgreSQL 등을 사용합니다)
inventory = {}

# Pydantic을 이용한 데이터 유효성 검사 모델
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None  # 선택 사항 (입력하지 않아도 됨)

@app.get("/")
def read_root():
    """루트 경로 API - 서버가 정상 작동하는지 확인합니다."""
    return {"message": " ssaft FastAPI 서버가 정상적으로 실행 중입니다! ssafy"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """특정 ID의 상품 정보를 가져옵니다."""
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")
    return {"item_id": item_id, "item_info": inventory[item_id]}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    """새로운 상품을 등록합니다."""
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="이미 존재하는 상품 ID입니다.")
    
    inventory[item_id] = item
    return {"message": "상품이 성공적으로 등록되었습니다.", "data": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """특정 ID의 상품을 삭제합니다."""
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="삭제할 상품을 찾을 수 없습니다.")
    
    del inventory[item_id]
    return {"message": f"{item_id}번 상품이 삭제되었습니다."}