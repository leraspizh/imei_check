from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from app.imei_service import check_imei_api
from config import API_TOKEN_SANDBOX


app = FastAPI()

class ImeiRequest(BaseModel):
    """
    Класс IMEIRequest используется для обработки входящих запросов от пользователей,
    которые отправляют IMEI устройства и токен для авторизации.

    Attributes:
        imei : Уникальный идентификатор устройства (IMEI), который должен быть проверен.
        token : Токен для авторизации, который используется для проверки доступа к API.

    """
    imei: str
    token: str


@app.post("/api/check-imei")
async def check_imei(request: ImeiRequest) -> Dict[str, Any]:
    """Функция check_imei обрабатывает POST-запрос для проверки IMEI через внешний API"""
    if API_TOKEN_SANDBOX != request.token :
        raise HTTPException(status_code=403, detail="Неверный токен API")

    imei_data = check_imei_api(request.model_dump())
    return imei_data

