import requests
import random
import json
from typing import Dict, Any
from config import API_TOKEN_SANDBOX,SERVICES_URL,CHECKS_URL

def get_random_service_id() -> int:
    """Функция get_random_service_id получает случайное serviceId из списка доступных сервисов"""
    headers = {
        'Authorization': f'Bearer {API_TOKEN_SANDBOX}',
        'Accept-Language': 'en',
        'Content-Type': 'application/json'
    }

    response = requests.get(SERVICES_URL, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Ошибка получения сервиса: {response.status_code}, {response.text}")

    services = response.json()

    if isinstance(services, list):
        random_service = random.choice(services)
        return random_service['id']
    else:
        raise Exception(f"Ошибка получения списка сервисов")

def check_imei_api(request: Dict[str, str]) -> Dict[str, Any]:
    """Функция check_imei_api проверяет IMEI через внешний API и выводит данные об устройстве"""
    service_id = get_random_service_id()
    headers = {
        "Authorization": f"Bearer {API_TOKEN_SANDBOX}",
        "Content-Type": "application/json",
    }

    body = json.dumps({
        "deviceId": request['imei'],
        "serviceId": service_id
    })

    response = requests.post(CHECKS_URL, headers=headers, data=body)
    return response.json()
