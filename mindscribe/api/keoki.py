```python
import requests

class KeokiAPI:
    def __init__(self):
        self.base_url = "https://api.keoki.com"

    def get_persona(self, persona_name):
        response = requests.get(f"{self.base_url}/persona/{persona_name}")
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_response(self, persona, query):
        response = requests.post(f"{self.base_url}/response", json={"persona": persona, "query": query})
        if response.status_code == 200:
            return response.json()
        else:
            return None
```