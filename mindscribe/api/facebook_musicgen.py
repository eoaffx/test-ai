```python
import requests

class FacebookMusicGenAPI:
    def __init__(self):
        self.base_url = "https://api.replicate.ai/facebook/musicgen"

    def generate_music(self, settings):
        response = requests.post(self.base_url, json=settings)
        if response.status_code == 200:
            return response.json()
        else:
            return None
```