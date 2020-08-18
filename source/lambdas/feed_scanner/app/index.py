import requests
from datetime import datetime


def handler(event: dict, context:dict) -> str:
    print(f'Request received at {datetime.now()}')