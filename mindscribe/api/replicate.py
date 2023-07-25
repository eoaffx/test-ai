```python
import requests
from flask import current_app

def summarize_text(url):
    """
    Function to summarize text using Replicate API
    """
    try:
        response = requests.post(
            f"{current_app.config['REPLICATE_API_URL']}/summarize",
            json={"url": url},
            headers={"Authorization": f"Bearer {current_app.config['REPLICATE_API_KEY']}"}
        )
        response.raise_for_status()
        return response.json()["summary"]
    except requests.exceptions.RequestException as e:
        return str(e)

def generate_music(settings):
    """
    Function to generate custom study music using Facebook MusicGen API from Replicate
    """
    try:
        response = requests.post(
            f"{current_app.config['REPLICATE_API_URL']}/musicgen",
            json={"settings": settings},
            headers={"Authorization": f"Bearer {current_app.config['REPLICATE_API_KEY']}"}
        )
        response.raise_for_status()
        return response.json()["music"]
    except requests.exceptions.RequestException as e:
        return str(e)
```